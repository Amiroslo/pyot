ice_golem = game.monster.genMonster("Ice Golem", (261, 7282), "an ice golem")
ice_golem.setHealth(385, healthmax=385)
ice_golem.bloodType(color="blood")
ice_golem.setDefense(armor=1, fire=0, earth=1, energy=1.2, ice=0, holy=0, death=0, physical=1.2, drown=1)
ice_golem.setExperience(295)
ice_golem.setSpeed(195)
ice_golem.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
ice_golem.walkAround(energy=1, fire=0, poison=1)
ice_golem.setImmunity(paralyze=1, invisible=1, lifedrain=0, drunk=0)
ice_golem.voices("Chrrr.", "Crrrrk.", "Gnarr.")
ice_golem.regMelee(220)
ice_golem.loot( (2148, 100, 63), ('frosty heart', 5.0), ('strong health potion', 0.5), ('strange helmet', 0.25), ('black pearl', 1.5), ('ice cube', 5.0), ('ice rapier', 0.25), ('small sapphire', 0.5), ('crystal sword', 0.25), ('glacier mask', 0.25), ('small diamond', 0.0025), ('shard', 0.25) )