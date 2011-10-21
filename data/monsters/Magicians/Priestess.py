
priestess = game.monster.genMonster("Priestess", (58, 6081), "a priestess")
priestess.setHealth(390)
priestess.bloodType(color="blood")
priestess.setDefense(armor=20, fire=0.6, earth=0.3, energy=1, ice=1, holy=1.1, death=0.9, physical=1.1, drown=1)
priestess.setExperience(420)
priestess.setSpeed(220)
priestess.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=0)
priestess.walkAround(energy=1, fire=1, poison=1)
priestess.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
priestess.summon("ghoul", 10)
priestess.maxSummons(2)
priestess.voices("Your energy is mine.", "Now your life is come to the end, hahahaha!", "Throw the soul on the altar!")
priestess.regMelee(75)
priestess.loot( ('goat grass', 12.0), ('book', 3.75), ('sling herb', 13.75), ('crystal ball', 1.25), ('clerical mace', 1.5), ('dark rosary', 9.5), ('black hood', 5.0), ('powder herb', 5.75), ('talon', 1.0), ('crystal necklace', 0.75), ('red apple', 11.0, 2), ('mana potion', 1.0), ('wood mushroom', 3.5), ('wooden flute', 1.25), ('hailstorm rod', 0.75), ('piggy bank', 0.0025), ('black shield', 0.25), ('cultish robe', 1.25) )