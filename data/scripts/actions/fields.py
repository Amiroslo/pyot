
def effectOverTime(creature, damage, perTime, effect, forTicks, ticks=0):
    if not creature.alive:
        return

    ticks += 1
    creature.modifyHealth(-damage)
    creature.magicEffect(effect)


    if ticks < forTicks:
        callLater(perTime, effectOverTime, creature, damage, perTime, effect, forTicks, ticks)

def callback(creature, thing, **k):
    if thing.fieldDamage:
        try:
            effect, effectOverTime = typeToEffect(thing.field)[0:2]
        except:
            effect = EFFECT_POOF
            effectOverTime = EFFECT_POOF

        creature.magicEffect(effect)
        creature.modifyHealth(-thing.fieldDamage)
        if thing.turns:
            effectOverTime(creature, thing.fieldDamage, thing.fieldTicks / 1000,effectOverTime, thing.fieldCount)

registerForAttr('walkOn', 'fieldDamage', callback)
