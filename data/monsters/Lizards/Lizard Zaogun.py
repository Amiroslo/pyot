lizard_zaogun = game.monster.genMonster("Lizard Zaogun", (343, 11284), "a lizard zaogun")
lizard_zaogun.setHealth(2955)
lizard_zaogun.bloodType(color="blood")
lizard_zaogun.setDefense(armor=35, fire=0.55, earth=0, energy=0.8, ice=0.85, holy=1, death=0.9, physical=0.5, drown=1)
lizard_zaogun.setExperience(1700)
lizard_zaogun.setSpeed(420)
lizard_zaogun.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=150)
lizard_zaogun.walkAround(energy=0, fire=0, poison=0)
lizard_zaogun.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
lizard_zaogun.voices("Hissss!", "Cowardzz!", "Softzzkinzz from zze zzouzz!", "Zztand and fight!")
lizard_zaogun.regMelee(350)
lizard_zaogun.loot( ('great health potion', 13.5, 3), ('zaoan shoes', 1.0), ('zaogun flag', 6.0), ('small emerald', 7.75, 5), ('zaogun shoulderplates', 11.5), (2148, 100, 289), ('lizard scale', 7.0, 3), ('red lantern', 2.0), ('platinum coin', 7.25, 2), ('lizard leather', 1.0), ('strong health potion', 2.0), ('tower shield', 1.0), ('zaoan legs', 0.5), ('zaoan armor', 0.5) )