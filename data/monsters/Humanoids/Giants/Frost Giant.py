frost_giant = genMonster("Frost Giant", 257, 7330)
frost_giant.health(270)
frost_giant.type("blood")
frost_giant.defense(armor=24, fire=1, earth=1, energy=1, ice=0, holy=1, death=1, physical=1, drown=1)
frost_giant.experience(150)
frost_giant.speed(195)
frost_giant.behavior(summonable=0, hostile=True, illusionable=True, convinceable=490, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
frost_giant.walkAround(energy=1, fire=1, poison=1)
frost_giant.immunity(paralyze=1, invisible=0, lifedrain=0, drunk=1)
frost_giant.voices("Hmm Humansoup!", "Stand still ya tasy snack!", "Joh Thun!", "Horre Sjan Flan!", "Brore Smode!", "Forle Bramma")
frost_giant.melee(110)
frost_giant.distance(80, ANIMATION_LARGEROCK, chance(21))
frost_giant.loot( (2148, 100, 40), ("short sword", 8.75), ("meat", 4.75, 2), ("shard", 0.0025), ("frost giant pelt", 5.25), ("ice cube", 2.0), ("dark helmet", 0.25), ("health potion", 0.75), ("battle shield", 1.75), ("halberd", 0.75), ("club ring", 0.0025), ("norse shield", 0.25) )