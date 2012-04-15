draken_spellweaver = game.monster.genMonster(_("Draken Spellweaver"), (340, 11317), _("a draken spellweaver"))
draken_spellweaver.setHealth(5000, healthmax=5000)
draken_spellweaver.bloodType(color="blood")
draken_spellweaver.setDefense(armor=26, fire=0, earth=0, energy=1.1, ice=1.1, holy=1.05, death=0.1, physical=1.1, drown=1)
draken_spellweaver.setExperience(2600)
draken_spellweaver.setSpeed(240)
draken_spellweaver.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
draken_spellweaver.walkAround(energy=0, fire=0, poison=0)
draken_spellweaver.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
draken_spellweaver.regMelee(250)
#draken_spellweaver.loot()