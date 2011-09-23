eternal_guardian = game.monster.genMonster("Eternal Guardian", (345, 11278), "an eternal guardian")
eternal_guardian.setHealth(2500)
eternal_guardian.bloodType(color="blood")
eternal_guardian.setDefense(armor=35, fire=0.7, earth=0, energy=0.9, ice=0.9, holy=0.8, death=0.8, physical=1, drown=1)
eternal_guardian.setExperience(1800)
eternal_guardian.setSpeed(420)
eternal_guardian.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
eternal_guardian.walkAround(energy=1, fire=0, poison=0)
eternal_guardian.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
eternal_guardian.regMelee(300)