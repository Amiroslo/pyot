duskbringer = game.monster.genMonster("Duskbringer", (300, 8955), "a duskbringer")
duskbringer.setHealth(3000, healthmax=3000)
duskbringer.bloodType(color="blood")
duskbringer.setDefense(armor=59, fire=0.6, earth=0.2, energy=0.95, ice=1.1, holy=0.7, death=1.05, physical=1, drown=1)
duskbringer.setExperience(2600)
duskbringer.setSpeed(300)
duskbringer.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
duskbringer.walkAround(energy=0, fire=0, poison=0)
duskbringer.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
duskbringer.voices("Death!", "Come a little closer!", "The end is near!")
duskbringer.regMelee(350)
duskbringer.loot( ("midnight shard", 8.75) )