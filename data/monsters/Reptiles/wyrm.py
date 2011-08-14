import game.monster

wyrm = game.monster.genMonster("Wyrm", (291, 8941), "a wyrm")
wyrm.setHealth(1825)
wyrm.bloodType(color="blood")
wyrm.setDefense(armor=30, fire=0.8, earth=0.75, energy=0, ice=1.05, holy=1, death=1.05, physical=1, drown=1)
wyrm.setExperience(1450)
wyrm.setSpeed(300)
wyrm.setBehavior(summonable=0, attackable=1, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=350)
wyrm.walkAround(energy=0, fire=0, poison=0)
wyrm.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
wyrm.voices("GRROARR", "GRRR")