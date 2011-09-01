LIGHTLEVEL_NONE = 0
LIGHTLEVEL_TORCH = 7
LIGHTLEVEL_FULL = 27
LIGHTLEVEL_WORLD = 255

LIGHTCOLOR_NONE = 0
LIGHTCOLOR_DEFAULT = 206 # Orange
LIGHTCOLOR_WHITE = 215

SLOT_WHEREEVER = 0
SLOT_FIRST = 1
SLOT_HEAD = SLOT_FIRST
SLOT_NECKLACE = 2
SLOT_BACKPACK = 3
SLOT_ARMOR = 4
SLOT_RIGHT = 5
SLOT_LEFT = 6
SLOT_LEGS = 7
SLOT_FEET = 8
SLOT_RING = 9
SLOT_AMMO = 10
SLOT_DEPOT = 11
SLOT_LAST = SLOT_DEPOT
SLOT_HAND = 12
SLOT_TWO_HAND = 12

# Skills
SKILL_FIRST = 0
SKILL_FIST = SKILL_FIRST
SKILL_CLUB = 1
SKILL_SWORD = 2
SKILL_AXE = 3
SKILL_DIST = 4
SKILL_SHIELD = 5
SKILL_FISH = 6
SKILL_LAST = SKILL_FISH

# Chat
MSG_NONE			= 0x00
MSG_SPEAK_SAY			= 0x01
MSG_SPEAK_WHISPER		= 0x02
MSG_SPEAK_YELL			= 0x03
MSG_PRIVATE_FROM		= 0x04
MSG_PRIVATE_TO			= 0x05
MSG_CHANNEL_MANAGEMENT		= 0x06
MSG_CHANNEL			= 0x07
MSG_CHANNEL_HIGHLIGHT		= 0x08
MSG_SPEAK_SPELL			= 0x09
MSG_NPC_FROM			= 0x0A
MSG_NPC_TO			= 0x0B
MSG_GAMEMASTER_BROADCAST	= 0x0C
MSG_GAMEMASTER_CHANNEL		= 0x0D
MSG_GAMEMASTER_PRIVATE_FROM	= 0x0E
MSG_GAMEMASTER_PRIVATE_TO	= 0x0F
MSG_SPEAK_MONSTER_SAY		= 0x22
MSG_SPEAK_MONSTER_YELL		= 0x23
MSG_SPEAK_FIRST			= MSG_SPEAK_SAY
MSG_SPEAK_LAST			= MSG_GAMEMASTER_PRIVATE_FROM
MSG_SPEAK_MONSTER_FIRST		= MSG_SPEAK_MONSTER_SAY
MSG_SPEAK_MONSTER_LAST		= MSG_SPEAK_MONSTER_YELL
MSG_STATUS_CONSOLE_RED		= 0x0C # Red message in the console
MSG_STATUS_DEFAULT		= 0x10 # White message at the bottom of the game window and in the console
MSG_STATUS_WARNING		= 0x11 # Red message in game window and in the console
MSG_EVENT_ADVANCE		= 0x12 # White message in game window and in the console
MSG_STATUS_SMALL		= 0x13 # White message at the bottom of the game window"
MSG_INFO_DESCR			= 0x14 # Green message in game window and in the console
MSG_DAMAGE_DEALT		= 0x15
MSG_DAMAGE_RECEIVED		= 0x16
MSG_HEALED			= 0x17
MSG_EXPERIENCE			= 0x18
MSG_DAMAGE_OTHERS		= 0x19
MSG_HEALED_OTHERS		= 0x1A
MSG_EXPERIENCE_OTHERS		= 0x1B
MSG_EVENT_DEFAULT		= 0x1C # White message at the bottom of the game window and in the console
MSG_LOOT			= 0x1D
MSG_TRADE_NPC			= 0x1E
MSG_CHANNEL_GUILD		= 0x1F # SPEAK_CHANNEL_W(?) guild messages.
MSG_PARTY_MANAGEMENT		= 0x20
MSG_PARTY			= 0x21
MSG_EVENT_ORANGE		= 0x22 # Orange message in the console
MSG_STATUS_CONSOLE_ORANGE	= 0x23 # Orange message in the console
MSG_REPORT 			= 0x24
MSG_HOTKEY_USE			= 0x25
MSG_TUTORIAL_HINT		= 0x26
MSG_STATUS_CONSOLE_BLUE		= 0xFF

# Colors
COLOR_BLACK                     = 0
COLOR_BLUE                      = 5
COLOR_GREEN                     = 18
COLOR_LIGHTGREEN                = 66
COLOR_DARKBROWN                 = 78
COLOR_LIGHTBLUE                 = 89
COLOR_MAYABLUE                  = 95
COLOR_DARKRED                   = 108
COLOR_DARKPURPLE                = 112
COLOR_BROWN                     = 120
COLOR_GREY                      = 129
COLOR_TEAL                      = 143
COLOR_DARKPINK                  = 152
COLOR_PURPLE                    = 154
COLOR_DARKORANGE                = 156
COLOR_RED                       = 180
COLOR_PINK                      = 190
COLOR_ORANGE                    = 192
COLOR_DARKYELLOW                = 205
COLOR_YELLOW                    = 210
COLOR_WHITE                     = 215

# Fluids
FLUID_EMPTY                     = 0x00
FLUID_BLUE                      = 0x01
FLUID_PURPLE                    = 0x02
FLUID_BROWN                     = 0x03
FLUID_RED                       = 0x05
FLUID_GREEN                     = 0x06
FLUID_YELLOW                    = 0x08
FLUID_WHITE                     = 0x09

FLUID_NONE                      = FLUID_EMPTY
FLUID_WATER                     = FLUID_BLUE
FLUID_BLOOD                     = FLUID_RED
FLUID_BEER                      = FLUID_BROWN
FLUID_SLIME                     = FLUID_GREEN
FLUID_LEMONADE                  = FLUID_YELLOW
FLUID_MILK                      = FLUID_WHITE
FLUID_MANA                      = FLUID_PURPLE

FLUID_LIFE                      = FLUID_RED + 8
FLUID_OIL                       = FLUID_BROWN + 8
FLUID_URINE                     = FLUID_YELLOW + 8
FLUID_COCONUTMILK               = FLUID_WHITE + 8
FLUID_WINE                      = FLUID_PURPLE + 8

FLUID_MUD                       = FLUID_BROWN + 16
FLUID_FRUITJUICE                = FLUID_YELLOW + 16

FLUID_LAVA                      = FLUID_RED + 24
FLUID_RUM                       = FLUID_BROWN + 24
FLUID_SWAMP                     = FLUID_GREEN + 24

FLUID_TEA                       = FLUID_BROWN + 32
FLUID_MEAD                      = FLUID_BROWN + 40

# Compatibility stuff
FLUID_ENERGY                    = FLUID_PURPLE
FLUID_UNDEAD                    = FLUID_NONE
FLUID_FIRE                      = FLUID_BROWN

# Floorchange
FLOORCHANGE_DOWN                = 0x00
FLOORCHANGE_UP                  = 0x01


# Directions
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
SOUTHWEST = 4
SOUTHEAST = 5
NORTHWEST = 6
NORTHEAST = 7

# Splashes
SMALLSPLASH = 2019
FULLSPLASH = 2016

# Damage types
PHYSICAL = 0
FIRE = 1
EARTH = 2
ENERGY = 3
ICE = 4
HOLY = 5
DEATH = 6
DROWN = 7
MELEE = 8

# Monster attack types
MELEE = 0
TARGET_SPELL = 1
SELF_SPELL = 2

# TargetTypes
TARGET_DIRECTION = 0
TARGET_CASTER_AREA = 1
TARGET_TARGET_AREA = 2

# Magic effects
EFFECT_DRAWBLOOD = 1
EFFECT_LOSEENERGY = 2
EFFECT_POFF = 3
EFFECT_BLOCKHIT = 4
EFFECT_EXPLOSIONAREA = 5
EFFECT_EXPLOSIONHIT = 6
EFFECT_FIREAREA = 7
EFFECT_YELLOW_RINGS = 8
EFFECT_GREEN_RINGS = 9
EFFECT_HITAREA = 10
EFFECT_TELEPORT = 11
EFFECT_ENERGYHIT = 12
EFFECT_MAGIC_BLUE = 13
EFFECT_MAGIC_RED = 14
EFFECT_MAGIC_GREEN = 15
EFFECT_HITBYFIRE = 16
EFFECT_HITBYPOISON = 17
EFFECT_MORTAREA = 18
EFFECT_SOUND_GREEN = 19
EFFECT_SOUND_RED = 20
EFFECT_POISONAREA = 21
EFFECT_SOUND_YELLOW = 22
EFFECT_SOUND_PURPLE = 23
EFFECT_SOUND_BLUE = 24
EFFECT_SOUND_WHITE = 25
EFFECT_BUBBLES = 26
EFFECT_CRAPS = 27
EFFECT_GIFT_WRAPS = 28
EFFECT_FIREWORK_YELLOW = 29
EFFECT_FIREWORK_RED = 30
EFFECT_FIREWORK_BLUE = 31
EFFECT_STUN = 32
EFFECT_SLEEP = 33
EFFECT_WATERCREATURE = 34
EFFECT_GROUNDSHAKER = 35
EFFECT_HEARTS = 36
EFFECT_FIREATTACK = 37
EFFECT_ENERGYAREA = 38
EFFECT_SMALLCLOUDS = 39
EFFECT_HOLYDAMAGE = 40
EFFECT_BIGCLOUDS = 41
EFFECT_ICEAREA = 42
EFFECT_ICETORNADO = 43
EFFECT_ICEATTACK = 44
EFFECT_STONES = 45
EFFECT_SMALLPLANTS = 46
EFFECT_CARNIPHILA = 47
EFFECT_PURPLEENERGY = 48
EFFECT_YELLOWENERGY = 49
EFFECT_HOLYAREA = 50
EFFECT_BIGPLANTS = 51
EFFECT_CAKE = 52
EFFECT_GIANTICE = 53
EFFECT_WATERSPLASH = 54
EFFECT_PLANTATTACK = 55
EFFECT_TUTORIALARROW = 56
EFFECT_TUTORIALSQUARE = 57
EFFECT_MIRRORHORIZONTAL = 58
EFFECT_MIRRORVERTICAL = 59
EFFECT_SKULLHORIZONTAL = 60
EFFECT_SKULLVERTICAL = 61
EFFECT_ASSASSIN = 62
EFFECT_STEPSHORIZONTAL = 63
EFFECT_BLOODYSTEPS = 64
EFFECT_STEPSVERTICAL = 65
EFFECT_YALAHARIGHOST = 66
EFFECT_BATS = 67
EFFECT_SMOKE = 68
EFFECT_INSECTS = 69
EFFECT_DRAGONHEAD = 70
EFFECT_ORCSHAMAN = 71
EFFECT_ORCSHAMAN_FIRE = 72
EFFECT_NONE = 0

# Animation
ANIMATION_SPEAR = 0
ANIMATION_BOLT = 1
ANIMATION_ARROW = 2
ANIMATION_FIRE = 3
ANIMATION_ENERGY = 4
ANIMATION_POISONARROW = 5
ANIMATION_BURSTARROW = 6
ANIMATION_THROWINGSTAR = 7
ANIMATION_THROWINGKNIFE = 8
ANIMATION_SMALLSTONE = 9
ANIMATION_DEATH = 10
ANIMATION_LARGEROCK = 11
ANIMATION_SNOWBALL = 12
ANIMATION_POWERBOLT = 13
ANIMATION_POISON = 14
ANIMATION_INFERNALBOLT = 15
ANIMATION_HUNTINGSPEAR = 16
ANIMATION_ENCHANTEDSPEAR = 17
ANIMATION_ASSASSINSTAR = 18
ANIMATION_GREENSTAR = 19
ANIMATION_ROYALSPEAR = 20
ANIMATION_SNIPERARROW = 21
ANIMATION_ONYXARROW = 22
ANIMATION_PIERCINGBOLT = 23
ANIMATION_WHIRLWINDSWORD = 24
ANIMATION_WHIRLWINDAXE = 25
ANIMATION_WHIRLWINDCLUB = 26
ANIMATION_ETHEREALSPEAR = 27
ANIMATION_ICE = 28
ANIMATION_EARTH = 29
ANIMATION_HOLY = 30
ANIMATION_SUDDENDEATH = 31
ANIMATION_FLASHARROW = 32
ANIMATION_FLAMMINGARROW = 33
ANIMATION_SHIVERARROW = 34
ANIMATION_ENERGYBALL = 35
ANIMATION_SMALLICE = 36
ANIMATION_SMALLHOLY = 37
ANIMATION_SMALLEARTH = 38
ANIMATION_EARTHARROW = 39
ANIMATION_EXPLOSION = 40
ANIMATION_CAKE = 41
ANIMATION_WEAPONTYPE = 254
ANIMATION_NONE = 255

# Item types
ITEM_TYPE_NONE        = 0
ITEM_TYPE_DEPOT       = 1
ITEM_TYPE_MAILBOX     = 2
ITEM_TYPE_TRASHHOLDER = 3
ITEM_TYPE_CONTAINER   = 4
ITEM_TYPE_DOOR        = 5
ITEM_TYPE_MAGICFIELD  = 6
ITEM_TYPE_TELEPORT    = 7
ITEM_TYPE_BED         = 8

# Modes
OFFENSIVE = 1
BALANCED = 2
DEFENSIVE = 3

STAND = 0
CHASE = 1

SECURE = 1

# Attack strategy
TARGETSTRATEGY_NONE = 0
TARGETSTRATEGY_NORMAL = 1
TARGETSTRATEGY_LOWEST = 2
TARGETSTRATEGY_HIGHEST = 3

# Money map, id => value. Have to be ordered from highest to lowest, otherwise it will be bugs
# TODO Move to money loading
MONEY_MAP = ((2160, 10000), (2152, 100), (2148, 1))

# Mailstuff
ITEM_PARCEL           = 2595
ITEM_PARCEL_STAMPED   = 2596
ITEM_LETTER           = 2597
ITEM_LETTER_STAMPED   = 2598
ITEM_LABEL            = 2599
