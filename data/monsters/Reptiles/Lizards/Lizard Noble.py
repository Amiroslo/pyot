#unknown
lizard_noble = genMonster("Lizard Noble", 115, 6041)
lizard_noble.health(5740, healthmax=5740)
lizard_noble.type("blood")
lizard_noble.defense(armor=29, fire=0.15, earth=0, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
lizard_noble.experience(2000)
lizard_noble.speed(210)
lizard_noble.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=4, runOnHealth=0)
lizard_noble.walkAround(energy=0, fire=0, poison=0)
lizard_noble.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
lizard_noble.voices("Where are zhe guardz when you need zhem!")
lizard_noble.melee(80)
#lizard_noble.loot()