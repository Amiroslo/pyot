orc_spearman = genMonster("Orc Spearman", (50, 5996), "an orc spearman")
orc_spearman.setHealth(105)
orc_spearman.bloodType(color="blood")
orc_spearman.setDefense(armor=7, fire=1, earth=1.1, energy=0.8, ice=1, holy=0.8, death=1.1, physical=1, drown=1)
orc_spearman.setExperience(38)
orc_spearman.setSpeed(176)
orc_spearman.setBehavior(summonable=310, hostile=1, illusionable=1, convinceable=310, pushable=1, pushItems=0, pushCreatures=0, targetDistance=4, runOnHealth=10)
orc_spearman.walkAround(energy=1, fire=1, poison=1)
orc_spearman.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
orc_spearman.voices("Ugaar!")
orc_spearman.regMelee(25)
orc_spearman.regDistance(30, ANIMATION_SPEAR, chance(21))
orc_spearman.loot( ("spear", 17.5), (2148, 100, 11), ("studded legs", 9.75), ("meat", 29.25), ("studded helmet", 9.25), ("machete", 2.75), ("orc leather", 2.0), ("orc tooth", 0.25) )