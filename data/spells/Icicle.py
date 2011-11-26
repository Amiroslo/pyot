
conjure = spell.Spell("Icicle", "adori frigo", icon=23, group=SUPPORT_GROUP)
conjure.require(mana=460, level=28, maglevel=0, soul=3, learned=0, vocations=(2, 6))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(2271, 5))

# Incomplete! Target rune.
rune = spell.Rune(2271, icon=114, count=5, target=TARGET_TARGET, group=None)
rune.cooldowns(0, 2)
rune.require(mana=0, level=28, maglevel=0)
rune.targetEffect() # TODO
rune.effects() # TODO