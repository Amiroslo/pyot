dworc_fleshhunter = game.monster.genMonster(_("Dworc Fleshhunter"), (215, 6058), _("a dworc fleshhunter"))
dworc_fleshhunter.setHealth(85, healthmax=85)
dworc_fleshhunter.bloodType(color="blood")
dworc_fleshhunter.setDefense(armor=2, fire=1.13, earth=0, energy=1, ice=1.13, holy=1, death=1.08, physical=1, drown=1)
dworc_fleshhunter.setExperience(40)
dworc_fleshhunter.setSpeed(240)
dworc_fleshhunter.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=8)
dworc_fleshhunter.walkAround(energy=1, fire=1, poison=0)
dworc_fleshhunter.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
dworc_fleshhunter.voices("Grow truk grrrrr.", "Brak brrretz!", "Prek tars, dekklep zurk.")
dworc_fleshhunter.regMelee(25)
dworc_fleshhunter.regDistance(15, ANIMATION_THROWINGKNIFE, chance(21))
dworc_fleshhunter.loot( (2148, 100, 13), ("cleaver", 8.5), ("skull", 5.75, 3), ("hunting spear", 2.0), ("torch", 5.5), ("leather armor", 11.0), ("poison dagger", 2.0), ("tribal mask", 0.5), ("bone shield", 1.25), ("ripper lance", 0.0025) )