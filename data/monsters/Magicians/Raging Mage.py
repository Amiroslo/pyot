#mostly unknown
raging_mage = game.monster.genMonster("Raging Mage", (416, 5995), "the raging mage") #unknown looktype or corpse (might be the right looktype)
#raging_mage.setOutfit(69, 66, 69, 66) #might be elem outfit?
raging_mage.setHealth(4000)
raging_mage.bloodType(color="blood")
raging_mage.setDefense(armor=20, fire=1, earth=1, energy=0, ice=1, holy=1, death=1, physical=1, drown=1)
raging_mage.setExperience(1000)
raging_mage.setSpeed(200)
raging_mage.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=800)
raging_mage.walkAround(energy=0, fire=0, poison=0)
raging_mage.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
raging_mage.voices("Behold the all permeating powers I draw from this gate!!", "ENERGY!!")
raging_mage.summon("Golden Servant", 10)
raging_mage.maxSummons(1)