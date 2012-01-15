hellhound = game.monster.genMonster("Hellhound", (240, 6332), "a hellhound")
hellhound.setHealth(7500, healthmax=7500)
hellhound.bloodType(color="blood")
hellhound.setDefense(armor=68, fire=0, earth=0.8, energy=0.9, ice=1.05, holy=1.05, death=1, physical=1, drown=1)
hellhound.setExperience(6800)
hellhound.setSpeed(310)
hellhound.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
hellhound.walkAround(energy=0, fire=0, poison=0)
hellhound.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
hellhound.voices("GROOOOWL!")
hellhound.regMelee(510)#or more
hellhound.loot( ("concentrated demonic blood", 46.5, 2), ("platinum coin", 100, 5), (2148, 100, 100), ("ham", 30.5), ("demonic essence", 17.75, 3), ("spike sword", 5.5), ("soul orb", 19.0), ("rusty armor", 4.75), ("knight axe", 7.5), ("hellhound slobber", 8.75), ("black pearl", 23.0, 4), ("giant sword", 1.25), ("great mana potion", 6.25), ("gold ingot", 0.5), ("big bone", 0.5), (4873, 0.0025), ("ruthless axe", 0.25) )