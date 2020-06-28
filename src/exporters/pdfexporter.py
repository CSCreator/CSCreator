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
from src.pdf.pdfutils import get_form_names_and_values_from_pdf, get_forms_from_pdf

logger = logging.getLogger(__name__)


class PDFExporter:
    def __init__(self, player_controller, pdf_file, plugin):
        self.player_controller = player_controller
        self.plugin = plugin

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

    def export(self):
        #TODO exporter should tell me what file to use
        dir_to_search = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        dir_to_search = os.path.join(dir_to_search, "exporters")
        file_to_export_to = os.path.join(
            dir_to_search, "Character Sheet_WARLOCK_FILLABLE.pdf"
        )

        self.form_fields, self.open_file = get_forms_from_pdf(file_to_export_to)

        form_fields_convertable = [
            field
            for field_name, field in self.form_fields.items()
            if field_name in self.plugin.key_conversion.keys()
        ]
        for field in form_fields_convertable:
            ch_candidate = self.plugin.key_conversion[field.field_name]
            if not ch_candidate:
                logger.info(f"Value {ch_candidate} is not a valid CH")
                continue
            ch = CH(ch_candidate)
            value = getattr(self.player_controller.player_model, ch.name)
            self.set_field(field, value)
            self.form_fields.pop(field.field_name)
        #TODO skills
        #forms = self.export_skills(form_fields, self.skill_keys)
        self.plugin.export_character_incremental_lists(self.form_fields, self.player_controller)

        # with open("dict_out.csv", "w", encoding="utf-8") as csv_file:
        #     writer = csv.writer(csv_file)
        #     for key, value in form_fields.items():
        #         writer.writerow([key, value])

        self.open_file.save(self.pdf_target)


