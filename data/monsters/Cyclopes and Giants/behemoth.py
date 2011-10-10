behemoth = game.monster.genMonster("Behemoth", (55, 5999), "a behemoth")
behemoth.setHealth(4000)
behemoth.bloodType(color="blood")
behemoth.setDefense(armor=30, fire=0.7, earth=0.2, energy=0.9, ice=1.1, holy=0.7, death=1.05, physical=0.9, drown=1)
behemoth.setExperience(2500)
behemoth.setSpeed(280)
behemoth.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
behemoth.walkAround(energy=1, fire=0, poison=0)
behemoth.setImmunity(paralyze=1, invisible=1, lifedrain=0, drunk=1)
behemoth.voices("Crush the intruders!", "You're so little!", "Human flesh - delicious!")
behemoth.regMelee(455)