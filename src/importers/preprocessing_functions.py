import logging


def concat(forms, parameters):
    new_value = ""
    for parameter in parameters:
        new_value += forms.get(parameter, "")
    return new_value


def to_boolean_true_if(forms, parameters):
    new_value = ""
    true_value = parameters["value"]
    field = parameters["field"]
    if isinstance(true_value, bool):
        new_value = bool(forms[field]) == true_value
    elif isinstance(true_value, str):
        new_value = forms[field] == true_value
    else:
        logging.error(f"Unknown type {type(true_value)} for method to_boolean_true_if")
    return new_value
