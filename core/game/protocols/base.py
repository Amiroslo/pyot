# This is the "common protocol" in which all other sub protocols is based upon
from packet import TibiaPacket
from twisted.internet.defer import Deferred, inlineCallbacks
from twisted.internet import defer, reactor
from twisted.python import log
import game.enum
import game.map
enum = game.enum
import math
import config
import sys
import game.scriptsystem
from collections import deque
import game.resource
import game.item
import game.party
from struct import pack, unpack

# Probably not a good place, but
from game.creature import Creature

class BasePacket(TibiaPacket):
    maxKnownCreatures = 1300
    maxOutfits = 29
    maxMounts = 25
    protocolEnums = {}
    _ok_ = []
    """protocolEnums["MSG_NONE"] = 0
    protocolEnums["MSG_SPEAK_SAY"] = 0x01
    protocolEnums["MSG_SPEAK_WHISPER"] = 0x02
    protocolEnums["MSG_SPEAK_YELL"] = 0x03
    protocolEnums["MSG_SPEAK_MONSTER_SAY"] = 0x13
    protocolEnums["MSG_SPEAK_MONSTER_YELL"] = 0x14
    
    protocolEnums["MSG_STATUS_CONSOLE_RED"] = 0x12
    protocolEnums["MSG_EVENT_ORANGE"] = 0x13
    protocolEnums["MSG_STATUS_CONSOLE_ORANGE"] = 0x14
    protocolEnums["MSG_STATUS_WARNING"] = 0x15
    protocolEnums["MSG_EVENT_ADVANCE"] = 0x16
    protocolEnums["MSG_EVENT_DEFAULT"] = 0x17
    protocolEnums["MSG_STATUS_DEFAULT"] = 0x18
    protocolEnums["MSG_INFO_DESCR"] = 0x19
    protocolEnums["MSG_STATUS_SMALL"] = 0x1A
    protocolEnums["MSG_STATUS_CONSOLE_BLUE"] = 0x1B""" # TODO fix this!

    def enum(self, key):
        #return self.protocolEnums[key]
        return getattr(game.enum, key)
        
    # Position
    # Parameters is list(x,y,z)
    def position(self, position):
        self.data += pack("<HHB", position.x, position.y, position.z)

    # Magic Effect
    def magicEffect(self, pos, type):
        self.data += pack("<BHHBB", 0x83, pos.x, pos.y, pos.z, type)
   
    # Shoot
    def shoot(self, fromPos, toPos, type):
        self.uint8(0x85)
        self.position(fromPos)
        self.position(toPos)
        self.uint8(type)

    # Item
    # Parameters is of class Item or ItemID
    def item(self, item, count=None):
        if isinstance(item, game.item.Item):
            self.uint16(item.cid)
                
            if item.stackable:
                self.uint8(item.count or 1)
            elif item.type in (11,12):
                self.uint8(item.fluidSource or 0)
            if item.animation:
                self.uint8(0xFE)
            
        else:
            self.uint16(item)
            if count:
                self.uint8(count)
        
    # Map Description (the entier visible map)
    # Isn't "Description" a bad word for it?
    def mapDescription(self, position, width, height, player):
        skip = -1
        start = 7
        end = 0
        step = -1

        # Lower then ground level
        if position.z > 7:
            start = position.z - 2
            end = min(15, position.z + 2) # Choose the smallest of 15 and z + 2
            step = 1

        # Run the steps by appending the floor
        for z in xrange(start, (end+step), step):
            skip = self.floorDescription(position.x, position.y, z, width, height, position.z - z, skip, player)

        if skip >= 0:
            self.data += pack(">H", (skip << 8) + 0xFF)

    def _helpGetTile(self,x,y,z,area,instanceId):
        iX = x / 32
        iY = y / 32
        pX = x -iX * 32
        pY = y -iY * 32
                
        sectorSum = (iX * 32768) + iY
        try:
            return area[sectorSum][z][pX][pY]
        except KeyError:
            if game.map.loadTiles(x, y, instanceId):
                try:
                    return area[sectorSum][z][pX][pY]
                except:
                    return None
        except:
            return None
            
    # Floor Description (the entier floor)
    def floorDescription(self, _x, _y, _z, width, height, offset, skip, player):
        instanceId = player.position.instanceId
        area = game.map.knownMap[instanceId]
        
        for x in xrange(0, width):
            for y in xrange(0, height):
                tile = self._helpGetTile(_x + x + offset, _y + y + offset, _z, area, instanceId)

                if tile and tile.things:
                    if skip >= 0:
                        self.data += pack(">H", (skip << 8) + 0xFF)
                    skip = 0
                    self.tileDescription(tile, player)
                else:
                    skip += 1
                    if skip == 0xFF:
                        self.data += pack(">H", (skip << 8) + 0xFF)
                        skip = -1
        return skip

    def tileDescription(self, tile, player):
        self.data += pack("<H", 0)
        count = 0
        for item in tile.topItems():  
            self.data += pack("<H", item.cid)
                    
            if item.stackable:
                self.data += chr(item.count or 1)
            elif item.type in (11,12):
                self.data += chr(item.fluidSource or 0)
            if item.animation:
                self.data += chr(0xFE)
            count += 1
            if count == 10:
                return
        
        for creature in tile.creatures():
            known = False
            removeKnown = 0
            if player:
                known = creature in player.knownCreatures
                    
                if not known:
                    if len(player.knownCreatures) > self.maxKnownCreatures:
                        removeKnown = player.checkRemoveKnown()
                        if not removeKnown:
                            player.exit("Too many creatures in known list. Please relogin")
                            return
                    player.knownCreatures.add(creature)
                    creature.knownBy.add(player)
                    
                self.creature(creature, known, removeKnown)
            if creature.creatureType != 0 and not creature.brainEvent:
                creature.base.brain.handleThink(creature, False)
                    
            count += 1
            if count == 10:
                return
                
        for item in tile.bottomItems():
            self.data += pack("<H", item.cid)
                    
            if item.stackable:
                self.data += chr(item.count or 1)
            elif item.type in (11,12):
                self.data += chr(item.fluidSource or 0)
            if item.animation:
                self.data += chr(0xFE)
            count += 1
            if count == 10:
                return

    def exit(self, message):
        self.uint8(0x14)
        self.string(message) # Error message

    def outfit(self, look, addon=0, mount=0x00):
        
        self.uint16(look[0])
        if look[0] != 0:
            self.uint8(look[1])
            self.uint8(look[2])
            self.uint8(look[3])
            self.uint8(look[4])
            self.uint8(addon)
        else:
            self.uint16(look[1])
        if config.allowMounts:    
            self.uint16(mount) # Mount
        else:
            self.uint16(0)
            
    def creature(self, creature, known, removeKnown=0):
        if known:
            self.uint16(0x62)
            self.uint32(creature.clientId())
        else:
            self.uint16(0x61)
            self.uint32(removeKnown) # Remove known
            self.uint32(creature.clientId())
            self.uint8(creature.creatureType)
            self.string(creature.name())
            
        if not creature.getHideHealth():
            self.uint8(int(round((float(creature.data["health"]) / creature.data["healthmax"]) * 100))) # Health %
        else:
            self.uint8(0)
            
        self.uint8(creature.direction) # Direction
        self.outfit(creature.outfit, creature.addon, creature.mount if creature.mounted else 0x00)
        self.uint8(0) # Light
        self.uint8(0) # Light
        self.uint16(int(creature.speed)) # Speed
        self.uint8(creature.skull) # Skull
        self.uint8(creature.shield) # Party/Shield
        if not known:
            self.uint8(creature.emblem) # Emblem
        self.uint8(creature.solid) # Can't walkthrough
        
    def worldlight(self, level, color):
        self.uint8(0x82)
        self.uint8(level)
        self.uint8(color)

    def creaturelight(self, cid, level, color):
        self.uint8(0x8D)
        self.uint32(cid)
        self.uint8(level)
        self.uint8(color)

    def removeInventoryItem(self, pos):
        self.uint8(0x79)
        self.uint8(pos)
        
    def addInventoryItem(self, pos, item):
        self.uint8(0x78)
        self.uint8(pos)
        self.item(item)

    def addContainerItem(self, openId, item):
        self.uint8(0x70)
        self.uint8(openId)
        self.item(item)
        
    def updateContainerItem(self, openId, slot, item):
        self.uint8(0x71)
        self.uint8(openId)
        self.uint8(slot)
        self.item(item)
       
    def removeContainerItem(self, openId, slot):
        self.uint8(0x72)
        self.uint8(openId)
        self.uint8(slot)
        
    def addTileItem(self, pos, stackpos, item):
        if stackpos > 9: return
        
        self.uint8(0x6A)
        self.position(pos)
        self.uint8(stackpos)
        self.item(item)

    def addTileCreature(self, pos, stackpos, creature, player=None, resend=False):
        if stackpos > 9: return
        
        self.uint8(0x6A)
        self.position(pos)
        self.uint8(stackpos)
        known = False
        removeKnown = 0
        if player:
            known = creature in player.knownCreatures
                    
            if not known:
                if len(player.knownCreatures) > self.maxKnownCreatures:
                    removeKnown = player.checkRemoveKnown()
                    if not removeKnown:
                        player.exit("Too many creatures in known list. Please relogin")
                        return
                player.knownCreatures.add(creature)
                creature.knownBy.add(player)
            elif resend:
                removeKnown = creature.clientId()
                known = False
            self.creature(creature, known, removeKnown)

    def moveUpPlayer(self, player, oldPos):
        self.uint8(0xBE)
        
        # Underground to surface
        if oldPos.z-1 == 7:
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, 5, 18, 14, 3, -1, player)
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, 4, 18, 14, 4, skip, player)
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, 3, 18, 14, 5, skip, player)
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, 2, 18, 14, 6, skip, player)
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, 1, 18, 14, 7, skip, player)
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, 0, 18, 14, 8, skip, player)

            if skip >= 0:
                self.uint8(skip)
                self.uint8(0xFF)
                
        elif oldPos.z-1 > 7: # Still underground
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, oldPos.z-3, 18, 14, 3, -1, player)
            
            if skip >= 0:
                self.uint8(skip)
                self.uint8(0xFF)
                
        self.uint8(0x68) # West
        self.mapDescription(Position(oldPos.x - 8, oldPos.y + 1 - 6, oldPos.z-1), 1, 14, player)
        
        self.uint8(0x65) # North
        self.mapDescription(Position(oldPos.x - 8, oldPos.y - 6, oldPos.z-1), 18, 1, player)
         
    def moveDownPlayer(self, player, oldPos):
        self.uint8(0xBF)
        if oldPos.z+1 == 8:
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, oldPos.z+1, 18, 14, -1, -1, player)
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, oldPos.z+2, 18, 14, -2, skip, player)
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, oldPos.z+3, 18, 14, -3, skip, player)

            if skip >= 0:
                self.uint8(skip)
                self.uint8(0xFF)
                
        elif oldPos.z+1 > 8:
            skip = self.floorDescription(oldPos.x - 8, oldPos.y - 6, oldPos.z+3, 18, 14, -3, -1, player)
            
            if skip >= 0:
                self.uint8(skip)
                self.uint8(0xFF)            
        
        self.uint8(0x66) # East
        self.mapDescription(Position(oldPos.x + 9, oldPos.y - 7, oldPos.z+1), 1, 14, player)
        self.uint8(0x67) # South
        self.mapDescription(Position(oldPos.x - 8, oldPos.y + 7, oldPos.z+1), 18, 1, player)

    def updateTileItem(self, pos, stackpos, item):
        if stackpos > 9: return
        self.uint8(0x6B)
        self.position(pos)
        self.uint8(stackpos)
        self.item(item)
        
    def removeTileItem(self, pos, stackpos):
        if stackpos > 9: return
        self.uint8(0x6C)
        self.position(pos)
        self.uint8(stackpos)
        
    def status(self, player):
        self.uint8(0xA0)
        self.uint16(player.data["health"])
        self.uint16(player.data["healthmax"])
        self.uint32(player.freeCapasity())
        self.uint32(player.data["capasity"] * 100)
        self.uint64(player.data["experience"])
        if player.data["level"] > 0xFFFF:
            self.uint16(0xFFFF)
        else:
            self.uint16(player.data["level"])
        self.uint8(int(math.ceil(float(config.levelFormula(player.data["level"]+1)) / player.data["experience"]))) # % to next level, TODO
        self.uint16(player.data["mana"]) # mana
        self.uint16(player.data["manamax"]) # mana max
        if player.data["maglevel"] > 255:
            self.uint8(255)
            self.uint8(255)
        else:
            self.uint8(player.data["maglevel"])
            self.uint8(player.data["maglevel"]) # TODO: Virtual cap? ManaBase
        self.uint8(int(player.data["manaspent"] / int(config.magicLevelFormula(player.data["maglevel"], player.getVocation().mlevel)))) # % to next level, TODO
        self.uint8(player.data["soul"]) # TODO: Virtual cap? Soul
        self.uint16(min(42 * 60, int(player.data["stamina"] / 60))) # Stamina minutes
        self.uint16(int(player.speed)) # Speed
        
        self.uint16(0x00) # Condition

    def skills(self, player):
        self.uint8(0xA1) # Skill type
        for x in xrange(game.enum.SKILL_FIRST, game.enum.SKILL_LAST+1):
            self.uint8(player.skills[x]) # Value / Level
            self.uint8(player.data["skills"][x]) # Base
            currHits = player.data["skill_tries"][x]
            goalHits = player.skillGoals[x]
            if currHits < 1:
                self.uint8(0)
            else:
                self.uint8(int(round((currHits / goalHits) * 100))) # %

    def cooldownIcon(self, icon, cooldown):
        self.uint8(0xA4)
        self.uint8(icon)
        self.uint32(cooldown * 1000)
        
    def cooldownGroup(self, group, cooldown):
        self.uint8(0xA5)
        self.uint8(group)
        self.uint32(cooldown * 1000)

    def violation(self, flag):
        pass # Not on 9.1

    def icons(self, icons):
        self.uint8(0xA2)
        self.uint16(icons)

    def message(self, player, message, msgType='MSG_STATUS_DEFAULT', color=0, value=0, pos=None):
        self.uint8(0xB4)
        self.uint8(self.enum(msgType))
        if msgType in ('MSG_DAMAGE_DEALT', 'MSG_DAMAGE_RECEIVED', 'MSG_DAMAGE_OTHERS'):
            if pos:
                self.position(pos)
            else:
                self.position(player.position)
            self.uint32(value)
            self.uint8(color)
            self.uint32(0)
            self.uint8(0)
        elif msgType in ('MSG_EXPERIENCE', 'MSG_EXPERIENCE_OTHERS', 'MSG_HEALED', 'MSG_HEALED_OTHERS'):
            if pos:
                self.position(pos)
            else:
                self.position(player.position)
            self.uint32(value)
            self.uint8(color)
            
        self.string(message)

    def vipLogin(self, playerId):
        self.uint8(0xD3)
        self.uint32(playerId)
        
    def vipLogout(self, playerId):
        self.uint8(0xD4)
        self.uint32(playerId)
        
    def vip(self, playerId, playerName, online=False):
        self.uint8(0xD2)
        self.uint32(playerId)
        self.string(playerName)
        self.uint8(online)
        
class BaseProtocol(object):
    Packet = BasePacket
    def handle(self, player, packet):
        packetType = packet.uint8()
        
        if packetType == 0x14: # Logout
            try:
                player.prepareLogout()
                player.client.transport.loseConnection()
            except:
                pass # Sometimes the connection is already dead
            
        elif packetType == 0x1E: # Keep alive
            player.pong()
            
        elif packetType == 0xA0: # Set modes
            player.setModes(packet.uint8(), packet.uint8(), packet.uint8())
            
        elif packetType in (0x6F, 0x70, 0x71, 0x72): # Turn packages
            player.turn(packetType - 0x6F)
            
        elif packetType == 0x64: # movement with multiple steps
            self.handleAutoWalk(player,packet)
    
        elif packetType == 0x69: # Stop autowalking
            player.stopAutoWalk()
            
        elif packetType in (0x65, 0x66, 0x67, 0x68): # Movement
            self.handleWalk(player,packetType - 0x65)
        
        elif packetType == 0x6A: # Northeast
            self.handleWalk(player,7)
            
        elif packetType == 0x6B: # Southeast
            self.handleWalk(player,5)

        elif packetType == 0x6C: # Northwest
            self.handleWalk(player,4)
            
        elif packetType == 0x6D: # Southwest
            self.handleWalk(player,6)
            
        elif packetType == 0x96: # Say
            self.handleSay(player,packet)
            
        elif packetType == 0x78: # Throw/move item
            self.handleMoveItem(player,packet)
        
        elif packetType == 0x79: # Look at in trade window
            self.handleLookAtTrade(player,packet)
            
        elif packetType == 0x7A: # Player brought from store
            self.handlePlayerBuy(player,packet)
            
        elif packetType == 0x7B: # Player sold to store
            self.handlePlayerSale(player,packet)
            
        elif packetType == 0x7C: # Player closed trade
            self.handleCloseTradeNPC(player, packet)
        
        elif packetType == 0x7D: # Request trade
            self.handleRequestTrade(player, packet)
            
        elif packetType == 0x7E: # Request trade
            self.handleLookAtInTrade(player, packet)
            
        elif packetType == 0x7F: # Request trade
            self.handleAcceptTrade(player, packet)
            
        elif packetType == 0x80: # Player close trade
            self.handleCloseTrade(player, packet)
            
        elif packetType == 0x82:
            self.handleUse(player,packet)

        elif packetType == 0x83:
            self.handleUseWith(player,packet)
            
        elif packetType == 0x84: # Hotkey usage etc
            self.handleUseBattleWindow(player, packet)
            
        elif packetType == 0x85: # Rotate item
            self.handleRotateItem(player,packet)
            
        elif packetType == 0x87: # Close container
            player.closeContainerId(packet.uint8())
            
        elif packetType == 0x88: # Arrow up container
            player.arrowUpContainer(packet.uint8())
        
        elif packetType == 0x89: # Text from textWindow
            self.handleWriteBack(player,packet)

        elif packetType == 0x8A: # Text from houseWindow
            self.handleWriteBackForHouses(player, packet)
            
        elif packetType == 0x97: # Request channels
            player.openChannels()

        elif packetType == 0x98: # Open channel
            player.openChannel(packet.uint16())
            
        elif packetType == 0x99: # Close channel
            player.closeChannel(packet.uint16())
            
        elif packetType == 0x8C: # Look at
            self.handleLookAt(player,packet)
        
        elif packetType == 0x9A: # Open private channel
            player.openPrivateChannel(game.engine.getPlayer(packet.string()))
            
        elif packetType == 0xA1: # Attack
            self.handleAttack(player,packet)

        elif packetType == 0xA2: # Follow
            self.handleFollow(player,packet)
            
        elif packetType == 0xA3: # Invite to party
            self.handleInviteToParty(player, packet)
            
        elif packetType == 0xA4: # Join party
            self.handleJoinParty(player, packet)
            
        elif packetType == 0xA5: # Revoke invite
            self.handleRevokePartyInvite(player, packet)
            
        elif packetType == 0xA6: # Pass leadership
            self.handlePassPartyLeadership(player, packet)
            
        elif packetType == 0xA7: # Leave party
            player.leaveParty()
            
        elif packetType == 0xC9:
            self.handleUpdateTile(player,packet)
            
        elif packetType == 0xCA:
            self.handleUpdateContainer(player,packet)
            
        elif packetType == 0xD2: # Request outfit
            player.outfitWindow()
            
        elif packetType == 0xD3: # Set outfit
            self.handleSetOutfit(player,packet)
        
        elif packetType == 0xD4 and config.allowMounts: # Set mount status
            self.handleSetMounted(player,packet)

        elif packetType == 0xDC: # Add VIP
            self.handleAddVip(player,packet)
            
        elif packetType == 0xDD: # remove VIP
            self.handleRemoveVip(player,packet)
            
        elif packetType == 0xBE: # Stop action
            player.stopAction()
            
        elif packetType == 0xE7: # Thanks
            self.handleThanks(player, packet)
        
        elif packetType == 0xF0:
            player.questLog()
            
        elif packetType == 0xF1:
            self.handleQuestLine(player, packet)
            
        else:
            log.msg("Unhandled packet (type = {0}, length: {1}, content = {2})".format(hex(packetType), len(packet.data), ' '.join( map(str, map(hex, map(ord, packet.getData())))) ))
            #self.transport.loseConnection()
            
    def handleSay(self, player, packet):
        channelType = packet.uint8()
        channelId = 0
        reciever = ""
        if channelType in (enum.MSG_CHANNEL_MANAGEMENT, enum.MSG_CHANNEL, enum.MSG_CHANNEL_HIGHLIGHT):
            channelId = packet.uint16()
        elif channelType in (enum.MSG_PRIVATE_TO, enum.MSG_GAMEMASTER_PRIVATE_TO):
            reciever = packet.string()

        text = packet.string()
        
        player.handleSay(channelType, channelId, reciever, text)
        
    def handleAutoWalk(self, player, packet):
        if player.target:
            player.target = None
        player.stopAction()  
        player.walkPattern = deque()
        
        steps = packet.uint8()

        walkPattern = deque()
        for x in xrange(0, steps):
            direction = packet.uint8()
            if direction == 1:
                walkPattern.append(1) # East
            elif direction == 2:
                walkPattern.append(7) # Northeast
            elif direction == 3:
                walkPattern.append(0) # North
            elif direction == 4:
                walkPattern.append(6) # Northwest          
            elif direction == 5:
                walkPattern.append(3) # West
            elif direction == 6:
                walkPattern.append(4) # Southwest
            elif direction == 7:
                walkPattern.append(2) # South
            elif direction == 8:
                walkPattern.append(5) # Southeast           
            else:
                continue # We don't support them
        
        player.walkPattern = walkPattern
        game.engine.autoWalkCreature(player)

    def handleWalk(self, player, direction):
        if player.target and player.modes[1] == game.enum.CHASE and player.targetMode > 0:
            player.cancelTarget()
            
        player.walkPattern = deque([direction])
        game.engine.autoWalkCreature(player)
            
    @inlineCallbacks
    def handleMoveItem(self, player, packet):
        from game.item import Item, sid, items
        fromPosition = packet.position(player.position.instanceId)
        fromMap = False
        toMap = False

        if fromPosition.x != 0xFFFF:
            # From map
            fromMap = True
        
        clientId = packet.uint16()
        fromStackPos = packet.uint8()
        toPosition = packet.position(player.position.instanceId)
        if toPosition.x != 0xFFFF:
            toMap = True
        
        count = packet.uint8()
        oldItem = None
        renew = False
        stack = True
        
        thing = player.findItem(fromPosition.setStackpos(fromStackPos))
        
        isCreature = False
        if clientId < 100:
            isCreature = True
        if not isCreature:
            # Remove item:
            if toPosition.x == 0xFFFF:
                currItem = player.findItemWithPlacement(toPosition)
            else:
                currItem = None
    
            """if currItem and currItem[1] and not ((currItem[1].stackable and currItem[1].itemId == sid(clientId)) or currItem[1].containerSize):
                currItem[1] = None
            """
            if fromMap:
                # This means we need to walk to the item
                if not player.inRange(fromPosition, 1, 1):

                    walkPattern = game.engine.calculateWalkPattern(player, player.position, fromPosition, -1)

                    # No walk pattern means impossible move.
                    if not walkPattern:
                        player.notPossible()
                        return

                    # Some half sync yield -> sleep walking
                    def sleep(seconds):
                        d = Deferred()
                        reactor.callLater(seconds, d.callback, seconds)
                        return d
                    
                    walking = [True]
                    scount = 0
                    player.walkPattern = deque(walkPattern)
                    game.engine.autoWalkCreature(player, lambda: walking.pop())
                    while walking and scount < 20:
                        yield sleep(0.5)
                        scount += 1

                    # Vertify, we might have been stopped on the run
                    if not player.inRange(fromPosition, 1, 1):
                        player.notPossible()
                        return
  
                    if toPosition.x == 0xFFFF and toPosition.y >= 64 and not player.getContainer(toPosition.y-64):
                        player.notPossible()
                        return
                    
                #stream = player.packet()
                oldItem = player.findItemWithPlacement(fromPosition.setStackpos(fromStackPos))
                slots = oldItem[1].slots()
                checkSlots = False
                # Before we remove it, can it be placed there?
                if toPosition.x == 0xFFFF and toPosition.y < 64 and (toPosition.y-1) not in (game.enum.SLOT_DEPOT, game.enum.SLOT_AMMO) and (toPosition.y-1) != game.enum.SLOT_BACKPACK:
                    checkSlots = True
                    if (toPosition.y-1) not in slots:
                        player.notPossible()
                        return
                    
                if not oldItem[1].movable or (toPosition.x == 0xFFFF and not oldItem[1].pickable):
                    player.notPickable()
                    return
                    
                elif oldItem[1].openIndex != None and oldItem[1].openIndex == toPosition.y-64: # Moving into self
                    player.notPossible()
                    return
                    
                if oldItem[1].stackable and count > oldItem[1].count:
                    player.notPossible()
                    return
                
                if currItem and currItem[1] and currItem[1].itemId == oldItem[1].itemId and currItem[1].stackable:
                    count = min(100-currItem[1].count, count)
                if oldItem[1].stackable and count <= 100:
                    renew = True

                    oldItem[1].count -= count
                    if oldItem[1].count > 0:
                        stream = player.packet() # Hack
                        stream.updateTileItem(fromPosition, fromStackPos, oldItem[1])
                        stream.sendto(game.engine.getSpectators(fromPosition)) # Hack
                    else:
                        #stream.removeTileItem(fromPosition, fromStackPos)
                        #game.map.getTile(fromPosition).removeItem(oldItem[1])
                        tile = game.map.getTile(fromPosition) # Hack
                        tile.removeItem(oldItem[1])
                        game.engine.updateTile(fromPosition, tile)
                else:
                    #stream.removeTileItem(fromPosition, fromStackPos)
                    #game.map.getTile(fromPosition).removeItem(oldItem[1])
                    tile = game.map.getTile(fromPosition) # Hack
                    tile.removeItem(oldItem[1])
                    game.engine.updateTile(fromPosition, tile)                    
                #stream.sendto(game.engine.getSpectators(fromPosition))
                
                # Dual handed etc
                if toPosition.x == 0xFFFF and toPosition.y < 64 and len(slots) > 1:
                    for slot in slots[1:]:
                        item = player.inventory[slot-1]
                        player.removeItem(Position(0xFFFF, slot, 0))
                        player.addItem(item)
                        
                
            else:
                stream = player.packet()
                        
                oldItem = player.findItemWithPlacement(fromPosition.setStackpos(fromStackPos))

                # Before we remove it, can it be placed there?
                if toPosition.x == 0xFFFF and toPosition.y < 64 and (toPosition.y-1) != game.enum.SLOT_AMMO and (toPosition.y-1) != game.enum.SLOT_BACKPACK and (toPosition.y-1) not in oldItem[1].slots():
                    player.notPossible()
                    return
                elif oldItem[1].inTrade:
                    player.message("Your trading this item.")
                    return
                    
                elif oldItem[1].openIndex != None and oldItem[1].openIndex == toPosition.y-64: # Moving into self
                    player.notPossible()
                    return    
                        
                elif currItem and currItem[1] and toPosition.x == 0xFFFF and toPosition.y >= 64 and currItem[1].containerSize:
                    
                        
                    container = currItem[1].inContainer
                    if container:
                        if container == oldItem[1]:
                            player.notPossible()
                            return
                        else:
                            container = container.inContainer
                            while container:
                                if container == oldItem[1]:
                                    player.notPossible()
                                    return
                                
                if oldItem[1].stackable and count <= 100:
                    if (count == oldItem[1].count and player.removeCache(oldItem[1])) or (player.modifyCache(oldItem[1], -1 * count)):
                        player.refreshStatus(stream)
                        
                    renew = True
                    oldItem[1].count -= count
                    if oldItem[1].count > 0:
                        if oldItem[0] == 1:
                            stream.addInventoryItem(fromPosition.y, oldItem[1])
                        elif oldItem[0] == 2:
                            stream.updateContainerItem(oldItem[2].openIndex, fromPosition.z, oldItem[1])
                            
                    else:
                        if oldItem[0] == 1:
                            player.inventory[fromPosition.y-1] = None
                            stream.removeInventoryItem(fromPosition.y)
                        elif oldItem[0] == 2:
                            oldItem[2].container.removeItem(oldItem[1])
                            stream.removeContainerItem(oldItem[2].openIndex, fromPosition.z)

                else:
                    if player.removeCache(oldItem[1]):
                        player.refreshStatus(stream)
                        
                    if oldItem[0] == 1:
                        game.scriptsystem.get("unequip").runSync(player, player.inventory[fromPosition.y-1], slot = (toPosition.y-1))
                        player.inventory[fromPosition.y-1] = None
                        stream.removeInventoryItem(fromPosition.y)
                    elif oldItem[0] == 2:
                        oldItem[2].container.removeItem(oldItem[1])
                        stream.removeContainerItem(oldItem[2].openIndex, fromPosition.z)
                
                if toPosition.y == fromPosition.y:
                    stack = False
                    
                stream.send(player.client)
                
            if toMap:
                stream = player.packet()
                if renew:
                    newItem = Item(sid(clientId), count)
                else:
                    newItem = oldItem[1]
                thisTile = game.map.getTile(toPosition)
                findItem = thisTile.findClientItem(clientId, True) # Find item for stacking
                if findItem and newItem.stackable and count <= 100 and findItem[1].count + count <= 100:
                    findItem[1].count += count
                    #stream.removeTileItem(toPosition, findItem[0])
                    #game.map.getTile(toPosition).removeItem(findItem[1])
                    stream.updateTileItem(toPosition, thisTile.findStackpos(findItem[1]), findItem[1])
                else:
                    toStackPos = None

                    process = [0]
                    
                    _items_ = thisTile.getItems()
                    count = len(_items_) * 2
                    for item in _items_:
                        yield game.scriptsystem.get('useWith').runDeferNoReturn(item, player, lambda: process.__setitem__(0, process[0]+1), position=toPosition, onPosition=fromPosition, onThing=newItem)
                        yield game.scriptsystem.get('useWith').runDeferNoReturn(newItem, player, lambda: process.__setitem__(0, process[0]+1), position=fromPosition, onPosition=toPosition, onThing=item)
                    if process[0] == count:
                        if newItem.decayPosition:
                            newItem.decayPosition = toPosition
                            
                        toStackPos = game.map.getTile(toPosition).placeItem(newItem)
                        stream.addTileItem(toPosition, toStackPos, newItem)
                        if not renew and newItem.containerSize and newItem.openIndex != None and not player.inRange(toPosition, 1, 1):
                            player.closeContainer(newItem)
                stream.sendto(game.engine.getSpectators(toPosition))
            else:
                sendUpdate = False
                if player.freeCapasity() - ((oldItem[1].weight or 0) * (oldItem[1].count or 1)) < 0:
                    player.tooHeavy()
                    tile = game.map.getTile(player.position)
                    tile.placeItem(Item(sid(clientId), count) if renew else oldItem[1])
                    game.engine.updateTile(player.position, tile)
                else:
                    stream = player.packet()    
                    if currItem and currItem[1] and currItem[1].containerSize:
                        ret = player.itemToContainer(currItem[1], Item(sid(clientId), count) if renew else oldItem[1], count=count, stack=stack)

                    elif currItem and (currItem[0] == 2) and currItem[2]:
                        ret = player.itemToContainer(currItem[2], Item(sid(clientId), count) if renew else oldItem[1], count=count, stack=stack)
                    
                    else:
                        """if currItem:
                            player.addItem(currItem[1])"""
                        if toPosition.y < 64:
                            if oldItem[1].stackable and player.inventory[toPosition.y-1] and player.inventory[toPosition.y-1].itemId == sid(clientId) and (player.inventory[toPosition.y-1].count + count <= 100):
                                player.inventory[toPosition.y-1].count += count
                                # Into inventory? Update cache
                                if player.modifyCache(player.inventory[toPosition.y-1], count):
                                    player.refreshStatus(stream)
                            else:       
                                player.inventory[toPosition.y-1] = Item(sid(clientId), count) if renew else oldItem[1]
                                game.scriptsystem.get("equip").runSync(player, player.inventory[toPosition.y-1], slot = (toPosition.y-1))
                                
                                if player.inventory[toPosition.y-1].decayPosition:
                                    player.inventory[toPosition.y-1].decayPosition = (toPosition.x, toPosition.y)
                                    
                                if player.inventory[toPosition.y-1].decayCreature:
                                    player.inventory[toPosition.y-1].decayCreature = player
                                    
                                # Into inventory? Update cache
                                if player.addCache(player.inventory[toPosition.y-1]):
                                    player.refreshStatus(stream)                            
                            stream.addInventoryItem(toPosition.y, player.inventory[toPosition.y-1])
                        else:
                            container = player.getContainer(toPosition.y-64)

                            try:
                                container.container.items[toPosition.z] = Item(sid(clientId), count) if renew else oldItem[1]
                                sendUpdate = True

                                if container.container.items[toPosition.z].decayPosition:
                                    container.container.items[toPosition.z].decayPosition = (toPosition.x, 65)
                                    
                                if container.container.items[toPosition.z].decayCreature:
                                    container.container.items[toPosition.z].decayCreature = player
                                    
                                try:
                                    player.inventoryCache[container.itemId].index(container)
                                    # Into inventory? Update cache
                                    if player.addCache(container.container.items[toPosition.z], container):
                                        player.refreshStatus(stream)
                                except:
                                    pass
                                
                            except:
                                pass
                                #player.itemToContainer(container, Item(sid(clientId), count) if renew else oldItem[1], stack=stack, streamX=stream)                  
                    
                    if currItem and currItem[1] and toPosition.y < 64 and not currItem[1].containerSize and not currItem[1].stackable:
                        player.itemToContainer(player.getContainer(fromPosition.y-64) or player.inventory[2], currItem[1].copy(), streamX=stream)
                        
                    """
                    if currItem and currItem[1] and not (fromMap and currItem[1].stackable) and not oldItem[1].containerSize and not (fromPosition.x == 0xFFFF and toPosition.x == 0xFFFF and fromPosition.y == toPosition.y) and not (fromPosition.x == 0xFFFF and fromPosition.y < 64) and not (fromPosition.x != 0xFFFF and toPosition.x == 0xFFFF):
                        if fromPosition.y < 64:
                            player.inventory[fromPosition.y-1] = currItem[1].copy()
                            
                            "if container.container.items[toPosition.z].decayPosition:
                                container.container.items[toPosition.z].decayPosition = (0xFFFF, fromPosition.y)
                                
                            if container.container.items[toPosition.z].decayCreature:
                                container.container.items[toPosition.z].decayCreature = player"
                                
                            stream.addInventoryItem(fromPosition.y, player.inventory[fromPosition.y-1])
                            
                            if player.addCache(oldItem[1]):
                                player.refreshStatus(stream)
                        else:
                            player.itemToContainer(player.getContainer(fromPosition.y-64) or player.inventory[2], currItem[1].copy(), streamX=stream)
                    """    
                    if sendUpdate:
                        stream.updateContainerItem(toPosition.y-64, toPosition.z, container.container.items[toPosition.z])
                    stream.send(player.client)
        else:
            if game.map.getTile(toPosition).creatures():
                player.notEnoughRoom()
                return
                
            creature = game.map.getTile(fromPosition).getThing(fromStackPos)
            
            if not creature or not creature.isPushable(player):
                player.message("Creature can't be pushed")
                return
                
            toTile = game.map.getTile(toPosition)
            for i in toTile.getItems():
                if i.solid:
                    player.notPossible()
                    return
            if abs(creature.position.x-player.position.x) > 1 or abs(creature.position.y-player.position.y) > 1:
                walkPattern = game.engine.calculateWalkPattern(player, creature.position, toPosition)
                if len(walkPattern) > 1:
                    player.outOfRange()
                else:
                    game.engine.autoWalkCreatureTo(player, creature.position, -1, True, lambda: game.engine.autoWalkCreature(creature, deque(walkPattern)))
            else:
                game.engine.autoWalkCreatureTo(creature, toPosition)
            
    def handleLookAt(self, player, packet):
        from game.item import sid, cid, items
        position = packet.position(player.position.instanceId)
        
        clientId = packet.uint16()
        stackpos = packet.uint8()
        
        stackPosition = position.setStackpos(stackpos)
        
        if position.x == 0xFFFF:
            thing = player.findItem(stackPosition)
        elif stackpos == 0 and clientId == 99:
            try:
                thing = game.map.getTile(position).creatures()[0]
            except:
                player.notPossible()
                return
        else:
            thing = player.findItem(stackPosition)     
            if not thing or thing.cid != clientId:
                for thing2 in game.map.getTile(position).things:
                    if thing2.cid == clientId:
                        thing = thing2
                        break
                    
        if thing:
            if isinstance(thing, game.item.Item):
                def afterScript():
                    extra = ""
                    # TODO propper description handling
                    if config.debugItems:
                        extra = "(ItemId: %d, Cid: %d)" % (thing.itemId, clientId)
                    player.message(thing.description(player, position) + extra, 'MSG_INFO_DESCR')
            elif isinstance(thing, Creature):
                def afterScript():
                    if self == thing:
                        player.message(thing.description(True), 'MSG_INFO_DESCR')
                    else:
                        player.message(thing.description(), 'MSG_INFO_DESCR')
            game.scriptsystem.get('lookAt').runSync(thing, player, afterScript, position=stackPosition)
        else:
            player.notPossible()

    def handleLookAtTrade(self, player, packet):
        from game.item import sid
        clientId = packet.uint16()
        count = packet.uint8()
        
        item = game.item.Item(sid(clientId), count)
        player.message(item.description(player), 'MSG_INFO_DESCR')
        del item
        
    def handleRotateItem(self, player, packet):
        position = packet.position(player.position.instanceId) # Yes, we don't support backpack rotations
        clientId = packet.uint16()
        stackpos = packet.uint8()
        
        if player.inRange(position, 1, 1):
            item = game.map.getTile(position).getThing(stackpos)
            def end():
                game.engine.transformItem(item, item.rotateTo, position, stackpos)
            game.scriptsystem.get('rotate').runSync(item, player, end, position=position.setStackpos(stackpos))
            
        
    def handleSetOutfit(self, player, packet):
        if config.playerCanChangeColor:
            player.outfit = [packet.uint16(), packet.uint8(), packet.uint8(), packet.uint8(), packet.uint8()]
        else:
            player.outfit[0] = packet.uint16()
            
        player.addon = packet.uint8()
        if config.allowMounts:
            player.mount = packet.uint16()
        player.refreshOutfit()
    
    def handleSetMounted(self, player, packet):
        if player.mount:
            mount = packet.uint8() != 0
            player.changeMountStatus(mount)
        else:
            player.outfitWindow()
            
    @inlineCallbacks        
    def handleUse(self, player, packet):
        position = packet.position(player.position.instanceId)

        clientId = packet.uint16() # Junk I tell you :p
        stackpos = packet.uint8()
        index = packet.uint8()
        stackPosition = position.setStackpos(stackpos)
        thing = player.findItem(stackPosition)
        end = None
        
        if thing and (position.x == 0xFFFF or (position.z == player.position.z and player.canSee(position))):
            if not position.x == 0xFFFF and not player.inRange(position, 1, 1):
                walkPattern = game.engine.calculateWalkPattern(player, player.position, position, -1)

                # No walk pattern means impossible move.
                if not walkPattern:
                    player.notPossible()
                    return

                # Some half sync yield -> sleep walking
                def sleep(seconds):
                    d = Deferred()
                    reactor.callLater(seconds, d.callback, seconds)
                    return d
                    
                walking = [True]
                scount = 0
                player.walkPattern = deque(walkPattern)
                game.engine.autoWalkCreature(player, lambda: walking.pop())
                while walking and scount < 20:
                    yield sleep(0.5)
                    scount += 1
            
            if position.x == 0xFFFF or player.inRange(position, 1, 1):
                game.scriptsystem.get('use').runSync(thing, player, None, position=stackPosition, index=index)
            
    @inlineCallbacks
    def handleUseWith(self, player, packet):
        position = packet.position(player.position.instanceId)
        clientId = packet.uint16() # Junk I tell you :p
        stackpos = packet.uint8()
        
        onPosition = packet.position(player.position.instanceId)
        onClientId = packet.uint16()
        onStack = packet.uint8()
        
        stackPosition1 = position.setStackpos(stackpos)
        stackPosition2 = onPosition.setStackpos(onStack)
        
        print stackPosition1
        print stackPosition2
        
        if clientId != 99:
            thing = player.findItem(stackPosition1)
        else:
            thing = position.getTile().creatures()[0]
            
        if onClientId != 99:
            onThing = player.findItem(stackPosition2)
        else:
            onThing = game.map.getTile(onPosition).creatures()[0]
        
        if thing and onThing and ((position.z == player.position.z and player.canSee(position)) or position.x == 0xFFFF) and ((onPosition.z == player.position.z and player.canSee(onPosition)) or onPosition.x == 0xFFFF):
            if not position.x == 0xFFFF and not player.inRange(position, 1, 1):
                walkPattern = game.engine.calculateWalkPattern(player, player.position, position, -1)

                # No walk pattern means impossible move.
                if not walkPattern:
                    player.notPossible()
                    return

                # Some half sync yield -> sleep walking
                def sleep(seconds):
                    d = Deferred()
                    reactor.callLater(seconds, d.callback, seconds)
                    return d
                    
                walking = [True]
                scount = 0
                player.walkPattern = deque(walkPattern)
                game.engine.autoWalkCreature(player, lambda: walking.pop())
                while walking and scount < 20:
                    yield sleep(0.5)
                    scount += 1

            if position.x == 0xFFFF or player.inRange(position, 1, 1):
                end = lambda: game.scriptsystem.get('useWith').runDeferNoReturn(onThing, player, None, position=stackPosition2, onPosition=stackPosition1, onThing=thing)
                game.scriptsystem.get('useWith').runDeferNoReturn(thing, player, end, position=stackPosition1, onPosition=stackPosition2, onThing=onThing)


    def handleAttack(self, player, packet):
        # HACK?
        # If we're in protected zone
        if player.position.getTile().getFlags() & TILEFLAGS_PROTECTIONZONE:
            player.notPossible()
            player.cancelTarget()
        else:
            cid = packet.uint32()
            player.setAttackTarget(cid)
            
    def handleFollow(self, player, packet):
        cid = packet.uint32()
        player.setFollowTarget(cid)
        
    def handleUpdateTile(self, player, packet):
        pos = packet.position(player.position.instanceId)
        tile = getTile(pos)
        stream = player.packet(0x69)
        stream.position(pos)
        stream.tileDescription(tile, player)
        stream.uint8(0x00)
        stream.uint8(0xFF)
        stream.send(player.client)
        
    def handleUpdateContainer(self, player, packet):
        openId = packet.uint8()
        
        parent = False
        try:
            parent = bool(container.parent)
        except:
            pass
        player.openContainer(player.openContainers[openId], parent=parent, update=True)
        
    def handlePlayerBuy(self, player, packet):
        from game.item import sid
        if not player.openTrade:
            return
            
        clientId = packet.uint16()
        count = packet.uint8()
        amount = packet.uint8()
        ignoreCapasity = packet.uint8()
        withBackpack = packet.uint8()
        
        player.openTrade.buy(player, sid(clientId), count, amount, ignoreCapasity, withBackpack)
        
    def handlePlayerSale(self, player, packet):
        from game.item import sid
        if not player.openTrade:
            return
            
        clientId = packet.uint16()
        count = packet.uint8()
        amount = packet.uint8()
        ignoreEquipped = packet.uint8() 
        
        player.openTrade.sell(player, sid(clientId), count, amount, ignoreEquipped)

    def handleWriteBack(self, player, packet):
        windowId = packet.uint32()
        text = packet.string()
        
        try:
            player.windowHandlers[windowId](text)
            del player.windowHandlers[windowId] # Cleanup
        except:
            pass
        
    def handleWriteBackForHouses(self, player, packet):
        packet.pos += 1 # Skip doorId, no need in PyOT :)
        windowId = packet.uint32()
        text = packet.string()
        
        try: # Try blocks are better than x in y checks :)
            player.windowHandlers[windowId](text)
            del player.windowHandlers[windowId] # Cleanup
        except:
            pass
        
    def handleQuestLine(self, player, packet):
        questId = packet.uint16()-1
        player.questLine(game.resource.getQuest(questId).name)
        
    def handleAddVip(self, player, packet):
        player.addVipByName(packet.string())
        
    def handleRemoveVip(self, player, packet):
        player.removeVip(packet.uint32())
        
    def handleRequestTrade(self, player, packet):
        position = packet.position(player.position.instanceId)
        itemId = packet.uint16()
        stackpos = packet.uint8()
        player2 = game.engine.getCreatureByCreatureId(packet.uint32())
        
        if not player.inRange(player2.position, 2, 2):
            player.message("You need to move closer.")
            return
            
        if position.x == 0xFFFF:
            thing = player.findItem(position, stackpos)
            if thing in player.tradeItems:
                player.message("Your already trading this item.")
                return
        else:
            return
        
        
        if player2.isTradingWith and player2.isTradingWith != player:
            player.message("This player is already trading.")
            return
        
        thing.inTrade = True
        
        # Modifing the current trade    
        if player.isTradingWith == player2:
            player.tradeItems.append(thing)
            # Close trade since we're refreshing it
            player2.closeTrade()
            player.closeTrade()
            
            if player.startedTrade:
                starter = player
                trader = player2
            else:
                starter = player2
                trader = player
                
            player2.tradeItemRequest(starter, starter.tradeItems, True)
            if player2.tradeItems:
                player2.tradeItemRequest(trader, trader.tradeItems, False)
                player.tradeItemRequest(trader, trader.tradeItems, True)
                player.tradeItemRequest(starter, starter.tradeItems, False)
            else:
                player.tradeItemRequest(starter, starter.tradeItems, True)

        else:
            player2.message("%s wish to trade with you." % player.name())
            
            player.tradeItems = [thing]
            
            player.tradeItemRequest(player, player.tradeItems, True)
            player2.tradeItemRequest(player, player.tradeItems, True)
            
            player.isTradingWith = player2
            player2.isTradingWith = player
            player.startedTrade = True
            player2.startedTrade = False
            
    def handleCloseTrade(self, player, packet, c=False):
        player.closeTrade()
        if player.isTradingWith:
            if not c:
                player.isTradingWith.message("Trade cancelled.")
                for item in player.isTradingWith.tradeItems:
                    del item.inTrade
                
            player.isTradingWith.tradeItems = []
            player.isTradingWith.isTradingWith = None
            player.isTradingWith.closeTrade()
            player.isTradingWith.tradeAccepted = False
            
            if not c:
                player.message("Trade cancelled.")
                for item in player.tradeItems:
                    del item.inTrade
                    
            player.tradeItems = []
            
            player.isTradingWith = None
            player.tradeAccepted = False
            
    def handleCloseTradeNPC(self, player, packet):
        if player.openTrade:
            player.openTrade.farewell(player)
            player.closeTrade()

            
    def handleLookAtInTrade(self, player, packet):
        counter = packet.uint8()
        stackpos = packet.uint8()
        thing = None
        if counter:
            try:
                thing = player.isTradingWith.tradeItems[stackpos]
            except:
                pass
        else:
            try:
                thing = player.tradeItems[stackpos]
            except:
                pass
            
        if thing:
            def afterScript():
                extra = ""
                # TODO propper description handling
                if config.debugItems:
                    extra = "(ItemId: %d, Cid: %d)" % (thing.itemId, thing.cid)
                player.message(thing.description(player) + extra, 'MSG_INFO_DESCR')
            game.scriptsystem.get('lookAtTrade').runSync(thing, player, afterScript, position=game.map.StackPosition(0xFFFE, counter, 0, stackpos))
            
    def handleAcceptTrade(self, player, packet):
        if player.isTradingWith.tradeAccepted:
            for item in player.isTradingWith.tradeItems:
                del item.inTrade
                if item.decayCreature and not item.inContainer:
                   item.decayCreature.inventory[item.decayCreature.inventory.index(item)] = None
                if item.decayCreature:
                    player.isTradingWith.removeCache(item)
                if item.inContainer:
                    item.inContainer.removeItem(item)
                    
                
            for item in player.tradeItems:
                del item.inTrade
                if item.decayCreature and not item.inContainer:
                    item.decayCreature.inventory[item.decayCreature.inventory.index(item)] = None
                if item.decayCreature:
                    player.isTradingWith.removeCache(item)
                if item.inContainer:
                    item.inContainer.removeItem(item)
                    
            for item in player.tradeItems:
                player.isTradingWith.addItem(item)
                
            for item in player.isTradingWith.tradeItems:
                player.addItem(item)
                
            player.message("Trade completed.")
            player.updateAllContainers()
            player.isTradingWith.message("Trade completed.")
            player.isTradingWith.updateAllContainers()
            self.handleCloseTrade(player, None, True)
            
        else:
            player.tradeAccepted = True
            player.isTradingWith.message("Offer accepted. Whats your take on this?")
            
    @inlineCallbacks        
    def handleUseBattleWindow(self, player, packet):
        position = packet.position(player.position.instanceId)
        clientItemId = packet.uint16()
        stackpos = packet.uint8()
        creature = game.engine.getCreatureByCreatureId(packet.uint32())
        hotkey = position.x == 0xFFFF and not position.y
        stackPosition = position.setStackpos(stackpos)
        # Is hotkeys allowed?
        if not config.enableHotkey:
            player.cancelMessage("Hotkeys are disabled.")
            return
            
        # Are we in distance to object?
        if player != creature and not player.inRange(creature.position, 7, 5):
            player.cancelMessage("Target is too far away.")
            return 
        
        if not hotkey:
            thing = player.findItem(stackPosition)
        else:
            itemId = game.item.sid(clientItemId)
            thing = player.findItemById(itemId)
            
            if not thing:
                player.cancelMessage("You don't have any left of this item.")
                
                return
                
            # Also tell hotkey message
            count = player.inventoryCache[itemId][0]
            
            if not thing.showCount:
                player.message("Using one of %s..." % thing.rawName())
            elif count == 1:
                player.message("Using the last %s..." % thing.rawName())
            else:
                player.message("Using one of %d %s..." % (count, thing.rawName()))
        
        if thing and (position.x == 0xFFFF or (position.z == player.position.z and player.canSee(position))):
            if not position.x == 0xFFFF and not player.inRange(position, 1, 1):
                walkPattern = game.engine.calculateWalkPattern(player, player.position, position, -1)

                # No walk pattern means impossible move.
                if not walkPattern:
                    player.notPossible()
                    return

                # Some half sync yield -> sleep walking
                def sleep(seconds):
                    d = Deferred()
                    reactor.callLater(seconds, d.callback, seconds)
                    return d
                    
                walking = [True]
                scount = 0
                player.walkPattern = deque(walkPattern)
                game.engine.autoWalkCreature(player, lambda: walking.pop())
                while walking and scount < 20:
                    yield sleep(0.5)
                    scount += 1
            
            if position.x == 0xFFFF or player.inRange(position, 1, 1):
                game.scriptsystem.get('use').runSync(thing, player, None, position=stackPosition)

        
    def handleInviteToParty(self, player, packet):
        creature = game.engine.getCreatureByCreatureId(packet.uint32())
        
        if creature.party():
            player.message("%s is already in a party." % creature.name())
            return
            
        # Grab the party
        party = player.party()
        if not party:
            # Make a party
            party = player.newParty()
        elif party.leader != player:
            return player.message("Your not the party leader!")
        
        party.addInvite(creature)
        
    def handleJoinParty(self, player, packet):
        creature = game.engine.getCreatureByCreatureId(packet.uint32())

        # Grab the party
        party = creature.party()
        if not party or party.leader != creature:
            return
        
        party.addMember(creature)
        
    def handleRevokePartyInvite(self, player, packet):
        creature = game.engine.getCreatureByCreatureId(packet.uint32())
        
        if creature.party() == player.party():
            player.message("%s is already a member of the party." % creature.name())
            return
            
        # Grab the party
        party = player.party()
        if not party or party.leader != player:
            return
        
        party.removeInvite(creature)        
        
    def handlePassPartyLeadership(self, player, packet):
        creature = game.engine.getCreatureByCreatureId(packet.uint32())
        
        if creature.party() != player.party():
            player.message("%s is not in your party." % creature.name())
            return
            
        # Grab the party
        party = player.party()
        if not party or party.leader != player:
            return
        
        party.changeLeader(creature)
        
    @inlineCallbacks
    def handleThanks(self, player, packet):
        messageId = packet.uint32()
        message = game.chat.getMessage(messageId)
        
        yield game.scriptsystem.get("thankYou").runDefer(player, messageId = messageId, author = message[0], channelType = message[3], channel = message[1], text = message[2])
