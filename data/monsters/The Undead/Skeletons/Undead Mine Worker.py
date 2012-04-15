undead_mine_worker = game.monster.genMonster(_("Undead Mine Worker"), (33, 5972), _("an undead mine worker"))
undead_mine_worker.setHealth(65)
undead_mine_worker.bloodType(color="undead")
undead_mine_worker.setDefense(armor=2, fire=1, earth=1, energy=1, ice=1, holy=1.01, death=0, physical=1, drown=1)
undead_mine_worker.setExperience(45)
undead_mine_worker.setSpeed(154)
undead_mine_worker.setBehavior(summonable=435, hostile=1, illusionable=1, convinceable=0, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
undead_mine_worker.walkAround(energy=1, fire=1, poison=1)
undead_mine_worker.setImmunity(paralyze=1, invisible=0, lifedrain=1, drunk=1)
undead_mine_worker.voices("Ahrrr... uhmmm... hmm...", "Grrr...", "Urrrgh... gnarrr...")
undead_mine_worker.regMelee(20)#could be wrong
undead_mine_worker.loot( (2148, 100, 9), ("bone", 52.25), ("brown mushroom", 8.75), ("white mushroom", 37.0, 3), ("mace", 26.0), ("sword", 2.25) )