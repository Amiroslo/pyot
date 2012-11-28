souleater = genMonster("Souleater", (355, 12631), "a souleater")
souleater.setHealth(1100)
souleater.bloodType("undead")
souleater.setDefense(armor=2, fire=1.1, earth=1, energy=1.1, ice=0.5, holy=1.1, death=0, physical=0.3, drown=1)
souleater.setExperience(1300)
souleater.setSpeed(250)
souleater.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
souleater.walkAround(energy=1, fire=1, poison=1)
souleater.setImmunity(paralyze=1, invisible=1, lifedrain=0, drunk=1)
souleater.voices("Life is such a fickle thing!", "I will devour your soul.", "Souuuls!", "I will feed on you.", "Aaaahh")
souleater.regMelee(209)
souleater.loot( ("wand of cosmic energy", 1.0), ("ectoplasmic sushi", 2.0), ("great mana potion", 8.25), ("platinum coin", 100, 6), ("ultimate health potion", 9.0), ("lizard essence", 14.75), (3031, 100, 200), ("necrotic rod", 1.0), ("souleater trophy", 0.0025), ("death ring", 0.25), (5884, 0.0025) )