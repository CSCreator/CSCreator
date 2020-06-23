from fitz import fitz


def get_forms_from_pdf(file):
    forms = {}
    doc = fitz.open(file)
    for page_number in range(doc.pageCount):
        page = doc.loadPage(page_number)
        for field in page.widgets():
            forms[field.field_name] = field

    return forms, doc

def get_form_names_and_values_from_pdf(file):
    form_fields = {}
    doc = fitz.open(file)
    for page_number in range(doc.pageCount):
        page = doc.loadPage(page_number)
        for field in page.widgets():
            form_fields[field.field_name] = field.field_value

    return form_fields, doc