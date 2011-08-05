import game.monster

Mammoth = game.monster.genMonster("Mammoth", (199, 6074), "a Mammoth")
Mammoth.setTargetChance(10)
Mammoth.bloodType("blood")
Mammoth.setHealth(320)
Mammoth.setExperience(160)
Mammoth.setSpeed(190) #correct
Mammoth.walkAround(1,1,1) # energy, fire, poison
Mammoth.setBehavior(summonable=0, attackable=1, hostile=1, illusionable=0, convinceable=500, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Mammoth.voices("Troooooot!", "Hooooot-Toooooot!", "Tooooot.")
Mammoth.setImmunity(0,0,0) # paralyze, invisible, lifedrain
Mammoth.setDefense(20, fire=1.1, earth=0.8, energy=1.0, ice=0.8, holy=1.0, death=1.0, physical=0.8, drown=1.0)
