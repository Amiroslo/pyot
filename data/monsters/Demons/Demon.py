demon = game.monster.genMonster("Demon", (35, 5995), "a demon")
demon.setHealth(8200)
demon.bloodType(color="blood")
demon.setDefense(armor=1, fire=0, earth=0.6, energy=0.5, ice=1.12, holy=1.12, death=0.8, physical=0.75, drown=1)
demon.setExperience(6000)
demon.setSpeed(280)
demon.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
demon.walkAround(energy=0, fire=0, poison=0)
demon.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
demon.summon("fire elemental", 10)
demon.maxSummons(2)
demon.voices("Your soul will be mine!", "CHAMEK ATH UTHUL ARAK!", "I SMELL FEEEEAAAAAR!", "Your resistance is futile!", "MUHAHAHA")
demon.regMelee(520)