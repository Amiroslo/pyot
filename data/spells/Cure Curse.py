instant = spell.Spell("Cure Curse", "exana mort", icon=147, target=TARGET_SELF, group=HEALING_GROUP)
instant.require(mana=40, level=80, maglevel=0, learned=0, vocations=(3, 7))
instant.cooldowns(1, 1)
instant.targetEffect() # TODO
instant.effects() # TODO