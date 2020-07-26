import logging

from cscreator.components.properties import Properties
from cscreator.utils.svgfile import fromfile

logger = logging.getLogger(__name__)

import uuid

standard_background_color = (0, 1, 1, 1)


class ComponentModel:
    def __init__(self, properties: Properties) -> None:
        self.properties = properties
        self.editable_properties = []
        self.uid = uuid.uuid4()

    def create_canvas_from_svg(self, file):
        background = fromfile(file)
        return background
