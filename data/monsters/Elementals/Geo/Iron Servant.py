iron_servant = genMonster("Iron Servant", (395, 5980), "an iron servant")
iron_servant.setHealth(350, healthmax=350)
iron_servant.bloodType(color="blood")
iron_servant.setDefense(armor=17, fire=0.75, earth=1.1, energy=0.75, ice=1, holy=0.8, death=1.1, physical=1, drown=1)
iron_servant.setExperience(210)
iron_servant.setSpeed(250)
iron_servant.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
iron_servant.walkAround(energy=0, fire=1, poison=0)
iron_servant.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
iron_servant.voices("Error. LOAD 'PROGRAM',8,1", "Remain. Obedient.")
iron_servant.regMelee(45)
iron_servant.loot( (2148, 100, 51), ("health potion", 3.0), ("halberd", 0.5), ("gear wheel", 4.0), ("rusty armor", 0.75) )