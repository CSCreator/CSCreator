import logging

from exceptions import MissingPreprocessingArgumentsException


def concat(forms, parameters):
    new_value = ""
    forms_to_concat = parameters.get("forms_to_concat")
    separator = parameters.get("separator")
    if not forms_to_concat or not separator:
        raise MissingPreprocessingArgumentsException()

    previous_set = False
    for index, form_name in enumerate(forms_to_concat):
        this_value = forms.get(form_name, None)

        if this_value and not this_value.isspace():
            #First value does not need a separator. Consecutive only if there was a value before it
            if index > 0 and previous_set:
                new_value += separator
                previous_set = False
            new_value += this_value
            previous_set = True


    return new_value

def dnd_beyond_split_proficiencies(forms, parameters):
    pass

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
