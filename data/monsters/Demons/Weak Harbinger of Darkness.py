#largely unknown
weak_harbinger_of_darkness = game.monster.genMonster("Weak Harbinger ofDarkness", (244, 6336), "a weak harbinger of darkness")
weak_harbinger_of_darkness.setHealth(10000)
weak_harbinger_of_darkness.bloodType(color="blood")
weak_harbinger_of_darkness.setDefense(armor=1, fire=1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
weak_harbinger_of_darkness.setExperience(0)
weak_harbinger_of_darkness.setSpeed(400)
weak_harbinger_of_darkness.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
weak_harbinger_of_darkness.walkAround(energy=0, fire=0, poison=0)
weak_harbinger_of_darkness.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
weak_harbinger_of_darkness.regMelee(4100)
weak_harbinger_of_darkness.loot( ('small diamond', 51.75, 3), ('small emerald', 66.75, 5), ('gold ingot', 33.25), ('small ruby', 100, 5), ('platinum coin', 100, 32), ('small amethyst', 22.25), (2148, 100, 183), ('midnight shard', 100.0), ('small sapphire', 18.5, 3) )