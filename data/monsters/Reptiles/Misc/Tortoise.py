Tortoise = genMonster("Tortoise", (197, 6072), "a tortoise")
Tortoise.setTargetChance(0)
Tortoise.type("blood")
Tortoise.health(185)
Tortoise.experience(90)
Tortoise.speed(130) #correct
Tortoise.walkAround(1,1,1) # energy, fire, poison
Tortoise.behavior(summonable=0, hostile=1, illusionable=1, convinceable=445, pushable=0, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
Tortoise.immunity(0,0,0) # paralyze, invisible, lifedrain
Tortoise.defense(24, fire=1.1, earth=0.8, energy=1.0, ice=0.8, holy=1.0, death=1.0, physical=0.8, drown=1.0)
Tortoise.loot( (2148, 100, 30), ("tortoise shield", 0.25), ("tortoise egg", 1.25, 2), ("fish", 5.0), ("plate shield", 2.75), ("battle hammer", 1.0), ("turtle shell", 1.0, 3) )
Tortoise.regMelee(50)