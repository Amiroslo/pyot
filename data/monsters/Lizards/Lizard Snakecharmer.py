lizard_snakecharmer = game.monster.genMonster("Lizard Snakecharmer", (115, 6041), "a lizard_snakecharmer")
lizard_snakecharmer.setHealth(315, healthmax=None)
lizard_snakecharmer.bloodType(color="blood")
lizard_snakecharmer.setDefense(armor=17, fire=1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
lizard_snakecharmer.setExperience(210)
lizard_snakecharmer.setSpeed(200)
lizard_snakecharmer.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=1, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=15)
lizard_snakecharmer.walkAround(energy=0, fire=0, poison=0)
lizard_snakecharmer.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
lizard_snakecharmer.summon("cobra", 10)
lizard_snakecharmer.maxSummons(6)
lizard_snakecharmer.voices("I smeeeel warm blood!", "Shhhhhhh")
lizard_snakecharmer.regMelee(30)
lizard_snakecharmer.loot( (2148, 100, 53), ("dead snake", 30.0), ("cape", 11.25), ("life crystal", 0.75), ("lizard scale", 0.75, 3), ("terra rod", 1.25), ("small amethyst", 0.5), ("lizard leather", 2.0), ("life ring", 0.25), (3971, 0.0025), ("mana potion", 0.25), ("snakebite rod", 0.25) )