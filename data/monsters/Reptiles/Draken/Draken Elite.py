draken_elite = genMonster("Draken Elite", (362, 12609), "a draken elite")
draken_elite.setHealth(5550)
draken_elite.bloodType("blood")
draken_elite.setDefense(armor=64, fire=0, earth=0, energy=0.6, ice=1, holy=0.7, death=0.7, physical=1, drown=1)
draken_elite.setExperience(4200)
draken_elite.setSpeed(220)
draken_elite.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
draken_elite.walkAround(energy=0, fire=0, poison=0)
draken_elite.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
draken_elite.voices("For ze emperor!", "You will die zhouzandz deazhz!")
draken_elite.regMelee(350)
draken_elite.loot( (3031, 100, 200), ("broken slicer", 25.0), ("meat", 29.5), ("platinum coin", 100, 8), ("great mana potion", 18.25, 3), ("small diamond", 5.25, 4), ("draken wristbands", 13.75), ("broken draken mail", 17.5), ("ultimate health potion", 17.75, 3), ("zaoan armor", 0.5), ("draken sulphur", 8.0), ("zaoan helmet", 0.25), ("twiceslicer", 1.0), ("zaoan legs", 0.75), ("magic sulphur", 2.0), ("assassin dagger", 1.0), ("zaoan sword", 0.5), ("draken boots", 0.25), ("elite draken mail", 0.0025), ("blade of corruption", 0.0025), ("cobra crown", 0.0025) )