import json
import logging

from src.controllers.charactercontroller import CharacterController
from exceptions import NotAllImportedWarning, ValueEnumKeyNotFoundException, DefinitionFileUnreadableException
from src.importers.preprocessing_functions import concat, to_boolean_true_if
from src.models.charactermodel import CH
from src.models.characterenums import SkillProficiencies
from src.pdf.pdfutils import get_forms_from_pdf

logger = logging.getLogger(__name__)


def find_candidate_key(key_patterns, format, dict_to_search, hardcoded_keys):
    for pattern in key_patterns:
        formatted_key_pattern = pattern.format(format)
        if formatted_key_pattern in hardcoded_keys:
            return hardcoded_keys[formatted_key_pattern]

        for key in dict_to_search.keys():
            if formatted_key_pattern in key:
                return key

    return False

def get_rows_per_header(list_keys, forms):
    form_keys_with_last_header_value = {}

    header_name = list_keys["header"]
    last_header_value = None

    for form_key in forms:
        if header_name in form_key:
            last_header_value = forms[form_key]
            continue

        if last_header_value is None:
            continue

        form_keys_with_last_header_value[form_key] = last_header_value

    return form_keys_with_last_header_value

def parse_list(list_keys, keys_to_parse, forms):


    header_present = "header" in list_keys.keys()
    if header_present:
        form_keys_with_last_header_value = get_rows_per_header(list_keys, forms)

    items = []
    for i in range(list_keys["max_items"]):
        if not list_keys["zero_indexed"]:
            i += 1
        candidate_keys = [
            find_candidate_key(key, i, forms, list_keys["hardcoded_keys"])
            for key in keys_to_parse
        ]

        keys_not_found = [key == False for key in candidate_keys]
        if any(keys_not_found) and not all(keys_not_found):
            logging.warning(
                f"Candidate_keys has some values set, and some False {candidate_keys}"
            )

        item = [forms.get(candidate_key, None) for candidate_key in candidate_keys]

        if header_present:
            item.append(form_keys_with_last_header_value.get(candidate_keys[0], None))

        if any(value for value in item):
            items.append(item)

        for candidate_key in candidate_keys:
            forms.pop(candidate_key, None)

    return items, forms

class PDFImporter:
    def __init__(self, definition_file):
        # super(DNDBeyondImporter, self).__init__()
        self.player = CharacterController()
        self.load_definition(definition_file=definition_file)

    def load_definition(self, definition_file):
        try:
            with open(definition_file, "r") as j:
                definition = json.loads(j.read())
        except IOError:
            raise DefinitionFileUnreadableException(f"Definition file {definition_file} cannot be read or found")

        self.experimental = definition.get("experimental", False)
        self.key_conversion = definition.get("key_conversion", None)
        self.keys_to_ignore = definition.get("keys_to_ignore", None)
        self.wildcards_to_ignore = definition.get("wildcards_to_ignore", None)
        self.pre_processing = definition.get("pre_processing", None)
        self.proficiency_values = definition.get("proficiency_values", None)
        self.skill_keys = definition.get("skill_keys", None)
        self.weapon_list_keys = definition.get("weapon_list_keys", None)
        self.equipment_list_keys = definition.get("equipment_list_keys", None)
        self.attuned_equipment_list_keys = definition.get(
            "attuned_equipment_list_keys", None
        )
        self.spell_list_keys = definition.get("spell_list_keys", None)
        self.spellslot_list_keys = definition.get("spellslot_list_keys", None)

        values = tuple(item.value for item in CH)

        def string_to_enum(dict_to_parse):
            for key, value in dict_to_parse.items():
                if value in values:
                    try:
                        enum_value = CH(value)
                        dict_to_parse[key] = enum_value
                    except Exception:
                        pass
                else:
                    logging.error(f"Value {value} is not a known CH. Enum")

        string_to_enum(self.key_conversion)

    def set_value_to_player_if_exists(self, form_fields, key):
        ch = self.key_conversion[key]
        value = form_fields[key]
        form_fields.pop(key, None)
        if not ch:
            return
        if isinstance(ch, str):
            logging.error(
                f"Attempting to set attribute {ch} which is not a CH value"
            )
            return
        if not hasattr(self.player.player_model, ch.name):
            logging.error(
                f"Attempting to set attribute {ch.name} which does not exist in PlayerModel"
            )
            return

        self.player.player_model.set_value(ch.name, value)

    def load(self, file):

        form_fields = get_forms_from_pdf(file)

        form_fields = self.apply_preprocessing(form_fields)
        form_fields = self.handle_ability_order(form_fields)

        for key in list(form_fields.keys()):
            if key in self.key_conversion:
                self.set_value_to_player_if_exists(form_fields, key)
            elif (
                any(wildcard in key for wildcard in self.wildcards_to_ignore)
                or key in self.keys_to_ignore
            ):
                form_fields.pop(key, None)

        form_fields = self.add_skills(form_fields)
        form_fields = self.add_equipment(form_fields)
        form_fields = self.add_weapons(form_fields)
        form_fields = self.add_spells(form_fields)
        form_fields = self.add_spellslots(form_fields)

        if len(form_fields) > 0:
            logging.warning(form_fields)
            if not self.experimental:
                raise NotAllImportedWarning(f"Not all dict values have been parsed! {form_fields}")

    def handle_ability_order(self, forms):
        def return_score_then_prof(score, prof):
            if "-" in score or "+" in score:
                # This is actually the proficiency bonus
                score, prof = prof, score
            return score, prof

        def get_key_from_value(value):
            return list(self.key_conversion.keys())[
                list(self.key_conversion.values()).index(value)
            ]

        str_value = get_key_from_value(CH.STR)
        dex_value = get_key_from_value(CH.DEX)
        con_value = get_key_from_value(CH.CON)
        int_value = get_key_from_value(CH.INT)
        wis_value = get_key_from_value(CH.WIS)
        cha_value = get_key_from_value(CH.CHA)
        str_mod = get_key_from_value(CH.STR_MOD)
        dex_mod = get_key_from_value(CH.DEX_MOD)
        con_mod = get_key_from_value(CH.CON_MOD)
        int_mod = get_key_from_value(CH.INT_MOD)
        wis_mod = get_key_from_value(CH.WIS_MOD)
        cha_mod = get_key_from_value(CH.CHA_MOD)

        for pair in [
            (str_value, str_mod),
            (dex_value, dex_mod),
            (con_value, con_mod),
            (int_value, int_mod),
            (wis_value, wis_mod),
            (cha_value, cha_mod),
        ]:
            forms[pair[0]], forms[pair[1]] = return_score_then_prof(
                forms[pair[0]], forms[pair[1]]
            )
        return forms

    def apply_preprocessing(self, forms):
        for new_field, process in self.pre_processing.items():
            logger.debug(
                f"Preprocessing method {process} to create new field {new_field}"
            )
            method = process["method"]
            parameters = process["parameters"]
            delete_after = (
                process["delete_parameters"]
                if "delete_parameters" in process.keys()
                else False
            )
            new_value = ""

            if method == "concat":
                new_value = concat(forms,parameters)
            if method == "to_bool_true_if":
                if not "field" in parameters:
                    parameters["field"] = new_field
                new_value = to_boolean_true_if(forms, parameters)

            forms[new_field] = new_value

            if delete_after:
                for parameter in parameters:
                    forms.pop(parameter, None)
        return forms

    def add_equipment(self, forms):
        items, forms = parse_list(
            self.equipment_list_keys,
            [
                self.equipment_list_keys["name"],
                self.equipment_list_keys["quantity"],
                self.equipment_list_keys["weight"],
            ],
            forms,
        )

        for item in items:
            self.player.add_equipment(item[0], item[1], item[2], False)

        items, forms = parse_list(
            self.attuned_equipment_list_keys,
            [
                self.attuned_equipment_list_keys["name"],
                self.attuned_equipment_list_keys["quantity"],
                self.attuned_equipment_list_keys["weight"],
            ],
            forms,
        )

        for item in items:
            self.player.add_equipment(item[0], item[1], item[2], True)

        return forms

    def add_skills(self, info):
        def prof_string_to_enum(prof_string):
            value_to_enum = {
                "prof_none": SkillProficiencies.No,
                "prof_half": SkillProficiencies.Half,
                "prof_proficient": SkillProficiencies.Prof,
                "prof_expertise": SkillProficiencies.Eff,
            }
            if self.proficiency_values is None:
                value_enum = SkillProficiencies.No
                if prof_string == "True":
                    value_enum = SkillProficiencies.Prof

            elif prof_string in self.proficiency_values.keys():
                value = self.proficiency_values[prof_string]
                if value not in value_to_enum.keys():
                    raise ValueEnumKeyNotFoundException(
                        f"Unknown value {value}, not found in value_to_enum {value_to_enum}"
                    )
                value_enum = value_to_enum[value]
            else:
                raise ValueEnumKeyNotFoundException("Unknown Proficiency string {}".format(prof_string))
            return value_enum

        for name in self.skill_keys:
            proficiency_field = self.skill_keys[name]["proficiency_field"]
            modifier_field = self.skill_keys[name]["modifier_field"]
            bonus_field = self.skill_keys[name]["bonus_field"]
            proficiency = prof_string_to_enum(info[proficiency_field])
            self.player.add_skill(
                proficiency, info[modifier_field], info[bonus_field], name
            )
            info.pop(modifier_field, None)
            info.pop(bonus_field, None)
            info.pop(proficiency_field, None)

        return info

    def add_weapons(self, forms):
        items, forms = parse_list(
            self.weapon_list_keys,
            [
                self.weapon_list_keys["name"],
                self.weapon_list_keys["attack_bonus"],
                self.weapon_list_keys["damage"],
                self.weapon_list_keys["notes"],
            ],
            forms,
        )

        for item in items:
            self.player.add_attack(item[0], item[1], item[2], item[3])

        return forms

    def add_spells(self, forms):
        items, forms = parse_list(
            self.spell_list_keys,
            [
                self.spell_list_keys["prepared"],
                self.spell_list_keys["name"],
                self.spell_list_keys["source"],
                self.spell_list_keys["save_hit"],
                self.spell_list_keys["time"],
                self.spell_list_keys["spell_range"],
                self.spell_list_keys["components"],
                self.spell_list_keys["duration"],
                self.spell_list_keys["page"],
                self.spell_list_keys["notes"],
            ],
            forms,
        )

        for item in items:
            self.player.add_spell(*item)

        return forms

    def add_spellslots(self, forms):
        items, forms = parse_list(
            self.spellslot_list_keys,
            [self.spellslot_list_keys["level"], self.spellslot_list_keys["n_slots"],],
            forms,
        )

        for item in items:
            self.player.add_spellslot(*item)

        return forms
