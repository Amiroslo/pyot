#largely unknown
weak_spawn_of_despair = genMonster("Weak Spawn of Despair", 322, 9923)
weak_spawn_of_despair.health(1000)
weak_spawn_of_despair.type("blood")
weak_spawn_of_despair.defense(armor=10, fire=1, earth=1, energy=1, ice=1.1, holy=1.1, death=1.1, physical=1, drown=1)
weak_spawn_of_despair.experience(0)
weak_spawn_of_despair.speed(200)
weak_spawn_of_despair.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
weak_spawn_of_despair.walkAround(energy=0, fire=0, poison=0)
weak_spawn_of_despair.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
weak_spawn_of_despair.melee(200)
weak_spawn_of_despair.loot( ("small ruby", 92.0, 5), ("rusty armor", 12.0), ("platinum coin", 100, 37), ("small diamond", 36.0, 3), (2148, 100, 153), ("gold ingot", 28.0), ("small topaz", 12.0), ("small sapphire", 24.0, 3), ("small emerald", 56.0, 5), ("midnight shard", 72.0), ("small amethyst", 4.0) )