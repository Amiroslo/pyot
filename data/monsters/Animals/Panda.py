import game.monster

Panda = game.monster.genMonster("Panda", (123, 6049), "a panda")
Panda.setTargetChance(10)
Panda.bloodType("blood")
Panda.setHealth(80)
Panda.setExperience(23)
Panda.setSpeed(200) #incorrect
Panda.walkAround(1,1,0) # energy, fire, poison
Panda.setBehavior(summonable=300, attackable=1, hostile=1, illusionable=300, convinceable=300, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=10)
Panda.voices("Groar", "Grrrrr")
Panda.setImmunity(0,0,0) # paralyze, invisible, lifedrain
Panda.setDefense(10, fire=1.1, earth=0, energy=1.0, ice=1.0, holy=1.0, death=1.0, physical=1.0, drown=1.0)
Panda.loot( ('meat', 17.25, 4), ('ham', 17.5, 2), ('bamboo stick', 1.75) )