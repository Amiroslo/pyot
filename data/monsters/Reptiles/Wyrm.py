
wyrm = game.monster.genMonster("Wyrm", (291, 8941), "a wyrm")
wyrm.setHealth(1825)
wyrm.bloodType(color="blood")
wyrm.setDefense(armor=30, fire=0.8, earth=0.75, energy=0, ice=1.05, holy=1, death=1.05, physical=1, drown=1)
wyrm.setExperience(1450)
wyrm.setSpeed(300)
wyrm.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=350)
wyrm.walkAround(energy=0, fire=0, poison=0)
wyrm.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
wyrm.voices("GRROARR", "GRRR")
wyrm.regMelee(235)
wyrm.loot( (2148, 100, 232), ('dragon ham', 35.0, 3), ('strong health potion', 20.25), ('wyrm scale', 14.75), ('burst arrow', 43.5, 10), ('strong mana potion', 15.25), ('crossbow', 6.0), ('hibiscus dress', 0.25), ('focus cape', 1.25), ('wand of draconia', 0.75), ('wand of starstorm', 0.5), ('lightning pendant', 0.75), ('small diamond', 1.5, 3), ('dragonbone staff', 0.0025), ('shockwave amulet', 0.25), ('composite hornbow', 0.0025) )