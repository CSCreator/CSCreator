from src.data.importers.importerplugin import ImporterPlugin


class DNDBeyond(ImporterPlugin):
    name = "DND Beyond"
    key_conversion = {
        "PP_NOTES": "CHProperty.ADDITIONAL_NOTES",
        "PP_ACTIONS": "CHProperty.ACTIONS",
        "PP_FEATURES": "CHProperty.FEATURES_TRAITS",
        "CharacterName": "CHProperty.CHARACTER_NAME",
        "CLASS  LEVEL": "CHProperty.CLASS_LEVEL",
        "PLAYER NAME": "CHProperty.PLAYER_NAME",
        "RACE": "CHProperty.RACE",
        "BACKGROUND": "CHProperty.BACKGROUND",
        "EXPERIENCE POINTS": "CHProperty.XP",
        "StrProf": "CHProperty.STR_ST_PROF",
        "DexProf": "CHProperty.DEX_ST_PROF",
        "ConProf": "CHProperty.CON_ST_PROF",
        "IntProf": "CHProperty.INT_ST_PROF",
        "WisProf": "CHProperty.WIS_ST_PROF",
        "ChaProf": "CHProperty.CHA_ST_PROF",
        "ST Strength": "CHProperty.STR_ST_MOD",
        "ST Dexterity": "CHProperty.DEX_ST_MOD",
        "ST Constitution": "CHProperty.CON_ST_MOD",
        "ST Intelligence": "CHProperty.INT_ST_MOD",
        "ST Wisdom": "CHProperty.WIS_ST_MOD",
        "ST Charisma": "CHProperty.CHA_ST_MOD",
        "STR": "CHProperty.STR",
        "DEX": "CHProperty.DEX",
        "CON": "CHProperty.CON",
        "INT": "CHProperty.INT",
        "WIS": "CHProperty.WIS",
        "CHA": "CHProperty.CHA",
        "STRmod": "CHProperty.STR_MOD",
        "DEXmod ": "CHProperty.DEX_MOD",
        "CONmod": "CHProperty.CON_MOD",
        "INTmod": "CHProperty.INT_MOD",
        "WISmod": "CHProperty.WIS_MOD",
        "CHamod": "CHProperty.CHA_MOD",
        "Defenses": "CHProperty.DEFENSES",
        "SaveModifiers": "CHProperty.SAVE_MODIFIERS",
        "Passive1": "CHProperty.PASSIVE_PERCEPTION",
        "Passive2": "CHProperty.PASSIVE_WISDOM",
        "Passive3": "CHProperty.PASSIVE_INVESTIGATION",
        "AdditionalSenses": "CHProperty.SENSES",
        "Init": "CHProperty.INITIATIVE",
        "AC": "CHProperty.AC",
        "ProfBonus": "CHProperty.PROF_BONUS",
        "AbilitySaveDC": "CHProperty.ABILITYSAVEDC1",
        "AbilitySaveScore1": "CHProperty.ABILITYSAVESCORE1",
        "AbilitySaveScore2": "CHProperty.ABILITYSAVESCORE2",
        "AbilitySaveDC2": "CHProperty.ABILITYSAVEDC2",
        "Speed": "CHProperty.SPEED",
        "MaxHP": "CHProperty.MAX_HP",
        "CurrentHP": "CHProperty.CURRENT_HP",
        "TempHP": "CHProperty.TEMP_HP",
        "Total": "CHProperty.TOTAL_HIT_DICE",
        "HD": "CHProperty.HIT_DICE",
        "Check Box 12": "CHProperty.SUCCESSFUL_SAVE_1",
        "Check Box 13": "CHProperty.SUCCESSFUL_SAVE_2",
        "Check Box 14": "CHProperty.SUCCESSFUL_SAVE_3",
        "Check Box 15": "CHProperty.FAILED_SAVE_1",
        "Check Box 16": "CHProperty.FAILED_SAVE_2",
        "Check Box 17": "CHProperty.FAILED_SAVE_3",
        "CP": "CHProperty.CP",
        "SP": "CHProperty.SP",
        "EP": "CHProperty.EP",
        "GP": "CHProperty.GP",
        "PP": "CHProperty.PP",
        "Weight Carried": "CHProperty.WEIGHT_CARRIED",
        "Encumbered": "CHProperty.ENCUMBERED",
        "PushDragLift": "CHProperty.PUSH_DRAG_LIFT",
        "GENDER": "CHProperty.GENDER",
        "AGE": "CHProperty.AGE",
        "SIZE": "CHProperty.SIZE",
        "HEIGHT": "CHProperty.HEIGHT",
        "WEIGHT": "CHProperty.WEIGHT",
        "ALIGNMENT": "CHProperty.ALIGNMENT",
        "FAITH": "CHProperty.FAITH",
        "SKIN": "CHProperty.SKIN",
        "EYES": "CHProperty.EYES",
        "HAIR": "CHProperty.HAIR",
        "AlliesOrganizations": "CHProperty.ALLIES_ORGANIZATIONS",
        "PersonalityTraits ": "CHProperty.PERSONALITY_TRAITS",
        "Ideals": "CHProperty.IDEALS",
        "Bonds": "CHProperty.BONDS",
        "Appearance": "CHProperty.APPEARANCE",
        "Flaws": "CHProperty.FLAWS",
        "Backstory": "CHProperty.BACKSTORY",
        "spellCastingAbility0": "CHProperty.SPELLCASTINGABILITY0",
        "spellSaveDC0": "CHProperty.SPELLSAVEDC0",
        "spellAtkBonus0": "CHProperty.SPELLATKBONUS0",
        "spellCastingClass0": "CHProperty.SPELLCASTINGCLASS0"
    }
    keys_to_ignore = {
        "CharacterName2": None,
        "CLASS  LEVEL2": None,
        "PLAYER NAME2": None,
        "RACE2": None,
        "BACKGROUND2": None,
        "EXPERIENCE POINTS2": None,
        "CharacterName3": None,
        "CLASS  LEVEL3": None,
        "PLAYER NAME3": None,
        "RACE3": None,
        "BACKGROUND3": None,
        "EXPERIENCE POINTS3": None,
        "CharacterName4": None,
        "spellPreparedHeader0": None,
        "spellSaveHitHeader0": None,
        "spellCastingTimeHeader0": None,
        "spellRangeHeader0": None,
        "spellComponentsHeader0": None,
        "spellDurationHeader0": None,
        "spellPageHeader0": None,
        "spellNotesHeader0": None
    }
    wildcards_to_ignore = {
        "spellPreparedBlankHeader": None,
        "spellNameBlankHeader": None,
        "spellSourceBlankHeader": None,
        "spellSaveHitBlankHeader": None,
        "spellCastingTimeBlankHeader": None,
        "spellRangeBlankHeader": None,
        "spellComponentsBlankHeader": None,
        "spellDurationBlankHeader": None,
        "spellPageBlankHeader": None,
        "spellNotesBlankHeader": None,
        "spellPreparedHeader": None,
        "spellSaveHitHeader": None,
        "spellCastingTimeHeader": None,
        "spellRangeHeader": None,
        "spellComponentsHeader": None,
        "spellDurationHeader": None,
        "spellPageHeader": None,
        "spellNotesHeader": None
    }
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
            "Skills.ACROBATICS": {
                "name": "Skills.ACROBATICS",
                "prof": "AcrobaticsProf",
                "mod": "AcrobaticsMod",
                "bonus": "Acrobatics"
            },
            "Skills.ANIMALHANDLING": {
                "name": "Skills.ANIMALHANDLING",
                "prof": "AnimalHandlingProf",
                "mod": "AnimalMod",
                "bonus": "Animal"
            },
            "Skills.ARCANA": {
                "name": "Skills.ARCANA",
                "prof": "ArcanaProf",
                "mod": "ArcanaMod",
                "bonus": "Arcana"
            },
            "Skills.ATHLETICS": {
                "name": "Skills.ATHLETICS",
                "prof": "AthleticsProf",
                "mod": "AthleticsMod",
                "bonus": "Athletics"
            },
            "Skills.DECEPTION": {
                "name": "Skills.DECEPTION",
                "prof": "DeceptionProf",
                "mod": "DeceptionMod",
                "bonus": "Deception"
            },
            "Skills.HISTORY": {
                "name": "Skills.HISTORY",
                "prof": "HistoryProf",
                "mod": "HistoryMod",
                "bonus": "History"
            },
            "Skills.INSIGHT": {
                "name": "Skills.INSIGHT",
                "prof": "InsightProf",
                "mod": "InsightMod",
                "bonus": "Insight"
            },
            "Skills.INTIMIDATION": {
                "name": "Skills.INTIMIDATION",
                "prof": "IntimidationProf",
                "mod": "IntimidationMod",
                "bonus": "Intimidation"
            },
            "Skills.INVESTIGATION": {
                "name": "Skills.INVESTIGATION",
                "prof": "InvestigationProf",
                "mod": "InvestigationMod",
                "bonus": "Investigation"
            },
            "Skills.MEDICINE": {
                "name": "Skills.MEDICINE",
                "prof": "MedicineProf",
                "mod": "MedicineMod",
                "bonus": "Medicine"
            },
            "Skills.NATURE": {
                "name": "Skills.NATURE",
                "prof": "NatureProf",
                "mod": "NatureMod",
                "bonus": "Nature"
            },
            "Skills.PERCEPTION": {
                "name": "Skills.PERCEPTION",
                "prof": "PerceptionProf",
                "mod": "PerceptionMod",
                "bonus": "Perception"
            },
            "Skills.PERFORMANCE": {
                "name": "Skills.PERFORMANCE",
                "prof": "PerformanceProf",
                "mod": "PerformanceMod",
                "bonus": "Performance"
            },
            "Skills.PERSUASION": {
                "name": "Skills.PERSUASION",
                "prof": "PersuasionProf",
                "mod": "PersuasionMod",
                "bonus": "Persuasion"
            },
            "Skills.RELIGION": {
                "name": "Skills.RELIGION",
                "prof": "ReligionProf",
                "mod": "ReligionMod",
                "bonus": "Religion"
            },
            "Skills.SLEIGHTOFHAND": {
                "name": "Skills.SLEIGHTOFHAND",
                "prof": "SleightOfHandProf",
                "mod": "SleightofHandMod",
                "bonus": "SleightofHand"
            },
            "Skills.STEALTH": {
                "name": "Skills.STEALTH",
                "prof": "StealthProf",
                "mod": "StealthMod",
                "bonus": "Stealth "
            },
            "Skills.SURVIVAL": {
                "name": "Skills.SURVIVAL",
                "prof": "SurvivalProf",
                "mod": "SurvivalMod",
                "bonus": "Survival"
            },
            "CustomSkill1": {
                "name": "Skills.CUSTOM1",
                "prof": "CustomProf1",
                "mod": "Custom Skill Bonus 1",
                "bonus": "CustomSkill1"
            },
            "CustomSkill2": {
                "name": "Skills.CUSTOM2",
                "prof": "CustomProf2",
                "mod": "Custom Skill Bonus 2",
                "bonus": "CustomSkill2"
            },
            "CustomSkill3": {
                "name": "Skills.CUSTOM3",
                "prof": "CustomProf3",
                "mod": "Custom Skill Bonus 3",
                "bonus": "CustomSkill3"
            }
        }
    }
    override = {
        "=== 1st LEVEL ===": 1,
        "=== 2nd LEVEL ===": 2,
        "=== 3rd LEVEL ===": 3,
        "=== 4th LEVEL ===": 4,
        "=== 5th LEVEL ===": 5,
        "=== 6th LEVEL ===": 6,
        "=== 7th LEVEL ===": 7,
        "=== 8th LEVEL ===": 8,
        "1 Slots O": 1,
        "2 Slots OO": 2,
        "3 Slots OOO": 3,
        "4 Slots OOOO": 4,
        "5 Slots OOOOO": 5,
        "6 Slots OOOOOO": 6,
        "7 Slots OOOOOOO": 7
    }
    pre_processing = {
        "PP_NOTES": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "AdditionalNotes1",
                    "AdditionalNotes2"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "PP_ACTIONS": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "Actions1",
                    "Actions2"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "PP_FEATURES": {
            "method": "concat",
            "parameters": {
                "forms_to_concat": [
                    "FeaturesTraits1",
                    "FeaturesTraits2",
                    "FeaturesTraits3",
                    "FeaturesTraits4",
                    "FeaturesTraits5",
                    "FeaturesTraits6"
                ],
                "separator": " "
            },
            "delete_parameters": True
        },
        "StrProf": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "DexProf": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "ConProf": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "IntProf": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "WisProf": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        },
        "ChaProf": {
            "method": "to_bool_true_if",
            "parameters": {
                "value": True
            }
        }
    }

    def __init__(self):
        super(DNDBeyond, self).__init__()
