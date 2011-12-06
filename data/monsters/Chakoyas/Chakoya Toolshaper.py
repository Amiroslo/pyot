chakoya_toolshaper = game.monster.genMonster("Chakoya Toolshaper", (259, 7320), "a chakoya toolshaper")#wrong looktype?
chakoya_toolshaper.setHealth(80, healthmax=80)
chakoya_toolshaper.bloodType(color="blood")
chakoya_toolshaper.setDefense(armor=7, fire=0.6, earth=1, energy=1.15, ice=0, holy=0.9, death=1.05, physical=1, drown=1)
chakoya_toolshaper.setExperience(40)
chakoya_toolshaper.setSpeed(270)
chakoya_toolshaper.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=305, pushable=0, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
chakoya_toolshaper.walkAround(energy=1, fire=1, poison=1)
chakoya_toolshaper.setImmunity(paralyze=1, invisible=0, lifedrain=0, drunk=0)
chakoya_toolshaper.voices("Chikuva!", "Jinuma jamjam!", "Suvituka siq chuqua!", "Kiyosa sipaju!")
chakoya_toolshaper.regMelee(35)
chakoya_toolshaper.loot( (2148, 100, 20), ("fish", 34.75, 2), ("mace", 3.75), ("pick", 1.5), ("ice cube", 0.25), ("bone shield", 1.0), ("green perch", 0.25), ("mammoth whopper", 0.0025) )