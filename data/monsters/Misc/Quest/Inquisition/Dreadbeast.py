dreadbeast = genMonster("Dreadbeast", (101, 6030), "a dreadbeast")
dreadbeast.setHealth(795)
dreadbeast.bloodType(color="undead")
dreadbeast.setDefense(armor=2, fire=0.45, earth=0, energy=0.85, ice=0.65, holy=1.5, death=0, physical=0.7, drown=0.25)
dreadbeast.setExperience(250)
dreadbeast.setSpeed(210)
dreadbeast.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=800, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
dreadbeast.walkAround(energy=0, fire=0, poison=0)
dreadbeast.setImmunity(paralyze=1, invisible=0, lifedrain=0, drunk=0)
dreadbeast.regMelee(50)#+poison
dreadbeast.loot( ("bone", 8.5), (2148, 100, 90), ("skull", 1.0), ("hardened bone", 0.25, 3), ("big bone", 1.75), ("health potion", 0.25), ("plate armor", 1.75), ("bone club", 1.25), ("bone shield", 0.25), ("green mushroom", 0.25) )