gargoyle = game.monster.genMonster("Gargoyle", (95, 6027), "a gargoyle")
gargoyle.setHealth(250, healthmax=250)
gargoyle.bloodType(color="blood")
gargoyle.setDefense(armor=10, fire=1.1, earth=0, energy=1, ice=1, holy=1, death=0.6, physical=0.8, drown=1)
gargoyle.setExperience(70)
gargoyle.setSpeed(250)
gargoyle.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=0, targetDistance=1, runOnHealth=30)
gargoyle.walkAround(energy=1, fire=1, poison=0)
gargoyle.setImmunity(paralyze=1, invisible=0, lifedrain=0, drunk=0)
gargoyle.voices("Feel my claws, softskin.", "There is a stone in your shoe!", "Stone sweet stone.", "Harrrr harrrr!", "Chhhhhrrrrk!")
gargoyle.regMelee(65)
gargoyle.loot( ('stone wing', 9.75), ('morning star', 1.25), ('battle shield', 1.5), (2148, 100, 30), (8838, 7.5, 2), ('small stone', 83.5, 10), ('dark armor', 0.25), ('club ring', 0.25), ('strawberry', 3.25, 5), ('shiny stone', 0.25), ('piece of marble rock', 0.5), ('wolf tooth chain', 0.25), ('steel helmet', 0.25) )