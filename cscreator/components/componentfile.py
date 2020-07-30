import json
import logging

from cscreator.components.componentdefinition import CustomComponentDefinition

logger = logging.getLogger(__name__)


def parse(file):
    with open(file) as json_file:
        data = json.load(json_file)
        logger.debug(data)
        component_definition = CustomComponentDefinition(
            data["background_file"], data["reference_size_x"], data["reference_size_y"]
        )
        for element_values in data["text_elements"]:
            component_definition.add_text_element(
                element_values["property"],
                element_values["x_pos"],
                element_values["y_pos"],
                element_values["width"],
            )
        return component_definition
