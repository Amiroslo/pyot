sea_serpent = genMonster("Sea Serpent", (275, 8307), "a sea serpent")
sea_serpent.setHealth(1750)
sea_serpent.bloodType("blood")
sea_serpent.setDefense(armor=27, fire=0.7, earth=1, energy=1.05, ice=0, holy=1, death=0.9, physical=1.1, drown=0)
sea_serpent.setExperience(2300)
sea_serpent.setSpeed(300)
sea_serpent.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=300)
sea_serpent.walkAround(energy=0, fire=0, poison=0)
sea_serpent.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
sea_serpent.voices("CHHHRRRR", "HISSSS")
sea_serpent.regMelee(250)
sea_serpent.loot( (3031, 100, 244), ("stealth ring", 0.5), ("dragon ham", 60.25), ("small sapphire", 8.0, 3), ("strong health potion", 4.75), ("sea serpent scale", 10.25), ("plate legs", 7.25), ("strong mana potion", 4.0), ("serpent sword", 4.0), ("glacier amulet", 1.0), ("northwind rod", 1.0), ("spirit cloak", 3.0), ("great mana potion", 1.0), ("focus cape", 0.5), ("glacier kilt", 0.5), ("ring of healing", 1.25), ("crystalline armor", 0.0025), ("leviathan's amulet", 0.0025) )