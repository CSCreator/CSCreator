import logging

from cscreator import config
from cscreator.components.pageproperties import PageProperties
from cscreator.components.utils import unit_str_to_float
from cscreator.utils.svgfile import fromfile, SVGFile
from cscreator.utils.svgtext import text_width

logger = logging.getLogger(__name__)

import uuid

standard_background_color = (0, 1, 1, 1)

class ComponentModel:
    def __init__(self, page_properties, elements):
        self.page_properties = page_properties
        self.elements = elements
        self.base_svg = None

    def create(self, box_width_pixels, box_height_pixels, player):
        width = unit_str_to_float(box_width_pixels)
        height = unit_str_to_float(box_height_pixels)
        self.base_svg = SVGFile(width, height)
        self.base_svg.append(self.elements)
        return self.base_svg


