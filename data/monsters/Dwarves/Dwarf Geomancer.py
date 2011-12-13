dwarf_geomancer = game.monster.genMonster("Dwarf Geomancer", (66, 6015), "a dwarf geomancer")
dwarf_geomancer.setHealth(380)
dwarf_geomancer.bloodType(color="blood")
dwarf_geomancer.setDefense(armor=15, fire=0.4, earth=0.8, energy=0.9, ice=1.05, holy=0.9, death=1.1, physical=1, drown=1)
dwarf_geomancer.setExperience(265)
dwarf_geomancer.setSpeed(200)
dwarf_geomancer.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=0, targetDistance=4, runOnHealth=150)
dwarf_geomancer.walkAround(energy=1, fire=0, poison=1)
dwarf_geomancer.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
dwarf_geomancer.voices("Earth is the strongest element.", "Dust to dust.")
dwarf_geomancer.regMelee(100)
dwarf_geomancer.loot( (2148, 100, 45), ("white mushroom", 89.5, 2), ("pear", 25.25), ("blank rune", 34.5), (12414, 7.75), ("dwarven ring", 0.75), (2162, 13.25), (12419, 6.75), ("small sapphire", 0.25), ("spellbook", 0.0025), ("iron ore", 0.5), ("clerical mace", 1.0), ("terra boots", 0.0025) )