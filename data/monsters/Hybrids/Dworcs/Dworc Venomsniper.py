dworc_venomsniper = genMonster("Dworc Venomsniper", (216, 6059), "a dworc venomsniper")
dworc_venomsniper.health(80, healthmax=80)
dworc_venomsniper.type("blood")
dworc_venomsniper.defense(armor=2, fire=1.13, earth=0, energy=1, ice=1.13, holy=0.85, death=1.08, physical=1, drown=1)
dworc_venomsniper.experience(35)
dworc_venomsniper.speed(240)
dworc_venomsniper.behavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=1, pushItems=0, pushCreatures=0, targetDistance=4, runOnHealth=15)
dworc_venomsniper.walkAround(energy=1, fire=1, poison=0)
dworc_venomsniper.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
dworc_venomsniper.voices("Grow truk grrrrr.", "Brak brrretz!", "Prek tars, dekklep zurk.")
dworc_venomsniper.regMelee(15)
dworc_venomsniper.loot( (2148, 100, 13), ("leather armor", 9.5), ("throwing knife", 13.0, 2), ("poison arrow", 9.25, 3), ("skull", 1.5, 2), ("tribal mask", 0.5), ("torch", 5.25), ("poison dagger", 1.75), ("bast skirt", 0.0025), ("seeds", 0.25), ("bronze amulet", 0.0025) )