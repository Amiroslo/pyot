# Autoconverted script for PyOT
# Untested. Please remove this message when the script is working properly!

def onUse(creature, thing, position, **k):
    if thing != creature.inventory[SLOT_HEAD]:
        return
    
    magicEffect(creature.position, EFFECT_GIFT_WRAPS)
    return True


register("use", 6578, onUse)
