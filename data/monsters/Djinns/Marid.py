marid = game.monster.genMonster("Marid", (104, 6033), "a marid")
marid.setHealth(550, healthmax=550)
marid.bloodType(color="blood")
marid.setDefense(armor=20, fire=0.9, earth=0.9, energy=0.4, ice=1.05, holy=0.8, death=1.08, physical=1, drown=1)
marid.setExperience(325)
marid.setSpeed(170)
marid.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
marid.walkAround(energy=1, fire=1, poison=1)
marid.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
marid.summon("blue djinn", 10)
marid.maxSummons(2)
marid.voices("Wishes can come true", "Feel the power of my magic, tiny mortal!", "Simsalabim", "Djinns will soon again be the greatest!", "Be careful what you wish.")
marid.regMelee(90)
marid.loot( (2148, 100, 128), ("blueberry", 100, 25), (12426, 8.0), ("small sapphire", 6.75), ("hailstorm rod", 1.0), ("strong mana potion", 10.0), ("royal spear", 35.75, 3), ("seeds", 2.5), ("blue tapestry", 2.5), ("heavy machete", 4.5), ("blue piece of cloth", 3.0, 3), ("magma monocle", 0.75), ("wooden flute", 0.25), (12442, 0.5), ("blue gem", 0.25), ("mystic turban", 0.25), ("small oil lamp", 0.0025) )