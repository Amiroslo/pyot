tarantula = genMonster("Tarantula", 219, 5995)
tarantula.health(225)
tarantula.type("slime")
tarantula.defense(armor=22, fire=1.15, earth=0, energy=0.9, ice=1.1, holy=1, death=1, physical=1, drown=1)
tarantula.experience(120)
tarantula.speed(280)
tarantula.behavior(summonable=485, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=False, targetDistance=1, runOnHealth=0)
tarantula.walkAround(energy=1, fire=1, poison=0)
tarantula.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
tarantula.loot( (2148, 100, 34), ("tarantula egg", 14.75), ("plate shield", 2.0), (8859, 7.25), ("brass legs", 4.25) )

tarantula.melee(90, condition=CountdownCondition(CONDITION_POISON, 2), conditionChance=100)