from game.creature import Creature, CreatureBase, uniqueId
import game.engine, game.map, game.scriptsystem
from packet import TibiaPacket
import copy, random, time
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from twisted.python import log
import game.enum
import game.errors
import game.item
import config

monsters = {}
brainFeatures = ({},{})

def chance(procent):
    def gen(monster):
        if 10 > random.randint(0, 100):
            return True
        else:
            return False
    return gen
    
class Monster(Creature):
    def generateClientID(self):
        return 0x40000000 + uniqueId()
        
    def __init__(self, base, position, cid=None):
        Creature.__init__(self, base.data.copy(), position, cid)
        self.base = base
        self.creatureType = 1
        self.spawnPosition = position[:]
        self.lastStep = 0
        self.speed = float(self.base.speed)
        self.lastMelee = 0
        self.walkPer = base.walkPer
        self.noBrain = True
        self.spawnTime = None
        self.radius = 5

    def damageToBlock(self, dmg, type):
        if type == game.enum.MELEE:
            return dmg - self.base.armor
        elif type == game.enum.PHYSICAL:
            return dmg * self.base.physical
        elif type == game.enum.FIRE:
            return dmg * self.base.fire
        elif type == game.enum.EARTH:
            return dmg * self.base.earth
        elif type == game.enum.ENERGY:
            return dmg * self.base.energy
        elif type == game.enum.ICE:
            return dmg * self.base.ice
        elif type == game.enum.HOLY:
            return dmg * self.base.holy
        elif type == game.enum.DEATH:
            return dmg * self.base.death
        elif type == game.enum.DROWN:
            return dmg * self.base.drown
        
        # What, no match?
        return dmg
        
    def onDeath(self):
        # Transform
        tile = game.map.getTile(self.position)

        corpse = game.item.Item(self.base.data["corpse"])
        for loot in self.base.lootTable:
            lenLoot = len(loot)
            if loot[1]*100 > random.randint(0, 10000):
                lenLoot = len(loot)
                if lenLoot == 2:
                    ret = corpse.container.placeItemRecursive(game.item.Item(loot[0], 1))
                    
                elif lenLoot == 3:
                    count = random.randint(1, loot[2])
                    if count > 100:
                        while count:
                            depCount = min(count, 100)
                            corpse.container.placeItemRecursive(game.item.Item(loot[0], depCount))
                            count -= depCount
                    else:        
                        ret = corpse.container.placeItemRecursive(game.item.Item(loot[0], count))
                        
                elif lenLoot == 4:
                    count = random.randint(loot[4], loot[2])
                    if count > 100:
                        while count:
                            depCount = min(count, 100)
                            ret = corpse.container.placeItemRecursive(game.item.Item(loot[0], depCount))
                            count -= depCount
                            
                    else:
                        ret = corpse.container.placeItemRecursive(game.item.Item(loot[0], count))
                        
            elif lenLoot == 4:
                ret = corpse.container.placeItemRecursive(game.item.Item(loot[0], loot[4]))
            
            if ret != 0:
                log.msg("Warning: Monster '%s' extends all possible loot space" % self.data['name'])
                break
                
        corpse.decay(self.position)
        splash = game.item.Item(game.enum.FULLSPLASH)
        splash.fluidSource = self.base.blood
        splash.decay(self.position)
        
        tile.placeItem(corpse)
        tile.placeItem(splash)
        try:
            tile.removeCreature(self)
        except:
            pass
        game.engine.updateTile(self.position, tile)
        
        if self.lastDamager and self.lastDamager.isPlayer():
            if self.lastDamager.data["stamina"] or config.noStaminaNoExp == False:
                self.lastDamager.modifyExperience(self.base.experience)

            if self.base.experience >= self.lastDamager.data["level"]:
                self.lastDamager.soulGain()
        Creature.onDeath(self)
        
        # Begin respawn
        # TODO just respawn <this> class, can't possibly bind so many kb :p
        if self.spawnTime:
            game.engine.safeCallLater(self.spawnTime, self.base.spawn, self.spawnPosition)
        else:
            game.engine.safeCallLater(self.base.spawnTime, self.base.spawn, self.spawnPosition)
            
    def say(self, message, messageType=game.enum.MSG_SPEAK_MONSTER_SAY):
        return Creature.say(self, message, messageType)
        
    def yell(self, message, messageType=game.enum.MSG_SPEAK_MONSTER_YELL):
        return Creature.yell(self, message, messageType)

    def description(self):
        return "You see %s" % self.base.data["description"]
        
class MonsterBase(CreatureBase):
    def __init__(self, data, brain):
        self.data = data
        self.voiceslist = []
        self.brain = brain
        self.scripts = {"onFollow":[], "onTargetLost":[]}
        self.summons = []
        
        self.spawnTime = 60
        
        self.speed = 100
        self.experience = 0
        
        
        self.setBehavior()
        self.setImmunity()
        self.walkAround()
        self.bloodType()
        self.setTargetChance()
        
        self.meleeAttacks = []
        self.spellAttacks = []
        self.defenceSpells = []
        
        self.intervals = {}
        self.lootTable = []
        
        self.walkable = True
        self.walkPer = config.monsterWalkPer
        
        self.brainFeatures = ["default"]
        
    def spawn(self, position, place=True, spawnTime=None, spawnDelay=0.5, radius=5, radiusTo=None):
        if spawnDelay:
            return game.engine.safeCallLater(spawnDelay, self.spawn, position, place, spawnTime, 0, radius, radiusTo)
        else:
            monster = Monster(self, position, None)
            if spawnTime:
                monster.spawnTime = spawnTime
            monster.radius = radius
            
            if radius <= 1:
                self.walkable = False
            if radiusTo:
                monster.radiusTo = radiusTo
            else:
                monster.radiusTo = (position[0], position[1])
                
            self.brain.beginThink(monster) # begin the heavy thought process!

            if self.targetChance and not (self.meleeAttacks or self.spellAttacks):
                log.msg("Warning: '%s' have targetChance, but no attacks!" % self.data["name"])
                
            if place:
                try:
                    stackpos = game.map.getTile(position).placeCreature(monster)
                    if stackpos > 9:
                        log.msg("Can't place creatures on a stackpos > 9")
                        return
                        
                    list = game.engine.getSpectators(position)
                    for client in list:
                        stream = TibiaPacket()
                        stream.magicEffect(position, 0x03)
                        stream.addTileCreature(position, stackpos, monster, client.player)
                
                        stream.send(client)
                except:
                    log.msg("Spawning of creature('%s') on %s failed" % (self.data["name"], str(position)))
            return monster
        
    def setHealth(self, health, healthmax=None):
        if not healthmax:
            healthmax = health
        self.data["health"] = health
        self.data["healthmax"] = healthmax
        
        return self

    def defaultSpawnTime(self, spawnTime):
        self.spawnTime = spawnTime
        
    def bloodType(self, color="blood"):
        self.blood = getattr(game.enum, 'FLUID_'+color.upper())

    def setOutfit(self, lookhead, lookbody, looklegs, lookfeet):
        self.data["lookhead"] = lookhead
        self.data["lookbody"] = lookbody
        self.data["looklegs"] = looklegs
        self.data["lookfeet"] = lookfeet

    def setAddons(self, addon):
        self.data["lookaddons"] = addon
        
    def setDefense(self, armor=0, fire=1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1, drown=1):
        self.armor = armor
        self.fire = fire
        self.earth = earth
        self.energy = energy
        self.ice = ice
        self.holy = holy
        self.death = death
        self.drown = drown
        self.physical = physical

    def setTargetChance(self, chance=10):
        self.targetChance = chance
    
    def setSummon(self, monster=None, chance=10, max=1):
        self.summons.append([monster, chance, max]) 
        
    def setExperience(self, experience):
        self.experience = experience
        
    def setSpeed(self, speed):
        self.speed = speed
        
    def setBehavior(self, summonable=0, attackable=1, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0):
        self.summonable = summonable
        self.attackable = attackable
        self.hostile = hostile
        self.illusionable = illusionable
        self.convinceable = convinceable
        self.pushable = pushable
        self.pushItems = pushItems
        self.pushCreaturse = pushCreatures
        self.targetDistance = targetDistance
        self.runOnHealth = runOnHealth
        
    def walkAround(self, energy=0, fire=0, poison=0):
        self.ignoreEnergy = energy
        self.ignoreFire = fire
        self.ignorePoison = poison
        
    def setImmunity(self, paralyze=1, invisible=1, lifedrain=1, drunk=1):
        self.paralyze = paralyze
        self.invisible = invisible
        self.lifedrain = lifedrain
        self.drunk = drunk

    def setWalkable(self, state):
        self.walkable = state

    def setRandomWalkInterval(self, per):
        self.walkPer = per

    def setBrainFeatures(self, *argc):
        self.brainFeatures = argc
        
    def voices(self, *argc):
        self.voiceslist = tuple(argc)

    def regMelee(self, maxDamage, check=lambda x: True, interval=config.meleeAttackSpeed):
        self.meleeAttacks.append([interval, check, maxDamage])
        
    def regTargetSpell(self, spellName, min, max, interval=1, check=chance(10), range=1):
        self.spellAttacks.append([interval, spellName, check, range, (min, max)])
        
    def regSelfSpell(self, spellName, min, max, interval=1, check=chance(10)):
        self.defenceSpells.append([interval, spellName, check, (min, max)])
        
    def regBoost(self, ability, chance, change, duration):
        pass # TODO
        
    def loot(self, *argc):
        # Convert name to Id here
        for loot in argc:
            if type(loot[0]) != int:
                loot = list(loot)
                loot[0] = game.item.itemNames[loot[0]]
    
            self.lootTable.append(loot)
        
class MonsterBrain(object):
    def beginThink(self, monster, isOk=False):
        monster.noBrain = False
        self.handleThink(monster)
        if monster.base.voiceslist:
            self.handleTalk(monster)
                
    @game.engine.loopInThread(0.5)
    def handleThink(self, monster, check=True):
        monster.noBrain = False
        # Are we alive?
        if not monster.alive:
            monster.noBrain = True
            return False # Stop looper
            
        for feature in monster.base.brainFeatures:
            if feature in brainFeatures[0]:
                ret = brainFeatures[0][feature](self, monster)
                
                if ret in (True, False):
                    return ret

        for feature in monster.base.brainFeatures:
            if feature in brainFeatures[1]:
                ret = brainFeatures[1][feature](self, monster)

                if ret in (True, False):
                    return ret
                    
        # Are anyone watching?
        if check and not game.engine.getSpectators(monster.position, (11, 9), cache=False):
            monster.noBrain = True
            return False
            
        if monster.base.walkable and not monster.action and not monster.target and time.time() - monster.lastStep > monster.walkPer: # If no other action is available
            self.walkRandomStep(monster) # Walk a random step
            
    @game.engine.loopInThread(2)        
    def handleTalk(self, monster):
        # Are we alive?
        if not monster.alive:
            return False # Stop looper
            
        if 10 > random.randint(0, 100): # 10%
            # Find a random text
            text = random.choice(monster.base.voiceslist)
            
            # If text is uppercase, then yell it.
            if text.isupper():
                monster.yell(text)
            else:
                monster.say(text)
                
    def walkRandomStep(self, monster, badDir=None):
        # Ignore autowalking when there is noone in range
        spectators = game.engine.getSpectatorList(monster.position, cache=False)
        if not spectators:
            return False
        
        # How far are we (x,y) from our spawn point?
        xFrom = monster.position[0]-monster.spawnPosition[0]
        yFrom = monster.position[1]-monster.spawnPosition[1]
        
        steps = [0,1,2,3]
        if badDir == None:
            badDir = []
        
        random.shuffle(steps)
        
        for step in steps:
            # Prevent checks in "bad" directions
            if step in badDir:
                continue
            
            # Prevent us from autowalking futher then 5 steps
            if step == 0 and monster.radiusTo[1]-(monster.position[1]-1) > monster.radius:
                continue
                
            elif step == 1 and (monster.position[0]+1)-monster.radiusTo[0] > monster.radius:
                continue
                
            elif step == 2 and (monster.position[1]+1)-monster.radiusTo[1] > monster.radius:
                continue
                
            elif step == 3 and monster.radiusTo[0]-(monster.position[0]-1) > monster.radius:
                continue
                
            badDir.append(step)
            def success(result):
                monster.lastStep = time.time()
            
            def errback(result):
                if config.monsterNeverSkipWalks:
                    self.walkRandomStep(monster, badDir)
            
            d = monster.move(step, spectators)
            d.addCallback(success)
            
            d.addErrback(errback)
            return True
        return False
        
brains = {}
brains["default"] = MonsterBrain()
def genMonster(name, look, description="", brain="default"):
    # First build the common creature data
    data = {"lookhead":0, "lookfeet":0, "lookbody":0, "looklegs":0, "lookaddons":0}

    data["looktype"] = look[0]
    data["corpse"] = look[1]
    data["name"] = name
    data["description"] = description or "a %s." % name
    # Then monster only data
    monsters[name] = MonsterBase(data, brains[brain])

    return monsters[name]

def getMonster(name):
    if name in monsters:
        return monsters[name]
    else:
        return None
        
def regBrainFeature(name, function, priority=1):
    if not name in brainFeatures[priority]:
        brainFeatures[priority][name] = function
    else:
        print "Warning, brain feature %s exists!" % name