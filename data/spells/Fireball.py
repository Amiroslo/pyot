
conjure = spell.Spell("Fireball", "adori flam", icon=23, group=SUPPORT_GROUP)
conjure.require(mana=460, level=27, maglevel=0, soul=3, learned=0, vocations=(1, 5))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(2302, 5))

# Incomplete! Target rune.
rune = spell.Rune(2302, icon=15, count=5, target=TARGET_TARGET, group=None)
rune.cooldowns(0, 2)
rune.require(mana=0, level=27, maglevel=0)
rune.targetEffect() # TODO
rune.effects() # TODO