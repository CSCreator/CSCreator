import logging

from src.components.properties import Properties

logger = logging.getLogger(__name__)

import uuid

standard_background_color = (0, 1, 1, 1)
import svgutils.transform as sg


class ComponentModel:
    def __init__(self, properties: Properties) -> None:
        self.properties = properties
        self.editable_properties = []
        self.uid = uuid.uuid4()

    def create_canvas_from_svg(self, file):
        background = sg.fromfile(file)
        return background
