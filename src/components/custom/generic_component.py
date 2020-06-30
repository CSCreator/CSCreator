import logging

from main import config

logger = logging.getLogger(__name__)

import json
import svgwrite

from src.models.componentmodel import ComponentModel
from src.components import unit_str_to_float
from src.svg.text import text_width


class TextElement:
    def __init__(self, text_property, x_percentage, y_percentage, w_percentage):
        self.text_property = text_property
        self.x = x_percentage
        self.y = y_percentage
        self.w = w_percentage

    def __init__(
        self,
        text_property,
        x_absolute,
        y_absolute,
        w_absolute,
        full_width_absolute,
        full_height_absolute,
    ):
        self.text_property = text_property
        self.x = x_absolute / full_width_absolute
        self.y = 1 - (y_absolute / full_height_absolute)
        self.w = w_absolute / full_width_absolute


class CustomComponentDefinition:
    def __init__(self, background_file, relative_w, relative_h):
        self.relative_h = relative_h
        self.relative_w = relative_w
        self.background_file = background_file
        self.text_elements = []

    def add_text_element(self, text_property, x_absolute, y_absolute, w_absolute):
        element = TextElement(
            text_property,
            x_absolute,
            y_absolute,
            w_absolute,
            self.relative_w,
            self.relative_h,
        )
        self.text_elements.append(element)

    def get_component(self, properties):
        return GenericComponentModel(
            properties, self.text_elements, self.background_file
        )


intermediate_file = "tmp/banner_intermediate.svg"


class GenericComponentModel(ComponentModel):
    def __init__(self, properties, text_elements, background_file):
        self.text_elements = text_elements
        self.background_file = background_file
        desired_ratio = 5.0
        if properties.w / properties.h != desired_ratio:
            logger.warning("Not ideal aspect ratio for banner")
        super(GenericComponentModel, self).__init__(properties)

    def create(self, box_width_pixels, box_height_pixels, player):
        import svgutils.transform as sg

        background = self.create_canvas_from_svg(self.background_file)
        size = background.width, background.height
        width = unit_str_to_float(background.width)
        height = unit_str_to_float(background.height)
        # create new SVG figure
        text = svgwrite.Drawing(filename=intermediate_file, size=size)

        for text_info in self.text_elements:
            font_size = 6
            accepted_width = text_info.w * width  # config.mm_to_pixel(width))
            # TODO inconsistent with regular components, which have a ENUM with .name
            text_to_render = getattr(player, text_info.text_property)
            while (
                config.pt_to_mm(text_width(text_to_render, fontsize=font_size)) * 1.5
                >= accepted_width
            ):
                font_size -= 1
                if font_size <= 1:
                    break
            # logger.info("Changed font size to {} because {} wont fit".format(font_size, text_to_render))
            text.add(
                text.text(
                    text_to_render,
                    insert=(text_info.x * width, text_info.y * height),
                    fill="rgb(0,0,0)",
                    style="font-size:{}; font-family:Arial".format(font_size),
                )
            )
        text.save()

        text_utils = sg.fromfile(intermediate_file)
        text_utils.set_size(size)
        # getroot otherwise the viewbox gets appended as well which makes scaling weird
        background.append(text_utils.getroot())
        self.rendered_img = background
        return self.rendered_img


def component_file_parser(file):
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
