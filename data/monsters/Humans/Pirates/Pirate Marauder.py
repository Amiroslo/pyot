pirate_marauder = genMonster("Pirate Marauder ", (93, 6080), "a pirate marauder ")
pirate_marauder.health(210)
pirate_marauder.type("blood")
pirate_marauder.defense(armor=9, fire=1.1, earth=0.9, energy=1.03, ice=1, holy=0.8, death=1.05, physical=1, drown=1)
pirate_marauder.experience(125)
pirate_marauder.speed(230)
pirate_marauder.behavior(summonable=0, hostile=2, illusionable=1, convinceable=490, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=20, targetChange=0)
pirate_marauder.walkAround(energy=1, fire=1, poison=1)
pirate_marauder.immunity(paralyze=1, invisible=0, lifedrain=1, drunk=1)
pirate_marauder.voices("Plundeeeeer!", "Hiyaa!", "Give up!")
pirate_marauder.regMelee(140)
pirate_marauder.regDistance(40, ANIMATION_SPEAR, chance(21))
pirate_marauder.loot( (2148, 100, 40), ("pirate bag", 0.5), ("torch", 10.0), ("chain armor", 3.0), ("compass", 10.25), ("hook", 0.5, 3), ("spear", 7.25, 2), ("treasure map", 1.0), ("peg leg", 0.5), ("plate shield", 5.0), ("bandana", 1.0), ("rum flask", 0.0025), ("eye patch", 0.5), ("goldfish bowl", 0.25), ("dice", 0.0025) )