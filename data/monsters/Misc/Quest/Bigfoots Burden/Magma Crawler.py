Magma_Crawler = game.monster.genMonster("Magma Crawler", (492, 15991), "a magma crawler")
Magma_Crawler.setHealth(4800)
Magma_Crawler.bloodType(color="blood")
Magma_Crawler.setDefense(armor=50, fire=0, earth=0, energy=0.9, ice=0.95, holy=1, death=0.75, physical=0.95, drown=1)
Magma_Crawler.setExperience(2700)
Magma_Crawler.setSpeed(500)
Magma_Crawler.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=0)
Magma_Crawler.walkAround(energy=0, fire=0, poison=0)
Magma_Crawler.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Magma_Crawler.voices("Crrroak!")
Magma_Crawler.regMelee(350)