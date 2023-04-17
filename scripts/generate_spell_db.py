#!/usr/bin/env python

import json

DBS_DIR = "dbs"

MAGE_OVERRIDE_JSON = "mythmancer_mage_spells_override.json"
WARLOCK_OVERRIDE_JSON = "mythmancer_warlock_spells_override.json"

SPELL_TYPES = ["Cleric", "Druid", "Magic User", "Illusionist"]

ALL_SPELLS = {}

with open(f"{DBS_DIR}/{MAGE_OVERRIDE_JSON}") as f:
    final_mage_spells = json.loads(f.read())

with open(f"{DBS_DIR}/{WARLOCK_OVERRIDE_JSON}") as f:
    final_warlock_spells = json.loads(f.read())

for spell_type in SPELL_TYPES:
    with open(f"{DBS_DIR}/{spell_type.lower().replace(' ', '_')}_spells.json") as f:
        d = json.loads(f.read())

    for k in d:
        ALL_SPELLS[f"{spell_type}/{k}"] = d[k]


# Mage spells
for spell in final_mage_spells:
    spell_type = spell.split('/')[0]
    alternative_name = f"{spell_type}/{final_mage_spells[spell].get('OSRIC Name')}"
    osric_spell = None
    if spell in ALL_SPELLS:
        osric_spell = ALL_SPELLS[spell]
    elif alternative_name in ALL_SPELLS:
        osric_spell = ALL_SPELLS[alternative_name]
    else:
        raise Exception(f"Spell <{spell}> or <{alternative_name}> not found in spellbook")

    for field in osric_spell:
        if field not in final_mage_spells[spell]:
            final_mage_spells[spell][field] = osric_spell[field]

final_mage_spells = {k[k.index("/") + 1:]: v for k, v in final_mage_spells.items()}

with open("docs/mage_spells.json", "w") as f:
    f.write(json.dumps(final_mage_spells, indent=2))


# Warlock spells
for spell in final_warlock_spells:
    spell_type = spell.split('/')[0]
    alternative_name = f"{spell_type}/{final_warlock_spells[spell].get('OSRIC Name')}"
    osric_spell = None
    if spell in ALL_SPELLS:
        osric_spell = ALL_SPELLS[spell]
    elif alternative_name in ALL_SPELLS:
        osric_spell = ALL_SPELLS[alternative_name]
    else:
        raise Exception(f"Spell <{spell}>/<{alternative_name}> not found in spellbook")

    for field in osric_spell:
        if field not in final_warlock_spells[spell]:
            final_warlock_spells[spell][field] = osric_spell[field]

final_warlock_spells = {k[k.index("/") + 1:]: v for k, v in final_warlock_spells.items()}

with open("docs/warlock_spells.json", "w") as f:
    f.write(json.dumps(final_warlock_spells, indent=2))

