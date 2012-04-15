demon_skeleton = game.monster.genMonster(_("Demon Skeleton"), (37, 5963), _("a demon skeleton"))
demon_skeleton.setHealth(400)
demon_skeleton.bloodType(color="undead")
demon_skeleton.setDefense(armor=26, fire=0, earth=0, energy=1, ice=1, holy=1.25, death=0, physical=1, drown=0)
demon_skeleton.setExperience(240)
demon_skeleton.setSpeed(230)
demon_skeleton.setBehavior(summonable=620, hostile=1, illusionable=1, convinceable=620, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
demon_skeleton.walkAround(energy=1, fire=0, poison=0)
demon_skeleton.setImmunity(paralyze=1, invisible=0, lifedrain=1, drunk=1)
demon_skeleton.regMelee(180)#approx~
demon_skeleton.loot( ("torch", 30.75), (2148, 100, 45), ("battle shield", 1.0), ("demonic skeletal hand", 5.0), ("battle hammer", 2.75), ("throwing star", 19.5, 3), ("iron helmet", 2.0), ("mysterious fetish", 0.25), ("mana potion", 0.75), ("mind stone", 0.25), ("guardian shield", 0.0025) )