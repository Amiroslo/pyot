instant = spell.Spell("Eternal Winter", "exevo gran mas frigo", icon=118, group=ATTACK_GROUP)
instant.require(mana=1050, level=60, maglevel=0, learned=0, vocations=(2, 6))
instant.cooldowns(40, 4)
instant.area(AREA_UE6X6)
instant.targetEffect(callback=spell.damage(5.5, 11, 25, 50, ICE))
instant.effects() # TODO