from src.data.importers.importerplugin import ImporterPlugin


class MorePurpleMoreBetter(ImporterPlugin):
    name = "MorePurpleMoreBetter"
    key_conversion = {
        "PC Name": "CHProperty.CHARACTER_NAME",
        "Player Name": "CHProperty.PLAYER_NAME",
        "PP_BACKGROUND": "CHProperty.BACKGROUND",
        "PP_CHAR_LEVEL": "CHProperty.CLASS_LEVEL",
        "PP_NOTES": "CHProperty.ADDITIONAL_NOTES",
        "Race": "CHProperty.RACE",
        "PP_EXPERIENCE": "CHProperty.XP",
        "Str": "CHProperty.STR",
        "Str Mod": "CHProperty.STR_MOD",
        "Str ST Mod": "CHProperty.STR_ST_MOD",
        "Str ST Prof": "CHProperty.STR_ST_PROF",
        "Dex": "CHProperty.DEX",
        "Dex Mod": "CHProperty.DEX_MOD",
        "Dex ST Mod": "CHProperty.DEX_ST_MOD",
        "Dex ST Prof": "CHProperty.DEX_ST_PROF",
        "Con": "CHProperty.CON",
        "Con Mod": "CHProperty.CON_MOD",
        "Con ST Mod": "CHProperty.CON_ST_MOD",
        "Con ST Prof": "CHProperty.CON_ST_PROF",
        "Int": "CHProperty.INT",
        "Int Mod": "CHProperty.INT_MOD",
        "Int ST Mod": "CHProperty.INT_ST_MOD",
        "Int ST Prof": "CHProperty.INT_ST_PROF",
        "Wis": "CHProperty.WIS",
        "Wis Mod": "CHProperty.WIS_MOD",
        "Wis ST Mod": "CHProperty.WIS_ST_MOD",
        "Wis ST Prof": "CHProperty.WIS_ST_PROF",
        "Cha": "CHProperty.CHA",
        "Cha Mod": "CHProperty.CHA_MOD",
        "Cha ST Mod": "CHProperty.CHA_ST_MOD",
        "Cha ST Prof": "CHProperty.CHA_ST_PROF",
        "PP_RESISTANCE": "CHProperty.SAVE_MODIFIERS",
        "PP_DEFENSES": "CHProperty.DEFENSES",
        "Passive Perception": "CHProperty.PASSIVE_PERCEPTION",
        "Vision": "CHProperty.SENSES",
        "Proficiency Bonus": "CHProperty.PROF_BONUS",
        "HP Max": "CHProperty.MAX_HP",
        "HP Temp": "CHProperty.TEMP_HP",
        "HP Current": "CHProperty.CURRENT_HP",
        "Death Save Success1": "CHProperty.SUCCESSFUL_SAVE_1",
        "Death Save Success2": "CHProperty.SUCCESSFUL_SAVE_2",
        "Death Save Success3": "CHProperty.SUCCESSFUL_SAVE_3",
        "Death Save Fail1": "CHProperty.FAILED_SAVE_1",
        "Death Save Fail2": "CHProperty.FAILED_SAVE_2",
        "Death Save Fail3": "CHProperty.FAILED_SAVE_3",
        "PP_HIT_DICE": "CHProperty.TOTAL_HIT_DICE",
        "AC": "CHProperty.AC",
        "Init Bonus": "CHProperty.INITIATIVE",
        "Speed": "CHProperty.SPEED",
        "PP_ACTIONS": "CHProperty.ACTIONS",
        "Sex": "CHProperty.GENDER",
        "Age": "CHProperty.AGE",
        "Height": "CHProperty.HEIGHT",
        "Weight": "CHProperty.WEIGHT",
        "Alignment": "CHProperty.ALIGNMENT",
        "Faith/Deity": "CHProperty.FAITH",
        "Hair colour": "CHProperty.HAIR",
        "Eyes colour": "CHProperty.EYES",
        "Skin colour": "CHProperty.SKIN",
        "Weight Carried": "CHProperty.WEIGHT_CARRIED",
        "Weight Encumbered": "CHProperty.ENCUMBERED",
        "Weight Push/Drag/Lift": "CHProperty.PUSH_DRAG_LIFT",
        "Copper Pieces": "CHProperty.CP",
        "Silver Pieces": "CHProperty.SP",
        "Gold Pieces": "CHProperty.GP",
        "Electrum Pieces": "CHProperty.EP",
        "Platinum Pieces": "CHProperty.PP",
        "Spell save DC 1": "CHProperty.ABILITYSAVEDC1",
        "Spell save DC 2": "CHProperty.ABILITYSAVEDC2",
        "Spell DC 1 Mod": "CHProperty.ABILITYSAVESCORE1",
        "Spell DC 2 Mod": "CHProperty.ABILITYSAVESCORE2",
        "PP_FEATURES_RACIAL_TRAITS": "CHProperty.FEATURES_TRAITS",
        "Personality Trait": "CHProperty.PERSONALITY_TRAITS",
        "Ideal": "CHProperty.IDEALS",
        "Bond": "CHProperty.BONDS",
        "Flaw": "CHProperty.FLAWS",
        "Background_Appearance": "CHProperty.APPEARANCE",
        "Background_History": "CHProperty.BACKSTORY",
        "PP_ALLIES_ORGANIZATIONS": "CHProperty.ALLIES_ORGANIZATIONS"
    }
    keys_to_ignore = [
        "Image.calc_boxes.CSfront",
        "Image.calc_lines.CSfront",
        "Show Buttons",
        "HeaderIcon",
        "Whiteout.Standard",
        "Image.HoS",
        "Image.calc_boxes.HoS",
        "Image.calc_lines.HoS",
        "Text.HoS.Ability",
        "HoS",
        "HoS Mod",
        "Text.HoS.Save",
        "Save Modifiers Title",
        "Skill Modifiers All Text",
        "Skill Modifiers Title",
        "Buttons.HP Max",
        "Heal",
        "Proficiency Bonus Modifiers Title",
        "Proficiency Bonus Dice",
        "Proficiency Bonus Dice Title",
        "Speed encumbered",
        "AC Shield Weight Title",
        "AC Armor Weight Title",
        "AC Armor Bonus",
        "AC Shield Bonus",
        "AC Dexterity Modifier",
        "AC Magic",
        "AC Misc Mod 1",
        "AC Misc Mod 2",
        "AC Armor Description",
        "AC Armor Weight",
        "AC Shield Bonus Description",
        "AC Shield Weight",
        "Medium Armor",
        "Heavy Armor",
        "AC Stealth Disadvantage Title",
        "AC Stealth Disadvantage",
        "AC Magic Description",
        "AC Misc Mod 1 Description",
        "AC Misc Mod 2 Description",
        "Inspiration",
        "Image.SaveDC",
        "P5.ASnotes.Notes.Options",
        "P5.ASnotes.Whiteout.Notes.Left",
        "P5.ASnotes.Whiteout.Notes.Right",
        "P5.ASnotes.SheetInformation",
        "P5.ASnotes.CopyrightInformation",
        "P6.ASnotes.Notes.Options",
        "P6.ASnotes.Whiteout.Notes.Left",
        "P6.ASnotes.Whiteout.Notes.Right",
        "P6.ASnotes.SheetInformation",
        "P6.ASnotes.CopyrightInformation",
        "PRsheet.toFocus",
        "Text.PRsheet.AL.explanation",
        "Text.PRsheet.AL.asterisk",
        "Lifestyle daily cost",
        "Lifestyle",
        "Image.Background_FactionRank",
        "Background_Faction.Text",
        "Portrait",
        "Symbol",
        "Image.DnDLogo.short",
        "Size Category",
        "Feat Button 1",
        "Feat Button 2",
        "Feat Button 3",
        "Feat Button 4",
        "Carrying Capacity Multiplier Title",
        "Carrying Capacity Multiplier",
        "Display.Weighttxt.LbKg",
        "Adventuring Gear Location.Line",
        "Adventuring Gear Location.Title",
        "Class Features Menu",
        "Background Menu",
        "Race Features Menu",
        "Equipment.menu",
        "Weight Remember Coins Total",
        "Weight Remember Coins",
        "Attuned Magic Items Whiteout",
        "Attuned Magic Items Title",
        "ATTUNED MAGICAL ITEMS",
        "Attack.Titles",
        "SR",
        "LR",
        "Dawn",
        "ShowHide 2nd DC"
    ]
    wildcards_to_ignore = [
        "AScomp",
        "Adventuring Gear Button",
        "Adventuring Gear Location.Subtotal",
        "Button",
        "Image",
        "BlueText",
        "Limited Feature ",
        "Weapon Selection",
        " Remember"
    ]
    incremental_lists = {
        "Attack": {
            "column_to_form": {
                "name": [
                    "Wpn Name {}"
                ],
                "attack_bonus": [
                    "Wpn{} AtkBonus"
                ],
                "damage": [
                    "Wpn{} Damage"
                ],
                "notes": [
                    "Wpn Notes {}"
                ]
            },
            "max_items": 6,
            "zero_indexed": False,
            "hardcoded_keys": {
                "Wpn Name 1": "Wpn Name",
                "Wpn2 AtkBonus": "Wpn2 AtkBonus ",
                "Wpn2 Damage": "Wpn2 Damage ",
                "Wpn3 AtkBonus": "Wpn3 AtkBonus  ",
                "Wpn3 Damage": "Wpn3 Damage "
            }
        },
        "Equipment": {
            "column_to_form": {
                "name": [
                    "Eq Name{}"
                ],
                "quantity": [
                    "Eq Qty{}"
                ],
                "weight": [
                    "Eq Weight{}"
                ]
            },
            "max_items": 56,
            "zero_indexed": True,
            "hardcoded_keys": {}
        },
        "Equipment": {
            "column_to_form": {
                "name": [
                    "Attuned Name{}"
                ],
                "quantity": [
                    "Attuned Qty{}"
                ],
                "weight": [
                    "Attuned Weight{}"
                ]
            },
            "max_items": 3,
            "zero_indexed": False,
            "hardcoded_keys": {
                "Attuned Weight3": "AttunedWeight3"
            }
        },
        "Spell": {
            "column_to_form": {
                "prepared": [
                    "spellPrepared{}",
                    "Prepared{}"
                ],
                "name": [
                    "spellName{}",
                    "Name{}"
                ],
                "source": [
                    "spellSource{}",
                    "Source{}"
                ],
                "save_hit": [
                    "spellSaveHit{}",
                    "SaveHit{}"
                ],
                "time": [
                    "spellCastingTime{}",
                    "CastingTime{}"
                ],
                "spell_range": [
                    "spellRange{}",
                    "Range{}"
                ],
                "components": [
                    "spellComponents{}",
                    "Components{}"
                ],
                "duration": [
                    "spellDuration{}",
                    "Duration{}"
                ],
                "page": [
                    "spellPage{}",
                    "Page{}"
                ],
                "notes": [
                    "spellNotes{}",
                    "Notes{}"
                ]
            },
            "max_items": 50,
            "zero_indexed": True,
            "hardcoded_keys": {
                "spellSource45": "Source45",
                "spellSource46": "Source46",
                "spellSource47": "Source47",
                "spellSource48": "Source48",
                "spellSource49": "Source49",
                "spellPage45": "SpellSource45",
                "spellPage46": "SpellSource46",
                "spellPage47": "SpellSource47",
                "spellPage48": "SpellSource48",
                "spellPage49": "SpellSource49"
            },
            "header": "spellHeader"
        },
        "SpellSlot": {
            "column_to_form": {
                "level": [
                    "spellHeader{}"
                ],
                "n_slots": [
                    "spellSlotHeader{}"
                ]
            },
            "max_items": 10,
            "zero_indexed": False,
            "hardcoded_keys": {}
        }
    }
    hardcoded_lists = {
        "Skill": {
            "ACROBATICS": {
                "prof": "Acr Prof",
                "exp": "Acr Exp",
                "mod": "Acr",
                "bonus": "Acr Bonus"
            },
            "ANIMALHANDLING": {
                "prof": "Ani Prof",
                "exp": "Ani Exp",
                "mod": "Ani",
                "bonus": "Ani Bonus"
            },
            "ARCANA": {
                "prof": "Arc Prof",
                "exp": "Arc Exp",
                "mod": "Arc",
                "bonus": "Arc Bonus"
            },
            "ATHLETICS": {
                "prof": "Ath Prof",
                "exp": "Ath Exp",
                "mod": "Ath",
                "bonus": "Ath Bonus"
            },
            "DECEPTION": {
                "prof": "Dec Prof",
                "exp": "Dec Exp",
                "mod": "Dec",
                "bonus": "Dec Bonus"
            },
            "HISTORY": {
                "prof": "His Prof",
                "exp": "His Exp",
                "mod": "His",
                "bonus": "His Bonus"
            },
            "INSIGHT": {
                "prof": "Ins Prof",
                "exp": "Ins Exp",
                "mod": "Ins",
                "bonus": "Ins Bonus"
            },
            "INTIMIDATION": {
                "prof": "Inti Prof",
                "exp": "Inti Exp",
                "mod": "Inti",
                "bonus": "Inti Bonus"
            },
            "INVESTIGATION": {
                "prof": "Inv Prof",
                "exp": "Inv Exp",
                "mod": "Inv",
                "bonus": "Inv Bonus"
            },
            "MEDICINE": {
                "prof": "Med Prof",
                "exp": "Med Exp",
                "mod": "Med",
                "bonus": "Med Bonus"
            },
            "NATURE": {
                "prof": "Nat Prof",
                "exp": "Nat Exp",
                "mod": "Nat",
                "bonus": "Nat Bonus"
            },
            "PERCEPTION": {
                "prof": "Perc Prof",
                "exp": "Perc Exp",
                "mod": "Perc",
                "bonus": "Perc Bonus"
            },
            "PERFORMANCE": {
                "prof": "Perf Prof",
                "exp": "Perf Exp",
                "mod": "Perf",
                "bonus": "Perf Bonus"
            },
            "PERSUASION": {
                "prof": "Pers Prof",
                "exp": "Pers Exp",
                "mod": "Pers",
                "bonus": "Pers Bonus"
            },
            "RELIGION": {
                "prof": "Rel Prof",
                "exp": "Rel Exp",
                "mod": "Rel",
                "bonus": "Rel Bonus"
            },
            "SLEIGHTOFHAND": {
                "prof": "Sle Prof",
                "exp": "Sle Exp",
                "mod": "Sle",
                "bonus": "Sle Bonus"
            },
            "STEALTH": {
                "prof": "Ste Prof",
                "exp": "Ste Exp",
                "mod": "Ste",
                "bonus": "Ste Bonus"
            },
            "SURVIVAL": {
                "prof": "Sur Prof",
                "exp": "Sur Exp",
                "mod": "Sur",
                "bonus": "Sur Bonus"
            },
            "Tool": {
                "prof": "Too Prof",
                "exp": "Too Exp",
                "mod": "Too",
                "bonus": "Too Bonus",
                "name": "Too Text"
            }
        }
    }
    override = {
        "Str Mod": "STR",
        "Dex Mod": "DEX",
        "Con Mod": "CON",
        "Int Mod": "INT",
        "Wis Mod": "WIS",
        "Cha Mod": "CHA"
    }
    pre_processing = {
        "PP_CHAR_LEVEL": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "Class and Levels",
                    "Character Level"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "PP_BACKGROUND": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "Background",
                    "Background Extra"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "PP_EXPERIENCE": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "Total Experience",
                    "Next level"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "PP_RESISTANCE": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "Saving Throw advantages / disadvantages",
                    "Resistance Damage Type 1",
                    "Resistance Damage Type 2",
                    "Resistance Damage Type 3",
                    "Resistance Damage Type 4",
                    "Resistance Damage Type 5",
                    "Resistance Damage Type 6"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "Str ST Prof": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Dex ST Prof": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Con ST Prof": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Int ST Prof": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Wis ST Prof": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Cha ST Prof": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Death Save Success1": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Death Save Success2": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Death Save Success3": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Death Save Fail1": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Death Save Fail2": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "Death Save Fail3": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "PP_HIT_DICE": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "HD1 Level",
                    "HD1 Die",
                    "HD2 Level",
                    "HD2 Die",
                    "HD3 Level",
                    "HD3 Die"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "PP_ACTIONS": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "Action 1",
                    "Action 2",
                    "Action 3",
                    "Action 4",
                    "Action 5",
                    "Action 6",
                    "Bonus Action 1",
                    "Bonus Action 2",
                    "Bonus Action 3",
                    "Bonus Action 4",
                    "Bonus Action 5",
                    "Bonus Action 6",
                    "Reaction 1",
                    "Reaction 2",
                    "Reaction 3",
                    "Reaction 4",
                    "Reaction 5",
                    "Reaction 6"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "PP_NOTES": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "Extra.Notes",
                    "P5.ASnotes.Notes.Left",
                    "P5.ASnotes.Notes.Right",
                    "P6.ASnotes.Notes.Left",
                    "P6.ASnotes.Notes.Right"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "PP_FEATURES_RACIAL_TRAITS": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "Class Features",
                    "Class, Features",
                    "Racial Traits"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "PP_ALLIES_ORGANIZATIONS": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "Background_Organisation.Left",
                    "Background_Organisation.Right",
                    "Background_Enemies"
                ],
                "separator": " "
            },
            "delete_parameters": True
        }
    }

    def __init__(self):
        super(MorePurpleMoreBetter, self).__init__()
