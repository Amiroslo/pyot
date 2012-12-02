convert = {}
convert[4137] = (5905, EFFECT_MAGIC_BLUE) # Vampire dust
convert[4097] = (5906, EFFECT_MAGIC_RED) # Demon dust

@register("useWith", 5942)
def useWith(creature, thing, onThing, onPosition, **k):
    if not onThing.itemId in convert:
        return

    if random.randint(1,15) == 1:
        try:
            creature.addItem(Item(convert[onThing.itemId][0]))
            magicEffect(onPosition, convert[onThing.itemId][1])
        except:
            creature.notPossible()
            return
    else:
        magicEffect(onPosition, EFFECT_BLOCKHIT)

    onThing.transform(onThing.itemId + 1)
    onThing.decay()
