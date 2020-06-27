import json
import logging
import os

from PySide2.QtCore import QStandardPaths

from src.models.charactermodel import CH
from src.models.charactersubmodel import str_to_class

logger = logging.getLogger(__name__)


class FixedListParser():
    def __init__(self, item_type, fixed_list):
        self.item_class = str_to_class(item_type)
        if self.item_class is None:
            logger.warning(f"SubModelName {item_type} unknown")

        self.hardcoded_keys = fixed_list.get("hardcoded_keys")

    def parse_fixed_list(self, forms_to_import, character_controller):
        pass

    def parse_import(self, forms_to_import, character_controller):
        if self.item_class is None:
            logger.warning(f"Attempting to parse a list with no item_class set")
            return

        if self.column_to_form:
            self.parse_incremental_list(forms_to_import, character_controller)
        elif self.enumn_to_form:
            self.parse_fixed_list(forms_to_import, character_controller)

    def export(self, forms_to_export, character_controller):

        pass

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

class IncrementalListParser():
    def __init__(self, item_type, incremental_lists):
        self.item_class = str_to_class(item_type)
        if self.item_class is None:
            logger.warning(f"SubModelName {item_type} unknown")
        self.column_to_form = incremental_lists.get("column_to_form")
        self.max_items = incremental_lists.get("max_items")
        self.zero_indexed = incremental_lists.get("zero_indexed")
        self.hardcoded_keys = incremental_lists.get("hardcoded_keys")


    def parse_incremental_list(self, forms_to_import, character_controller):
        for i in range(self.max_items):
            if not self.zero_indexed:
                i += 1

            item_columns = {}
            for column_name in self.column_to_form:
                key = self.get_candidate_key(column_name, i, forms_to_import)
                item_columns[column_name] = forms_to_import.get(key)
            values = item_columns.values()
            if all(value == '' or value == None for value in values):
                #TODO this does not catch all spells
                #TODO if the column_names do not exist, this fails silently
                continue

            item = self.item_class(**item_columns)
            character_controller.add_item(self.item_class, item)

    def parse_import(self, forms_to_import, character_controller):
        if self.item_class is None:
            logger.warning(f"Attempting to parse a list with no item_class set")
            return

        if self.column_to_form:
            self.parse_incremental_list(forms_to_import, character_controller)


    def export(self, forms_to_export, character_controller):

        pass

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

class Plugin():
    def __init__(self, definition_file):
        try:
            with open(definition_file, "r") as j:
                definition = json.loads(j.read())
        except Exception:
            logger.warning(f"JSON file {definition_file} found but not openable")

        self.name = definition.get("name", None)
        self.key_conversion = definition.get("key_conversion", None)
        self.keys_to_ignore = definition.get("keys_to_ignore", None)
        self.wildcards_to_ignore = definition.get("wildcards_to_ignore", None)
        self.pre_processing = definition.get("pre_processing", None)

        self.incremental_lists = []

        lists = definition.get("incremental_lists", None)
        if lists is not None:
            for item_type, incremental_lists in lists.items():
                self.incremental_lists.append(IncrementalListParser(item_type, incremental_lists))

        all_conversions_valid = self.verify_conversions()

        if self.name and self.key_conversion and all_conversions_valid:
            self.valid = True
        else:
            self.valid = False

    def verify_conversions(self):
        all_conversions_valid = True
        if self.key_conversion:
            for key, value in self.key_conversion.items():
                if value not in CH._value2member_map_:
                    logger.warning(f"Plugin refers to CH field {value} which does not exist")
                    all_conversions_valid = False
                else:
                    self.key_conversion[key] = CH(value)
        return all_conversions_valid

    def export_character_incremental_lists(self, forms_to_fill, player_controller):
        pass

    def import_character_incremental_lists(self, forms_to_read, character_controller):
        for incremental_list_parser in self.incremental_lists:
            incremental_list_parser.parse_import(forms_to_read, character_controller)

class PluginManager():
    def __init__(self):
        self.plugin_dir = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        self.importers = self.find_valid_plugins(subdir="importers")
        self.exporters = self.find_valid_plugins(subdir="exporters")

    def find_valid_plugins(self, subdir):
        dir_to_search = self.plugin_dir
        dir_to_search = os.path.join(dir_to_search, subdir)
        plugins = []
        for file in os.listdir(dir_to_search):
            if file.endswith(".json"):
                file = os.path.join(dir_to_search, file)
                plugin = Plugin(file)
                # At some point we might return invalid plugins so the user can fix them later
                if plugin.valid:
                    plugins.append(plugin)

        return plugins
