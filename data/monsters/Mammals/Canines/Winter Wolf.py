Winter_Wolf = genMonster("Winter Wolf", (52, 5997), "a winter wolf")
Winter_Wolf.setTargetChance(0)
Winter_Wolf.type("blood")
Winter_Wolf.health(30)
Winter_Wolf.experience(20)
Winter_Wolf.speed(170) #correct
Winter_Wolf.walkAround(1,1,1) # energy, fire, poison
Winter_Wolf.behavior(summonable=260, hostile=1, illusionable=1, convinceable=260, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
Winter_Wolf.voices("Yooooohhuuuu!")
Winter_Wolf.immunity(0,0,0) # paralyze, invisible, lifedrain
Winter_Wolf.defense(2, fire=1.1, earth=1.0, energy=1.1, ice=0.8, holy=0.9, death=1.1, physical=1.0, drown=1.0)
Winter_Wolf.loot( ("meat", 29.0, 2), ("winter wolf fur", 10.0) )
Winter_Wolf.regMelee(20)