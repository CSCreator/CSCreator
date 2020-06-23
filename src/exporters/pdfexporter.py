import csv
import logging
import os

from PySide2.QtCore import QStandardPaths
from fitz import fitz

from exceptions import InvalidFieldException
from src.models.characterenums import SkillProficiencies
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

weapon_list_keys = {
      "name":[
         "Front_Weapon Name {}"
      ],
      "attack_bonus":[
         "Front_Weapon Atk Bonus {}"
      ],
      "damage":[
         "Front_Weapon Damage {}"
      ],
      "max_items":4,
      "zero_indexed":False,
      "hardcoded_keys":{}
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

    def export_weapons(self, forms, weapon_keys):
        max_weapons = weapon_keys["max_items"]
        zero_indexed = weapon_keys["max_items"]
        name_string = weapon_keys["name"][0]
        attack_bonus_string = weapon_keys["attack_bonus"][0]
        damage_string = weapon_keys["damage"][0]
        for i in range(max_weapons):
            if zero_indexed:
                i+=1
            attack = self.player_controller.get_attack(i)
            if attack is None:
                continue

            name_form = forms.get(name_string.format(i), None)
            attack_form = forms.get(attack_bonus_string.format(i), None)
            damage_form = forms.get(damage_string.format(i), None)

            self.set_field(name_form, attack.name)
            self.set_field(attack_form, attack.attack)
            self.set_field(damage_form, attack.damage)

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
        forms = self.export_weapons(forms, weapon_list_keys)

        doc.save("test.pdf")

        with open("dict_out.csv", "w", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in forms.items():
                writer.writerow([key, value])
