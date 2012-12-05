
orc_shaman = genMonster("Orc Shaman", (6, 5978), "an orc shaman")
orc_shaman.setHealth(115)
orc_shaman.bloodType("blood")
orc_shaman.setDefense(armor=8, fire=1, earth=1.1, energy=0.5, ice=1, holy=0.9, death=1.05, physical=1, drown=1)
orc_shaman.setExperience(110)
orc_shaman.setSpeed(180)
orc_shaman.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=0, pushCreatures=0, targetDistance=4, runOnHealth=0)
orc_shaman.walkAround(energy=1, fire=1, poison=1)
orc_shaman.setImmunity(paralyze=0, invisible=1, lifedrain=0, drunk=1)
orc_shaman.summon("snake", 10)
orc_shaman.maxSummons(4)
orc_shaman.voices("Huumans stinkk!", "Grak brrretz gulu.")
orc_shaman.regMelee(15) #incorrect
orc_shaman.loot( ("shamanic hood", 7.0), (2148, 100, 5), ("broken shamanic staff", 9.25), ("orc tooth", 1.5), ("spear", 5.75), ("chain armor", 8.25), ("corncob", 14.5, 2), ("orc leather", 4.5), ("wand of decay", 1.0), ("book", 0.5) )