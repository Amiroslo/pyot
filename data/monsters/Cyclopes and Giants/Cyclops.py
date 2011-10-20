cyclops = game.monster.genMonster("cyclops", (22, 5962), "a cyclops")
cyclops.setHealth(260, healthmax=260)
cyclops.bloodType(color="blood")
cyclops.setDefense(armor=10, fire=1, earth=1.1, energy=0.75, ice=1, holy=0.8, death=1.1, physical=1, drown=1)
cyclops.setExperience(150)
cyclops.setSpeed(200)
cyclops.setBehavior(summonable=490, hostile=1, illusionable=1, convinceable=490, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
cyclops.walkAround(energy=1, fire=1, poison=1)
cyclops.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
cyclops.voices("Human, uh whil dyh!", "Youh ah trak!", "Let da mashing begin!", "Toks utat.", "Il lorstok human!")
cyclops.regMelee(105)