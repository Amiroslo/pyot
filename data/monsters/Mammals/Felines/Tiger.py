Tiger = genMonster("Tiger", (125, 6051), "a tiger")
Tiger.setTargetChance(10)
Tiger.type("blood")
Tiger.health(75)
Tiger.experience(40)
Tiger.speed(200) #correct
Tiger.walkAround(1,1,1) # energy, fire, poison
Tiger.behavior(summonable=420, hostile=1, illusionable=1, convinceable=420, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Tiger.immunity(0,0,0) # paralyze, invisible, lifedrain
Tiger.defense(4, fire=1.0, earth=1.0, energy=1.0, ice=1.0, holy=1.0, death=1.05, physical=1.0, drown=1.0)
Tiger.regMelee(40)
Tiger.loot( ("meat", 33.5, 3), ("striped fur", 10.75) )
Tiger.regMelee(40)