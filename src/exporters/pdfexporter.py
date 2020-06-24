import csv
import logging
import os

from PySide2.QtCore import QStandardPaths
from fitz import fitz

from exceptions import InvalidFieldException
from src.models.characterenums import SkillProficiencies
from src.models.charactermodel import CH
from src.models.charactersubmodel import Attack, Spell

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

    "Front_Racial Traits": "CH.FEATURES_TRAITS",
    "Front_Light Armour": None,
    "Front_Medium Armour": None,
    "Front_Heavy Armour": None,
    "Front_Simple Weapons": None,
    "Front_Martial Weapons": None,
    "Front_Shields": None,
    "Front_Languages": "CH.PROFICIENCIES_LANGUAGES",
    "Front_Tools": None,
    "Front_AC": "CH.AC",
    "Front_Shield Bonus": None,
    "Front_Initiative": "CH.INITIATIVE",
    "Front_Speed": "CH.SPEED",
    "Front_Max HP": "CH.MAX_HP",
    "Front_Current HP": "CH.CURRENT_HP",
    "Front_Temp HP": "CH.TEMP_HP",
    "Front_Used Hit Dice": "CH.HIT_DICE",
    "Front_Total Hit Dice": "CH.TOTAL_HIT_DICE",
    "Front_Success 1": "CH.SUCCESSFUL_SAVE_1",
    "Front_Success 2": "CH.SUCCESSFUL_SAVE_2",
    "Front_Success 3": "CH.SUCCESSFUL_SAVE_3",
    "Front_Fail 1": "CH.FAILED_SAVE_1",
    "Front_Fail 2": "CH.FAILED_SAVE_2",
    "Front_Fail 3": "CH.FAILED_SAVE_3",

    "Front_Spell Atk": "CH.SPELLATKBONUS0",
    "Front_Spell DC": "CH.SPELLSAVEDC0",
    "Front_Spell Slots Used": None,
    "Front_Spell Slots Total": None,
    "Front_Spell Slots Level": None,

}

weapon_list_keys = {
    "column_to_form": {
        "Name": [
            "Front_Weapon Name {}"
        ],
        "Attack": [
            "Front_Weapon Atk Bonus {}"
        ],
        "Damage": [
            "Front_Weapon Damage {}"
        ]
    },
    "max_items": 4,
    "zero_indexed": True,
    "hardcoded_keys": {}
}

spell_list_keys = {
    "column_to_form": {
        "Prepared": [
            "Front_Spell Concentration {}"
        ],
        "Spell Name": [
            "Front_Spell Attack Name {}"
        ],
        "Notes": ["Front_Spell Effect {}"],
        "Save/Attack": ["Front_Spell Save {}"],
        "Duration": ["Front_Spell Casting Time {}"],
        "Range": ["Front_Spell Range {}"],
    },
    "max_items": 4,
    "zero_indexed": True,
    "hardcoded_keys": {
    }
}

skill_keys = {
    "Skills.ACROBATICS": {
        "expertise_field": "Front_Expertise Acrobatics",
        "proficiency_field": "Front_Proficiency Acrobatics",
        "modifier_field": "Front_Skill Acrobatics",
    },
    "Skills.ANIMALHANDLING": {
        "expertise_field": "Front_Expertise Animal Handling",
        "proficiency_field": "Front_Proficiency Animal Handling",
        "modifier_field": "Front_Skill Animal Handling",
    },
    "Skills.ARCANA": {
        "expertise_field": "Front_Expertise Arcana",
        "proficiency_field": "Front_Proficiency Arcana",
        "modifier_field": "Front_Skill Arcana",
    },
    "Skills.ATHLETICS": {
        "expertise_field": "Front_Expertise Athletics",
        "proficiency_field": "Front_Proficiency Athletics",
        "modifier_field": "Front_Skill Athletics",
    },
    "Skills.DECEPTION": {
        "expertise_field": "Front_Expertise Deception",
        "proficiency_field": "Front_Proficiency Deception",
        "modifier_field": "Front_Skill Deception",
    },
    "Skills.HISTORY": {
        "expertise_field": "Front_Expertise History",
        "proficiency_field": "Front_Proficiency History",
        "modifier_field": "Front_Skill History",
    },
    "Skills.INSIGHT": {
        "expertise_field": "Front_Expertise Insight",
        "proficiency_field": "Front_Proficiency Insight",
        "modifier_field": "Front_Skill Insight",
    },
    "Skills.INTIMIDATION": {
        "expertise_field": "Front_Expertise Intimidation",
        "proficiency_field": "Front_Proficiency Intimidation",
        "modifier_field": "Front_Skill Intimidation",
    },
    "Skills.INVESTIGATION": {
        "expertise_field": "Front_Expertise Investigation",
        "proficiency_field": "Front_Proficiency Investigation",
        "modifier_field": "Front_Skill Investigation",
    },
    "Skills.MEDICINE": {
        "expertise_field": "Front_Expertise Medicine",
        "proficiency_field": "Front_Proficiency Medicine",
        "modifier_field": "Front_Skill Medicine",
    },
    "Skills.NATURE": {
        "expertise_field": "Front_Expertise Nature",
        "proficiency_field": "Front_Proficiency Nature",
        "modifier_field": "Front_Skill Nature",
    },
    "Skills.PERCEPTION": {
        "expertise_field": "Front_Expertise Perception",
        "proficiency_field": "Front_Proficiency Perception",
        "modifier_field": "Front_Skill Perception",
    },
    "Skills.PERFORMANCE": {
        "expertise_field": "Front_Expertise Performance",
        "proficiency_field": "Front_Proficiency Performance",
        "modifier_field": "Front_Skill Performance",
    },
    "Skills.PERSUASION": {
        "expertise_field": "Front_Expertise Persuasion",
        "proficiency_field": "Front_Proficiency Persuasion",
        "modifier_field": "Front_Skill Persuasion",
    },
    "Skills.RELIGION": {
        "expertise_field": "Front_Expertise Religion",
        "proficiency_field": "Front_Proficiency Religion",
        "modifier_field": "Front_Skill Religion",
    },
    "Skills.SLEIGHTOFHAND": {
        "expertise_field": "Front_Expertise Sleight of Hand",
        "proficiency_field": "Front_Proficiency Sleight of Hand",
        "modifier_field": "Front_Skill Sleight of Hand",
    },
    "Skills.STEALTH": {
        "expertise_field": "Front_Expertise Stealth",
        "proficiency_field": "Front_Proficiency Stealth",
        "modifier_field": "Front_Skill Stealth",
    },
    "Skills.SURVIVAL": {
        "expertise_field": "Front_Expertise Survival",
        "proficiency_field": "Front_Proficiency Survival",
        "modifier_field": "Front_Skill Survival",
    }
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
        if field_to_set is None:
            logging.error(f"Attempting to set None field with value {value}")
            raise InvalidFieldException(f"Attempting to set None field with value {value}")

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

    def export_skills(self, forms, skill_keys):
        for skill in skill_keys:
            this_skill = self.player_controller.get_skill(skill)
            this_skill_half = skill_keys[skill].get("half_field", None)
            this_skill_prof = skill_keys[skill].get("proficiency_field", None)
            this_skill_expertise = skill_keys[skill].get("expertise_field", None)
            this_skill_mod = skill_keys[skill].get("modifier_field", None)
            mod_field = forms.get(this_skill_mod, None)
            self.set_field(mod_field, this_skill.bonus)

            field = None
            if this_skill.prof == SkillProficiencies.Prof:
                field = forms.get(this_skill_prof, None)
            elif this_skill.prof == SkillProficiencies.Eff:
                field = forms.get(this_skill_expertise, None)
            elif this_skill.prof == SkillProficiencies.Half:
                field = forms.get(this_skill_half, None)

            if field is not None:
                self.set_field(field, True)

        return forms

    def set_item_fields(self, item, fields_to_map, forms_to_fill, forms, index):
        for value, form in forms_to_fill.items():
            for column_index, value_name in fields_to_map.items():
                if value_name == value:
                    form_nominee = None
                    for form_candidate in form:
                        form_candidate = form_candidate.format(index)
                        if form_candidate in forms:
                            form_nominee = forms[form_candidate]
                            break

                    self.set_field(form_nominee, item.get_column(column_index))
        return forms

    def export_custom_table(self, item_class, forms, keys):
        max_items = keys["max_items"]
        zero_indexed = keys["zero_indexed"]

        fields_to_map = item_class.columns_names
        forms_to_fill = keys["column_to_form"]

        for i in range(max_items):
            if zero_indexed:
                i += 1

            item = self.player_controller.get_item(item_class, i)
            if item is not None:
                self.set_item_fields(item, fields_to_map, forms_to_fill, forms, i)
        return forms

    def export(self):
        dir_to_search = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        dir_to_search = os.path.join(dir_to_search, "exporters")
        file_to_export_to = os.path.join(
            dir_to_search, "Character Sheet_WARLOCK_FILLABLE.pdf"
        )

        forms = {}
        doc = fitz.open(file_to_export_to)
        for page_number in range(doc.pageCount):
            page = doc.loadPage(page_number)
            for field in page.widgets():
                forms[field.field_name] = field

        form_fields_convertable = [field for field_name, field in forms.items() if field_name in conversion_key.keys()]
        for field in form_fields_convertable:
            ch_candidate = conversion_key[field.field_name]
            if not ch_candidate in CH._value2member_map_:
                logger.info(f"Value {ch_candidate} is not a valid CH")
                continue
            ch = CH(ch_candidate)
            value = getattr(
                self.player_controller.player_model, ch.name
            )
            self.set_field(field, value)
            forms.pop(field.field_name)

        forms = self.export_skills(forms, skill_keys)
        forms = self.export_custom_table(Attack, forms, weapon_list_keys)
        forms = self.export_custom_table(Spell, forms, spell_list_keys)

        doc.save("test.pdf")

        with open("dict_out.csv", "w", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in forms.items():
                writer.writerow([key, value])
