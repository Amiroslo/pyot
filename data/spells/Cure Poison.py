instant = spell.Spell("Cure Poison", "exana pox", icon=29, target=TARGET_SELF, group=HEALING_GROUP)
instant.require(mana=30, level=10, maglevel=0, learned=0, vocations=(1, 2, 3, 4, 5, 6, 7, 8))
instant.cooldowns(1, 1)
instant.targetEffect() # TODO
instant.effects() # TODO