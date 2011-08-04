import game.monster

pirate_skeleton = game.monster.genMonster("Pirate Skeleton", (195, 6070), "a pirate skeleton")
pirate_skeleton.setHealth(190)
pirate_skeleton.bloodType(color="undead")
pirate_skeleton.setDefense(19, armor=18, fire=1, earth=1, energy=1, ice=1, holy=1.25, death=0, physical=1, drown=1)
pirate_skeleton.setExperience(85)
pirate_skeleton.setSpeed(230)
pirate_skeleton.setBehavior(summonable=0, attackable=1, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=20)
pirate_skeleton.walkAround(energy=1, fire=1, poison=1)
pirate_skeleton.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)