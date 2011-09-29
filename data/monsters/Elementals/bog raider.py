bog_raider = game.monster.genMonster("Bog Raider", (299, 8951), "a bog raider")
bog_raider.setHealth(1300, healthmax=1300)
bog_raider.bloodType(color="blood")
bog_raider.setDefense(armor=10, fire=0.15, earth=0.7, energy=1.1, ice=1.05, holy=1.05, death=0.95, physical=1.05, drown=1)
bog_raider.setExperience(800)
bog_raider.setSpeed(300)
bog_raider.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
bog_raider.walkAround(energy=1, fire=1, poison=1)
bog_raider.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
bog_raider.voices("Tchhh!", "Slurp!")
bog_raider.regMelee(180) #poisons you 4hp/turn