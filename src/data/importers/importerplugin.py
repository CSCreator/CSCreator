from abc import abstractmethod, ABC
from typing import Dict

from src.models.characterenums import CHProperty
from src.models.charactersubmodel import str_to_class
import logging

logger = logging.getLogger(__name__)


class HardcodedListParser:
    def __init__(self, item_type, hardcoded_list):
        self.item_class = str_to_class(item_type)
        if self.item_class is None:
            logger.warning(f"SubModelName {item_type} unknown")
        self.items_to_convert = hardcoded_list

    def parse_import(self, pdf_file, character_controller):
        if self.item_class is None:
            logger.warning(f"Attempting to parse a list with no item_class set")
            return

        column_names = self.item_class.columns_names
        column_names_inverted = {v: k for k, v in column_names.items()}

        for enum, item in self.items_to_convert.items():
            submodel_item = self.item_class()
            submodel_item.named_item_enum = enum
            for column_name, form_name in item.items():
                column_index = column_names_inverted[column_name]

                forms_values = pdf_file.forms_and_values
                value = forms_values.get(form_name)
                if not value:
                    # TODO handle enums here
                    value = None

                submodel_item.set_column(column_index, value)
            # TODO if submodel_item is completely None or EnumNames, do not add
            character_controller.add_item(self.item_class, submodel_item)

    def parse_export(self, pdf_file, character_controller):
        character_submodels = character_controller.get_models()
        if self.item_class not in character_submodels:
            return
        for current_item in character_controller.get_items(self.item_class):
            current_item_enum = current_item.named_item_enum
            if not current_item_enum:
                logger.warning(
                    f"Trying to export fixed item {self.item_class}, but no named_item_enum_set. Do not know where to place"
                )
                continue

            current_item_forms = self.items_to_convert.get(current_item_enum)
            if not current_item_forms:
                logger.warning(
                    f"Current_item_enum {current_item_enum} not found in self.items_to_convert"
                )
                continue

            for column_index in current_item.columns_names:
                value = current_item.get_column(column_index)
                column_name = current_item.columns_names[column_index]
                field_to_set = current_item_forms.get(column_name)
                if field_to_set:
                    pdf_file.set_field(field_to_set, value)


class IncrementalListParser:
    def __init__(self, item_type, incremental_lists):
        self.item_class = str_to_class(item_type)
        if self.item_class is None:
            logger.warning(f"SubModelName {item_type} unknown")
        self.column_to_form = incremental_lists.get("column_to_form")
        self.max_items = incremental_lists.get("max_items")
        self.zero_indexed = incremental_lists.get("zero_indexed")
        self.hardcoded_keys = incremental_lists.get("hardcoded_keys")
        self.header_key = incremental_lists.get("header_key")

    def import_incremental_list(self, pdf_file, character_controller):
        for i in range(self.max_items):
            if not self.zero_indexed:
                i += 1

            item_columns = {}
            for column_name in self.column_to_form:
                key = self.get_candidate_key(column_name, i, pdf_file.forms)
                item_columns[column_name] = pdf_file.forms_and_values.get(key)
            values = item_columns.values()
            if all(value == "" or value is None for value in values):
                # TODO this does not catch all spells
                # TODO if the column_names do not exist, this fails silently
                continue

            item = self.item_class(**item_columns)
            character_controller.add_item(self.item_class, item)

    def export_incremental_list(self, pdf_file, character_controller):
        character_submodels = character_controller.get_models()
        if self.item_class not in character_submodels:
            return
        for item_index, current_item in enumerate(
            character_controller.get_items(self.item_class)
        ):
            if self.zero_indexed:
                item_index += 1
            for column_index in current_item.columns_names:
                value = current_item.get_column(column_index)
                column_name = current_item.columns_names[column_index]
                field_to_set = self.get_candidate_key(
                    column_name, item_index, pdf_file.forms
                )
                if field_to_set:
                    pdf_file.set_field(field_to_set, value)

    def parse_import(self, pdf_file, character_controller):
        if self.item_class is None:
            logger.warning(f"Attempting to parse a list with no item_class set")
            return

        if self.column_to_form:
            self.import_incremental_list(pdf_file, character_controller)

    def parse_export(self, forms_to_export, character_controller):
        if self.item_class is None:
            logger.warning(f"Attempting to parse a list with no item_class set")
            return

        if self.column_to_form:
            self.export_incremental_list(forms_to_export, character_controller)

    def get_candidate_key(self, column_name, index, forms):
        if self.column_to_form is None:
            return None
        unformatted_fields = self.column_to_form.get(column_name)
        if unformatted_fields is None:
            return None

        formatted_fields = [field.format(index) for field in unformatted_fields]
        for formatted_field in formatted_fields:
            if formatted_field in self.hardcoded_keys:
                return self.hardcoded_keys[formatted_field]
            if formatted_field in forms:
                return formatted_field

        return None


class ImporterPlugin:
    name = None
    key_conversion = None
    keys_to_ignore = None
    wildcards_to_ignore = None
    incremental_lists = None
    hardcoded_lists = None
    override = None
    pre_processing = None

    incremental_lists_parsers = []
    hardcoded_lists_parsers = []

    def __init__(self):
        self.register_incremental_lists()
        self.register_hardcoded_lists()
        if not self.conversions_valid():
            logger.warning(
                f"Not all specified key_conversion are known CHProperty values. This may result in errors later on"
            )

    def conversions_valid(self) -> bool:
        all_conversions_valid = True
        if self.key_conversion:
            for key, value in self.key_conversion.items():
                if value not in CHProperty._value2member_map_:
                    logger.warning(
                        f"Plugin refers to CH field {value} which does not exist"
                    )
                    all_conversions_valid = False
                else:
                    self.key_conversion[key] = CHProperty(value)

        if self.key_conversion and all_conversions_valid:
            return True

    def register_incremental_lists(self):
        if self.incremental_lists is not None:
            for item_type, incremental_list in self.incremental_lists.items():
                self.incremental_lists_parsers.append(
                    IncrementalListParser(item_type, incremental_list)
                )

    def register_hardcoded_lists(self):
        if self.hardcoded_lists is not None:
            for item_type, hardcoded_list in self.hardcoded_lists.items():
                self.hardcoded_lists_parsers.append(
                    HardcodedListParser(item_type, hardcoded_list)
                )

    def override_values(self, pdf_file):
        if not self.override:
            return pdf_file

        for key, value in pdf_file.forms_and_values.items():
            if value in self.override:
                pdf_file.forms_and_values[key] = self.override[value]
        return pdf_file

    def export_character_incremental_lists(self, pdf_file, character_controller):
        for incremental_list_parser in self.incremental_lists:
            incremental_list_parser.parse_export(pdf_file, character_controller)
        for hardcoded_list_parser in self.hardcoded_lists:
            hardcoded_list_parser.parse_export(pdf_file, character_controller)

    def import_character_incremental_lists(self, pdf_file, character_controller):
        for incremental_list_parser in self.incremental_lists_parsers:
            incremental_list_parser.parse_import(pdf_file, character_controller)
        for hardcoded_list_parser in self.hardcoded_lists_parsers:
            hardcoded_list_parser.parse_import(pdf_file, character_controller)
