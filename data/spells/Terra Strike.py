instant = spell.Spell("Terra Strike", "exori tera", icon=113, group=ATTACK_GROUP)
instant.require(mana=20, level=13, maglevel=0, learned=0, vocations=(1, 5, 2, 6))
instant.cooldowns(2, 2)
instant.targetEffect(callback=spell.damage(1.4, 2.2, 4, 18, EARTH))
instant.effects() # TODO