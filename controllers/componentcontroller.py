import logging
import uuid
from enum import Enum

from PySide2 import QtSvg
from PySide2.QtGui import QDrag, QIcon

from main import config_controller
from models.charactermodel import CH

logger = logging.getLogger(__name__)

from PySide2.QtCore import (
    QPoint,
    QRect,
    QSize,
    QByteArray,
    Qt,
    QDataStream,
    QIODevice,
    QMimeData,
)
from PySide2.QtSvg import QSvgWidget, QGraphicsSvgItem
from PySide2.QtWidgets import QSizeGrip, QGridLayout, QGraphicsItem

standard_background_color = (0, 1, 1, 1)
import svgutils.transform as sg


class PropertyTypes(Enum):
    SINGLE_LINE_STRING = 0
    MULTI_LINE_STRING = 1
    NUMBER = 2


class EditableProperty:
    def __init__(self, property_type, description, value, owner, size_and_pos):
        assert isinstance(property_type, PropertyTypes)
        assert isinstance(description, str)
        self.type = property_type
        self.description = description
        self.value = value
        self.owner = owner
        self.size_and_pos = size_and_pos

    def update_value(self, caller, value):
        self.value = value
        self.owner.rendered_img = None

    def get_value(self, player):
        if isinstance(self.value, str):
            return self.value
        elif isinstance(self.value, CH):
            if player is not None:
                return getattr(player, self.value.name)
            else:
                return ""
        else:
            raise Exception("Unknown type of character_property passed")


class ComponentController:
    def __init__(self, properties, character_controller, **kwargs):
        super(ComponentController, self).__init__(**kwargs)
        self._rendered_img = None
        self.pixmap = None
        self.properties = properties
        self.editable_properties = []
        self.uid = uuid.uuid4()
        self.svg_renderer = QtSvg.QSvgRenderer()
        self.character_controller = character_controller

    @property
    def rendered_img(self):
        return self._rendered_img

    @rendered_img.setter
    def rendered_img(self, value):
        self._rendered_img = value
        string_image = self._rendered_img.to_str()
        value.save("tmp/pixmap_intermediate.svg")
        pixmap_size = QSize(
            config_controller.box_size[0] * self.properties.w,
            config_controller.box_size[1] * self.properties.h,
        )
        self.pixmap = QIcon("tmp/pixmap_intermediate.svg").pixmap(pixmap_size)
        self.svg_renderer.load(QByteArray(string_image))
        logging.info("Rendered img updated")

    def create_canvas(self, size):
        width_mm = config_controller.pixel_to_mm(size[0])
        height_mm = config_controller.pixel_to_mm(size[1])
        fig = sg.SVGFigure(width_mm, height_mm)
        return fig

    def create_canvas_from_svg(self, file):
        background = sg.fromfile(file)
        return background

    def set_position(self, point):
        self.properties.x = point.x() // config_controller.box_size[0]
        self.properties.y = point.y() // config_controller.box_size[1]
        # logging.info(f"Set positions to {self.properties.x} {self.properties.y}")

    def get_q_svg_scene_item(self, parent=None):

        # TODO this is overkill, recreating the SVG Widget way too often.
        self.create(
            config_controller.box_size[0] * self.properties.w,
            config_controller.box_size[1] * self.properties.h,
        )

        q_graphics_svg_item = QGraphicsSvgItem()
        q_graphics_svg_item.parent = self
        q_graphics_svg_item.setFlags(
            QGraphicsItem.ItemIsMovable
            | QGraphicsItem.ItemIsSelectable
            | QGraphicsItem.ItemIsFocusable
            | QGraphicsItem.ItemSendsScenePositionChanges
            | QGraphicsItem.ItemSendsGeometryChanges
        )
        q_graphics_svg_item.uid = self.uid
        q_graphics_svg_item.setSharedRenderer(self.svg_renderer)
        q_graphics_svg_item.setPos(
            float(config_controller.box_size[0] * self.properties.x),
            float(config_controller.box_size[1] * self.properties.y),
        )
        return q_graphics_svg_item

    def get_q_svg_component_widget(self, parent=None):
        label = QSvgWidget(parent)
        label.parent = parent
        # TODO this is overkill, recreating the SVG Widget way too often.
        self.create(
            config_controller.box_size[0] * self.properties.w,
            config_controller.box_size[1] * self.properties.h,
        )

        string_image = self.rendered_img.to_str()
        array = QByteArray(string_image)
        label.load(array)
        label.uid = self.uid
        return label
