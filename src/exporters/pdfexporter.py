import csv
import logging
import os

from PySide2.QtCore import QStandardPaths
from fitz import fitz

from src.models.charactermodel import CH

logger = logging.getLogger(__name__)

conversion_key = {
    "Front_Character Name": "CH.CHARACTER_NAME",
    "Front_Race": "CH.CHARACTER_NAME",
    "Front_Background": "CH.BACKGROUND",
    "Front_Alignment": "CH.ALIGNMENT",
    "Front_XP": "CH.XP",
    "Front_Level": "CH.CLASS_LEVEL",
    "Front_Proficiency": "CH.PROF_BONUS",
    "Front_Passive Perception": "CH.PASSIVE_PERCEPTION",
    "Front_Inspiration": "CH.INITIATIVE",
    "Front_Passive Insight": "CH.PASSIVE_INVESTIGATION",
    "Front_Str Mod": "CH.STR_MOD",
    "Front_Str Score": "CH.STR",
    "Front_Dex Mod": "CH.DEX_MOD",
    "Front_Dex Score": "CH.DEX",
    "Front_Con Mod": "CH.CON_MOD",
    "Front_Con Score": "CH.CON",
    "Front_Int Mod": "CH.INT_MOD",
    "Front_Int Score": "CH.INT",
    "Front_Wis Mod": "CH.WIS_MOD",
    "Front_Wis Score": "CH.WIS",
    "Front_Cha Mod": "CH.CHA_MOD",
    "Front_Cha Score": "CH.CHA",

    "Front_Save Str": "CH.STR_ST_PROF",
    "Front_Str Save Throw": "CH.STR_ST_MOD",
    "Front_Save Dex": "CH.DEX_ST_PROF",
    "Front_Dex Save Throw": "CH.DEX_ST_MOD",

    "Front_Save Con": "CH.CON_ST_PROF",
    "Front_Con Save Throw": "CH.CON_ST_MOD",

    "Front_Save Int": "CH.INT_ST_PROF",
    "Front_Int Save Throw": "CH.INT_ST_MOD",

    "Front_Save Wis": "CH.WIS_ST_PROF",
    "Front_Wis Save Throw": "CH.WIS_ST_MOD",

    "Front_Save Cha": "CH.CHA_ST_PROF",
    "Front_Cha Save Throw": "CH.CHA_ST_MOD",

    "Front_Archetype,Battlemaste": None,

    "Front_Expertise Athletics": None,
    "Front_Proficiency Athletics": None,
    "Front_Skill Athletics": None,

    "Front_Expertise Acrobatics": None,
    "Front_Proficiency Acrobatics": None,
    "Front_Skill Acrobatics": None,

    "Front_Expertise Sleight of Hand": None,
    "Front_Proficiency Sleight of Hand": None,
    "Front_Skill Sleight of Hand": None,

    "Front_Expertise Stealth": None,
    "Front_Proficiency Stealth": None,
    "Front_Skill Stealth": None,

    "Front_Expertise Arcana": None,
    "Front_Proficiency Arcana": None,
    "Front_Skill Arcana": None,

    "Front_Expertise History": None,
    "Front_Proficiency History": None,
    "Front_Skill History": None,

    "Front_Expertise Investigation": None,
    "Front_Proficiency Investigation": None,
    "Front_Skill Investigation": None,

    "Front_Expertise Nature": None,
    "Front_Proficiency Nature": None,
    "Front_Skill Nature": None,

    "Front_Expertise Religion": None,
    "Front_Proficiency Religion": None,
    "Front_Skill Religion": None,

    "Front_Expertise Animal Handling": None,
    "Front_Proficiency Animal Handling": None,
    "Front_Skill Animal Handling": None,

    "Front_Expertise Insight": None,
    "Front_Proficiency Insight": None,
    "Front_Skill Insight": None,

    "Front_Expertise Medicine": None,
    "Front_Proficiency Medicine": None,
    "Front_Skill Medicine": None,

    "Front_Expertise Perception": None,
    "Front_Proficiency Perception": None,
    "Front_Skill Perception": None,

    "Front_Expertise Survival": None,
    "Front_Proficiency Survival": None,
    "Front_Skill Survival": None,

    "Front_Expertise Deception": None,
    "Front_Proficiency Deception": None,
    "Front_Skill Deception": None,

    "Front_Expertise Intimidation": None,
    "Front_Proficiency Intimidation": None,
    "Front_Skill Intimidation": None,

    "Front_Expertise Performance": None,
    "Front_Proficiency Performance": None,
    "Front_Skill Performance": None,

    "Front_Expertise Persuasion": None,
    "Front_Proficiency Persuasion": None,
    "Front_Skill Persuasion": None,

    "Front_Racial Traits": None,
    "Front_Light Armour": None,
    "Front_Medium Armour": None,
    "Front_Heavy Armour": None,
    "Front_Simple Weapons": None,
    "Front_Martial Weapons": None,
    "Front_Shields": None,
    "Front_Languages": None,
    "Front_Tools": None,
    "Front_AC": "CH.AC",
    "Front_Shield Bonus": None,
    "Front_Initiative": "CH.INITIATIVE",
    "Front_Speed": "CH.SPEED",
    "Front_Max HP": "CH.MAX_HP",
    "Front_Current HP": None,
    "Front_Temp HP": None,
    "Front_Used Hit Dice": None,
    "Front_Total Hit Dice": None,
    "Front_Success 1": None,
    "Front_Success 2": None,
    "Front_Success 3": None,
    "Front_Fail 1": None,
    "Front_Fail 2": None,
    "Front_Fail 3": None,
    "Front_Weapon Name 1": None,
    "Front_Weapon Atk Bonus 1": None,
    "Front_Weapon Damage 1": None,
    "Front_Weapon Name 2": None,
    "Front_Weapon Atk Bonus 2": None,
    "Front_Weapon Damage 2": None,
    "Front_Weapon Name 3": None,
    "Front_Weapon Atk Bonus 3": None,
    "Front_Weapon Damage 3": None,
    "Front_Weapon Name 4": None,
    "Front_Weapon Atk Bonus 4": None,
    "Front_Weapon Damage 4": None,
    "Front_Action Surge": None,
    "Front_Extra Attack": None,
    "Front_Indomitable": None,
    "Front_Superiority Used": None,
    "Front_Superiority Total": None,
    "Front_Superiority Die": None,
    "Front_Additional Combat Features": None,
    "Front_Fighting Style": None,
    "Front_Martial Archetype 3": None,
    "Front_Martial Archetype 7": None,
    "Front_Martial Archetype 10": None,
    "Front_Martial Archetype 15": None,
    "Front_Martial Archetype 18": None,
    "Front_Maneuver DC": None,
    "Front_Spell Atk": "CH.",
    "Front_Spell DC": "CH.",
    "Front_Spell Slots Used": "CH.",
    "Front_Spell Slots Total": "CH.",
    "Front_Spell Slots Level": "CH.",
    "Front_Spell Attack Name 1": "CH.",
    "Front_Spell Range 1": "CH.",
    "Front_Spell Casting Time 1": "CH.",
    "Front_Spell Save 1": "CH.",
    "Front_Spell Effect 1": "CH.",
    "Front_Spell Concentration 1": "CH.",
    "Front_Spell Attack Name 2": "CH.",
    "Front_Spell Range 2": "CH.",
    "Front_Spell Casting Time 2": "CH.",
    "Front_Spell Save 2": "CH.",
    "Front_Spell Effect 2": "CH.",
    "Front_Spell Concentration 2": "CH.",
    "Front_Spell Attack Name 3": "CH.",
    "Front_Spell Range 3": "CH.",
    "Front_Spell Casting Time 3": "CH.",
    "Front_Spell Save 3": "CH.",
    "Front_Spell Effect 3": "CH.",
    "Front_Spell Concentration 3": "CH.",
    "Front_Spell Attack Name 4": "CH.",
    "Front_Spell Range 4": "CH.",
    "Front_Spell Casting Time 4": "CH.",
    "Front_Spell Save 4": "CH.",
    "Front_Spell Effect 4": "CH.",
    "Front_Spell Concentration 4": "CH.",
    "Front_Spell Level 1": "CH.",
    "Front_Spell Ritual 1": "CH.",
    "Front_Spell Name 1": "CH.",
    "Front_Spell Level 2": "CH.",
    "Front_Spell Ritual 2": "CH.",
    "Front_Spell Name 2": "CH.",
    "Front_Spell Level 3": "CH.",
    "Front_Spell Ritual 3": "CH.",
    "Front_Spell Name 3": "CH.",
    "Front_Spell Level 4": "CH.",
    "Front_Spell Ritual 4": "CH.",
    "Front_Spell Name 4": "CH.",
    "Front_Spell Level 5": "CH.",
    "Front_Spell Ritual 5": "CH.",
    "Front_Spell Name 5": "CH.",
    "Front_Spell Level 6": "CH.",
    "Front_Spell Ritual 6": "CH.",
    "Front_Spell Name 6": "CH.",
    "Front_Spell Level 7": "CH.",
    "Front_Spell Ritual 7": "CH.",
    "Front_Spell Name 7": "CH.",
    "Front_Spell Level 8": "CH.",
    "Front_Spell Ritual 8": "CH.",
    "Front_Spell Name 8": "CH.",
    "Front_Spell Level 9": "CH.",
    "Front_Spell Ritual 9": "CH.",
    "Front_Spell Name 9": "CH.",
    "Front_Spell Level 10": "CH.",
    "Front_Spell Ritual 10": "CH.",
    "Front_Spell Name 10": "CH.",
    "Front_Spell Level 11": "CH.",
    "Front_Spell Ritual 11": "CH.",
    "Front_Spell Name 11": "CH.",
    "Front_Spell Level 12": "CH.",
    "Front_Spell Ritual 12": "CH.",
    "Front_Spell Name 12": "CH.",
    "Front_Spell Level 13": "CH.",
    "Front_Spell Ritual 13": "CH.",
    "Front_Spell Name 13": "CH.",
    "Front_Spell Level 14": "CH.",
    "Front_Spell Ritual 14": "CH.",
    "Front_Spell Name 14": "CH.",
    "Front_Spell Level 15": "CH.",
    "Front_Spell Ritual 15": "CH.",
    "Front_Spell Name 15": "CH.",
    "Front_Spell Level 16": "CH.",
    "Front_Spell Ritual 16": "CH.",
    "Front_Spell Name 16": "CH.",
    "Front_Spell Level 17": "CH.",
    "Front_Spell Ritual 17": "CH.",
    "Front_Spell Name 17": "CH.",
    "Front_Spell Level 18": "CH.",
    "Front_Spell Ritual 18": "CH.",
    "Front_Spell Name 18": "CH.",
    "Front_Spell Level 19": "CH.",
    "Front_Spell Ritual 19": "CH.",
    "Front_Spell Name 19": "CH.",
    "Front_Spell Level 20": "CH.",
    "Front_Spell Ritual 20": "CH.",
    "Front_Spell Name 20": "CH.",
    "Front_Spell Level 21": "CH.",
    "Front_Spell Ritual 21": "CH.",
    "Front_Spell Name 21": "CH.",
    "Front_Spell Level 22": "CH.",
    "Front_Spell Ritual 22": "CH.",
    "Front_Spell Name 22": "CH.",
    "Front_Spell Level 23": "CH.",
    "Front_Spell Ritual 23": "CH.",
    "Front_Spell Name 23": "CH.",
    "Front_Spell Level 24": "CH.",
    "Front_Spell Ritual 24": "CH.",
    "Front_Spell Name 24": "CH.",
    "Front_Spell Level 25": "CH.",
    "Front_Spell Ritual 25": "CH.",
    "Front_Spell Name 25": "CH.",
    "Front_Spell Level 26": "CH.",
    "Front_Spell Ritual 26": "CH.",
    "Front_Spell Name 26": "CH.",
    "Front_Spell Level 27": "CH.",
    "Front_Spell Ritual 27": "CH.",
    "Front_Spell Name 27": "CH.",
    "Front_Spell Level 28": "CH.",
    "Front_Spell Ritual 28": "CH.",
    "Front_Spell Name 28": "CH.",
    "Front_Spell Level 29": "CH.",
    "Front_Spell Ritual 29": "CH.",
    "Front_Spell Name 29": "CH.",
    "Front_Spell Level 30": "CH.",
    "Front_Spell Ritual 30": "CH.",
    "Front_Spell Name 30": "CH.",
    "Front_Spell Level 31": "CH.",
    "Front_Spell Ritual 31": "CH.",
    "Front_Spell Name 31": "CH.",
    "Front_Spell Level 32": "CH.",
    "Front_Spell Ritual 32": "CH.",
    "Front_Spell Name 32": "CH.",

}


class PDFExporter:
    def __init__(self, player_controller):
        self.player_controller = player_controller

    def get_field_type(self, field):
        if field.field_type_string == 'Text':
            return str
        elif field.field_type_string == 'CheckBox':
            return bool

    def set_field(self, field_to_set, value):
        value_type = type(value)
        field_type = self.get_field_type(field_to_set)
        if value_type is int and field_type is str:
            value = str(value)
        elif value_type is bool:
            value = bool(value)
        elif value_type is not field_type:  # Int values need to be casted to str as well, but fail this clause
            logging.warning(f"Setting value with type {value_type} to field with type {field_type}")
            value = str(value)

        field_to_set.field_value = value
        field_to_set.update()

    def export(self):
        dir_to_search = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        dir_to_search = os.path.join(dir_to_search, "exporters")
        file_to_export_to = os.path.join(
            dir_to_search, "Character Sheet_WARLOCK_FILLABLE.pdf"
        )

        form_fields = {}
        doc = fitz.open(file_to_export_to)
        for page_number in range(doc.pageCount):
            page = doc.loadPage(page_number)
            for field in page.widgets():
                if field.field_name in conversion_key.keys():
                    ch_candidate = conversion_key[field.field_name]
                    if not ch_candidate in CH._value2member_map_:
                        logger.info(f"Value {ch_candidate} is not a valid CH")
                        continue
                    ch = CH(ch_candidate)
                    value = getattr(
                        self.player_controller.player_model, ch.name
                    )
                    self.set_field(field, value)
                else:
                    form_fields[field.field_name] = field.field_value

        doc.save("test.pdf")

        with open("dict_out.csv", "w", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in form_fields.items():
                writer.writerow([key, value])
