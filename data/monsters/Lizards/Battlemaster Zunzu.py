Battlemaster_Zunzu = game.monster.genMonster("Battlemaster Zunzu", (343, 11278), "a battlemaster zunzu")
Battlemaster_Zunzu.setHealth(6000, healthmax=6000)
Battlemaster_Zunzu.bloodType(color="blood")
Battlemaster_Zunzu.setDefense(armor=60, fire=0.75, earth=0, energy=0.8, ice=0.85, holy=1, death=0.9, physical=0.85, drown=1)
Battlemaster_Zunzu.setExperience(2500)
Battlemaster_Zunzu.setSpeed(250)
Battlemaster_Zunzu.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Battlemaster_Zunzu.walkAround(energy=0, fire=0, poison=0)
Battlemaster_Zunzu.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Battlemaster_Zunzu.voices("Hissss!")
Battlemaster_Zunzu.regMelee(300)
Battlemaster_Zunzu.loot( (2148, 100, 166), ("red lantern", 100.0), ("zaogun shoulderplates", 100.0), ("zaoan shoes", 3.25), ("small emerald", 61.25, 10), ("zaogun flag", 11.25), ("strong health potion", 3.0), ("lizard scale", 0.75, 3), ("great health potion", 0.75), ("zaoan legs", 2.5), ("lizard leather", 1.75), ("zaoan armor", 1.0) )