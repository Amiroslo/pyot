import game.monster

Tortoise = game.monster.genMonster("Tortoise", (197, 6072), "a tortoise")
Tortoise.setTargetChance(0)
Tortoise.bloodType("blood")
Tortoise.setHealth(185)
Tortoise.setExperience(90)
Tortoise.setSpeed(130) #correct
Tortoise.walkAround(1,1,1) # energy, fire, poison
Tortoise.setBehavior(summonable=0, attackable=1, hostile=1, illusionable=445, convinceable=445, pushable=0, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
Tortoise.setImmunity(0,0,0) # paralyze, invisible, lifedrain
Tortoise.setDefense(25, fire=1.1, earth=0.8, energy=1.0, ice=0.8, holy=1.0, death=1.0, physical=0.8, drown=1.0)
