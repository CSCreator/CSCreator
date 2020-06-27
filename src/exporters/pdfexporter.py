import csv
import json
import logging
import os

from PySide2.QtCore import QStandardPaths
from fitz import fitz

from exceptions import InvalidFieldException, DefinitionFileUnreadableException
from src.models.characterenums import SkillProficiencies
from src.models.charactermodel import CH
from src.models.charactersubmodel import Attack, Spell

logger = logging.getLogger(__name__)


class PDFExporter:
    def __init__(self, player_controller, pdf_file, definition_file):
        self.player_controller = player_controller

        try:
            with open(definition_file, "r") as j:
                definition = json.loads(j.read())
        except IOError:
            raise DefinitionFileUnreadableException(
                f"Definition file {definition_file} cannot be read or found"
            )

        self.name = definition.get("exporter_name", False)
        self.key_conversion = definition.get("key_conversion", None)
        self.weapon_list_keys = definition.get("weapon_list_keys", None)
        self.spell_list_keys = definition.get("spell_list_keys", None)
        self.skill_keys = definition.get("skill_keys", None)

        self.pdf_target = pdf_file

    def get_field_type(self, field):
        if field.field_type_string == "Text":
            return str
        elif field.field_type_string == "CheckBox":
            return bool

    def set_field(self, field_to_set, value):
        if field_to_set is None:
            logging.error(f"Attempting to set None field with value {value}")
            raise InvalidFieldException(
                f"Attempting to set None field with value {value}"
            )

        value_type = type(value)
        field_type = self.get_field_type(field_to_set)
        if value_type is int and field_type is str:
            value = str(value)
        elif value_type is bool:
            value = bool(value)
        elif value_type is not field_type:
            logging.warning(
                f"Setting value with type {value_type} to field with type {field_type}"
            )
            value = str(value)
        field_to_set.text_fontsize = 0
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

    def find_form(self, form, forms, index):
        form_nominee = None
        for form_candidate in form:
            form_candidate = form_candidate.format(index)
            if form_candidate in forms:
                form_nominee = forms[form_candidate]
                break
        return form_nominee

    def set_item_fields(self, item, fields_to_map, forms_to_fill, forms, index):
        for value, form in forms_to_fill.items():
            for column_index, value_name in fields_to_map.items():
                if value_name == value:
                    form_nominee = self.find_form(form, forms, index)
                    self.set_field(form_nominee, item.get_column(column_index))
        return forms

    def export_custom_table(self, item_class, forms, keys):
        max_items = keys["max_items"]
        zero_indexed = keys["zero_indexed"]

        fields_to_map = item_class.columns_names
        forms_to_fill = keys["incremental_list"]

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

        form_fields_convertable = [
            field
            for field_name, field in forms.items()
            if field_name in self.key_conversion.keys()
        ]
        for field in form_fields_convertable:
            ch_candidate = self.key_conversion[field.field_name]
            if not ch_candidate in CH._value2member_map_:
                logger.info(f"Value {ch_candidate} is not a valid CH")
                continue
            ch = CH(ch_candidate)
            value = getattr(self.player_controller.player_model, ch.name)
            self.set_field(field, value)
            forms.pop(field.field_name)

        forms = self.export_skills(forms, self.skill_keys)
        forms = self.export_custom_table(Attack, forms, self.weapon_list_keys)
        forms = self.export_custom_table(Spell, forms, self.spell_list_keys)

        doc.save(self.pdf_target)

        with open("dict_out.csv", "w", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in forms.items():
                writer.writerow([key, value])
