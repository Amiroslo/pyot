spitter = game.monster.genMonster("Spitter", (461, 15392), "a spitter")
spitter.setHealth(1500)
spitter.bloodType(color="slime")
spitter.setDefense(armor=1, fire=0.95, earth=0, energy=1.05, ice=1.05, holy=1, death=0.95, physical=1, drown=1)
spitter.setExperience(1100)
spitter.setSpeed(300) #incorrect
spitter.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=40)
spitter.walkAround(energy=1, fire=1, poison=0)
spitter.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
spitter.regMelee(150)