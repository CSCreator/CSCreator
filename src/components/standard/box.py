import logging

from src.components.utils import unit_str_to_float
from src.controllers.componentcontroller import (
    ComponentController,
    EditableProperty,
    PropertyTypes,
)
from main import config_controller

logger = logging.getLogger(__name__)

import svgwrite

import svgutils.transform as sg

from src.svg.text import text_width

intermediate_border_file = "tmp/box_border_intermediate.svg"
intermediate_text_file = "tmp/box_text_intermediate.svg"


class BoxController(ComponentController):
    def __init__(self, properties, header_text, text, active_character_controller):
        super(BoxController, self).__init__(properties, active_character_controller)
        self.body_text = ""
        self.header_property = EditableProperty(
            PropertyTypes.SINGLE_LINE_STRING, "Header String", header_text, None, self
        )
        self.editable_properties.append(self.header_property)
        self.text_property = EditableProperty(
            PropertyTypes.MULTI_LINE_STRING, "Box text", text, None, self
        )
        self.editable_properties.append(self.text_property)

        self.total_width = -1
        self.total_height = -1

    def create(self, box_width_pixels: int, box_height_pixels: int) -> sg.SVGFigure:
        self.total_width = box_width_pixels
        self.total_height = box_height_pixels

        img = self.create_canvas((self.total_width, self.total_height))
        size = img.width, img.height
        width = unit_str_to_float(img.width)
        height = unit_str_to_float(img.height)
        # create new SVG figure
        box = svgwrite.Drawing(filename=intermediate_border_file, size=size)
        borders = box.add(box.g(id="borders", stroke="black", stroke_width=1))

        borders.add(box.line(start=(0, 0), end=(size[0], 0)))
        borders.add(box.line(start=(size[0], 0), end=(size[0], size[1])))
        borders.add(box.line(start=(size[0], size[1]), end=(0, size[1])))
        borders.add(box.line(start=(0, size[1]), end=(0, 0)))
        box.save()

        # create new SVG figure
        text = svgwrite.Drawing(filename=intermediate_text_file, size=size)

        # Header
        font_size = 6
        text_to_render = self.header_property.get_value(self.character_controller)
        while (
            config_controller.pt_to_mm(text_width(text_to_render, fontsize=font_size))
            >= width
        ):
            font_size -= 1
            if font_size <= 1:
                break
            logger.info(
                "Changed font size to {} because {} wont fit".format(
                    font_size, text_to_render
                )
            )
        text_w = config_controller.pt_to_mm(
            text_width(text_to_render, fontsize=font_size)
        )
        x = (width - text_w) / 2
        text.add(
            text.text(
                self.header_property.get_value(self.character_controller),
                insert=(x, int(0.95 * height)),
                fill="rgb(0,0,0)",
                style="font-size:2.5px; font-family:Arial",
            )
        )

        # Box
        font_size = 6
        text_to_render = self.text_property.get_value(self.character_controller)

        text.add(
            text.text(
                text_to_render,
                insert=(0, int(0.5 * height)),
                fill="rgb(0,0,0)",
                style="font-size:{}; font-family:Arial".format(font_size),
            )
        )

        text.save()

        text_utils = sg.fromfile(intermediate_border_file)
        text_utils.set_size(size)
        img.append(text_utils.getroot())

        text_utils = sg.fromfile(intermediate_text_file)
        text_utils.set_size(size)
        img.append(text_utils.getroot())
        img.save("debug/box{}.svg".format(self.uid))
        self.rendered_img = img
        return self.rendered_img
