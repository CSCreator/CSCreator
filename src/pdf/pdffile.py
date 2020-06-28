import logging

from fitz import fitz

from exceptions import InvalidFieldException

logger = logging.getLogger(__name__)


class PDFFile():
    def __init__(self, filename):
        self.doc = fitz.open(filename)
        self.pages = {}
        self.forms = self.get_forms()

    def get_forms(self):
        forms = {}
        for page_number in range(self.doc.pageCount):
            #TODO storing these page references prevents the gc from destroying the widgets parents
            self.pages[page_number] = self.doc.loadPage(page_number)
            for field in self.pages[page_number].widgets():
                forms[field.field_name] = field

        return forms

    def get_forms_names(self):
        forms = []
        for page_number in range(self.doc.pageCount):
            page = self.doc.loadPage(page_number)
            forms = [field.field_name for field in page.widgets()]

        return forms

    def get_forms_and_values(self):
        forms = {}
        for page_number in range(self.doc.pageCount):
            page = self.doc.loadPage(page_number)
            for field in page.widgets():
                forms[field.field_name] = field.field_value

        return forms

    def get_field_type(self, field):
        if field.field_type_string == "Text":
            return str
        elif field.field_type_string == "CheckBox":
            return bool

    def set_field(self, field_name_to_set, value):
        form_to_set = self.forms[field_name_to_set]
        if form_to_set is None:
            logger.error(f"Attempting to set None field with value {value}")
            raise InvalidFieldException(
                f"Attempting to set None field with value {value}"
            )

        value_type = type(value)
        field_type = self.get_field_type(form_to_set)
        if value_type is int and field_type is str:
            value = str(value)
        elif value_type is bool:
            value = bool(value)
        elif value_type is not field_type:
            logging.warning(
                f"Setting value with type {value_type} to field with type {field_type}"
            )
            value = str(value)
        form_to_set.text_fontsize = 0
        form_to_set.field_value = value
        form_to_set.update()

    def save(self, file):
        self.doc.save(file)

    def close(self):
        self.doc.close()

    def __del__(self):
        if not self.doc.isClosed:
            self.close()
