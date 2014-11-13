dwarf_guard = genMonster("Dwarf Guard", (70, 6013), "a dwarf guard")
dwarf_guard.health(245)
dwarf_guard.type("blood")
dwarf_guard.defense(armor=20, fire=1.05, earth=0.8, energy=1, ice=1, holy=1, death=1.05, physical=0.9, drown=1)
dwarf_guard.experience(165)
dwarf_guard.speed(200)
dwarf_guard.behavior(summonable=650, hostile=1, illusionable=1, convinceable=650, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
dwarf_guard.walkAround(energy=1, fire=1, poison=1)
dwarf_guard.immunity(paralyze=1, invisible=0, lifedrain=1, drunk=1)
dwarf_guard.voices("Hail Durin!")
dwarf_guard.regMelee(140)
dwarf_guard.loot( ("battle hammer", 7.5), (2148, 100, 29), ("leather boots", 22.5), ("scale armor", 7.5), ("white mushroom", 82.5, 2), ("battle shield", 7.5) )