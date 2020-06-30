import logging
import os

from PySide2.QtCore import QStandardPaths

from src.models.characterenums import SkillProficiencies
from src.models.charactermodel import CH
from src.pdf.pdffile import PDFFile

logger = logging.getLogger(__name__)


class PDFExporter:
    def __init__(self, player_controller, pdf_file, plugin):
        self.player_controller = player_controller
        self.plugin = plugin

        self.pdf_target = pdf_file

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
        # TODO exporter should tell me what file to use
        dir_to_search = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        dir_to_search = os.path.join(dir_to_search, "exporters")
        file_to_export_to = os.path.join(
            dir_to_search, "Character Sheet_WARLOCK_FILLABLE.pdf"
        )
        pdf_file = PDFFile(file_to_export_to)
        form_fields = pdf_file.get_forms_names()

        convertable_form_fields = [
            field_name
            for field_name in form_fields
            if field_name in self.plugin.key_conversion.keys()
        ]
        for field in convertable_form_fields:
            ch_candidate = self.plugin.key_conversion[field]
            if not ch_candidate:
                logger.info(f"Value {ch_candidate} is not a valid CH")
                continue
            ch = CH(ch_candidate)
            value = getattr(self.player_controller.player_model, ch.name)
            pdf_file.set_field(field, value)

        # TODO maybe go to a model where we do not keep track of set fields and check it at another place (plugin?)
        # form_fields = [
        #         #     form for form in form_fields if form not in convertable_form_fields
        #         # ]

        # TODO skills
        # forms = self.export_skills(form_fields, self.skill_keys)
        self.plugin.export_character_incremental_lists(
            pdf_file, self.player_controller
        )

        pdf_file.save(self.pdf_target)
