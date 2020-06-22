from fitz import fitz


def get_forms_from_pdf(file):
    form_fields = {}
    doc = fitz.open(file)
    for page_number in range(doc.pageCount):
        page = doc.loadPage(page_number)
        for field in page.widgets():
            form_fields[field.field_name] = field.field_value

    return form_fields