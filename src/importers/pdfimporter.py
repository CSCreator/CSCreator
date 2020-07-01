import json
import logging

from exceptions import (
    NotAllImportedWarning,
    ValueEnumKeyNotFoundException,
    DefinitionFileUnreadableException,
)
from src.controllers.charactercontroller import CharacterController
from src.importers.preprocessing_functions import concat, to_boolean_true_if
from src.models.characterenums import SkillProficiencies, Skills
from src.models.charactermodel import CHProperty
from src.models.charactersubmodel import str_to_class
from src.pdf.pdffile import PDFFile

logger = logging.getLogger(__name__)


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


class PDFImporter:
    def __init__(self, plugin):
        # super(DNDBeyondImporter, self).__init__()
        self.player = CharacterController()
        self.plugin = plugin

    def set_value_to_player_if_exists(self, form_fields, key):
        ch = self.plugin.key_conversion[key]
        value = form_fields[key]
        form_fields.pop(key, None)
        self.player.player_model.set_value(ch, value)

    def load(self, file):
        pdf_file = PDFFile(file)
        form_fields = pdf_file.get_forms_and_values()

        form_fields = self.apply_preprocessing(form_fields)
        form_fields = self.handle_ability_order(form_fields)

        for key in list(form_fields.keys()):
            if key in self.plugin.key_conversion:
                self.set_value_to_player_if_exists(form_fields, key)
            elif (
                any(wildcard in key for wildcard in self.plugin.wildcards_to_ignore)
                or key in self.plugin.keys_to_ignore
            ):
                form_fields.pop(key, None)

        self.plugin.import_character_incremental_lists(pdf_file, self.player)
        pdf_file.close()
        if len(form_fields) > 0:
            logger.warning(f"Not all dict values have been parsed! {form_fields}")

    def handle_ability_order(self, forms):
        def return_score_then_prof(score, prof):
            if "-" in score or "+" in score:
                # This is actually the proficiency bonus, switch
                score, prof = prof, score
            return score, prof

        def get_key_from_value(value):

            conversion_keys = list(self.plugin.key_conversion.keys())
            conversion_values = list(self.plugin.key_conversion.values())
            return conversion_keys[conversion_values.index(value)]

        str_value = get_key_from_value(CHProperty.STR)
        dex_value = get_key_from_value(CHProperty.DEX)
        con_value = get_key_from_value(CHProperty.CON)
        int_value = get_key_from_value(CHProperty.INT)
        wis_value = get_key_from_value(CHProperty.WIS)
        cha_value = get_key_from_value(CHProperty.CHA)
        str_mod = get_key_from_value(CHProperty.STR_MOD)
        dex_mod = get_key_from_value(CHProperty.DEX_MOD)
        con_mod = get_key_from_value(CHProperty.CON_MOD)
        int_mod = get_key_from_value(CHProperty.INT_MOD)
        wis_mod = get_key_from_value(CHProperty.WIS_MOD)
        cha_mod = get_key_from_value(CHProperty.CHA_MOD)

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
        for new_field, process in self.plugin.pre_processing.items():
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
                new_value = concat(forms, parameters)
            if method == "to_bool_true_if":
                if not "field" in parameters:
                    parameters["field"] = new_field
                new_value = to_boolean_true_if(forms, parameters)

            forms[new_field] = new_value

            if delete_after:
                for parameter in parameters:
                    forms.pop(parameter, None)
        return forms
