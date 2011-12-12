plaguesmith = game.monster.genMonster("Plaguesmith", (247, 6516), "a plaguesmith")
plaguesmith.setHealth(8250, healthmax=8250)
plaguesmith.bloodType(color="blood")
plaguesmith.setDefense(armor=32, fire=0.7, earth=0, energy=1.1, ice=0.8, holy=1.1, death=0.9, physical=1, drown=1)
plaguesmith.setExperience(4500)
plaguesmith.setSpeed(340)
plaguesmith.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=500)
plaguesmith.walkAround(energy=1, fire=0, poison=0)
plaguesmith.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
plaguesmith.voices("You are looking a bit feverish!", "You don't look that good!", "Hachoo!", "Cough Cough")
plaguesmith.regMelee(540)#poisons you up to 10 hp/turn
plaguesmith.loot( ("onyx arrow", 20.5, 4), ("small amethyst", 10.25, 3), ("morning star", 30.75), (2148, 100, 270), ("dirty cape", 60.0), ("steel shield", 20.0), ("soul orb", 12.0), ("piece of iron", 20.25), ("club ring", 5.25), ("platinum coin", 12.0, 2), ("emerald bangle", 0.5), ("demonic essence", 9.0, 3), ("two handed sword", 19.5), ("rusty armor", 8.0), ("great health potion", 10.0), ("battle hammer", 19.75), (2235, 49.5), ("piece of hell steel", 1.0), ("knight legs", 7.0), ("war hammer", 2.0), ("steel boots", 1.25), ("silver brooch", 2.0), ("axe ring", 4.75), ("piece of draconian steel", 1.0), ("hammer of wrath", 0.75), ("piece of royal steel", 1.0), ("war horn", 0.0025) )