undead_mine_worker = genMonster("Undead Mine Worker", 33, 5972)
undead_mine_worker.health(65)
undead_mine_worker.type("undead")
undead_mine_worker.defense(armor=2, fire=1, earth=1, energy=1, ice=1, holy=1.01, death=0, physical=1, drown=1)
undead_mine_worker.experience(45)
undead_mine_worker.speed(154)
undead_mine_worker.behavior(summonable=435, hostile=True, illusionable=True, convinceable=0, pushable=True, pushItems=False, pushCreatures=False, targetDistance=1, runOnHealth=0)
undead_mine_worker.walkAround(energy=1, fire=1, poison=1)
undead_mine_worker.immunity(paralyze=1, invisible=0, lifedrain=1, drunk=1)
undead_mine_worker.voices("Ahrrr... uhmmm... hmm...", "Grrr...", "Urrrgh... gnarrr...")
undead_mine_worker.melee(20)#could be wrong
undead_mine_worker.loot( (2148, 100, 9), ("bone", 52.25), ("brown mushroom", 8.75), ("white mushroom", 37.0, 3), ("mace", 26.0), ("sword", 2.25) )