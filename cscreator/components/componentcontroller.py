import logging
import uuid
from enum import Enum
from typing import Tuple, Union, Any, List

from PySide2 import QtSvg, QtXml
from PySide2.QtGui import QIcon, QImage, QPainter

from cscreator.character.charactercontroller import CharacterController
from cscreator.character.characterenums import CHProperty
from cscreator.components.componentmodel import ComponentModel
from cscreator.components.pageproperties import PageProperties
from cscreator.config import CONFIG
from cscreator.utils.svgfile import SVGFile, FigureElement
from exceptions import UnknownCharacterProperty

logger = logging.getLogger(__name__)

from PySide2.QtCore import (
    QSize,
    QByteArray,
)
from PySide2.QtSvg import QSvgWidget, QGraphicsSvgItem
from PySide2.QtWidgets import QGraphicsItem

standard_background_color = (0, 1, 1, 1)


class ComponentController:
    def __init__(
            self,
            page_properties: PageProperties,
            character_controller: CharacterController,
            elements: List[FigureElement],
            **kwargs
    ) -> None:
        self._rendered_img = None
        self.pixmap: QIcon = QIcon()
        self.page_properties = page_properties
        self.editable_properties = []
        self.uid = uuid.uuid4()
        self.svg_renderer = QtSvg.QSvgRenderer()
        self.character_controller = character_controller
        self.component_model = ComponentModel(page_properties, elements)

    @property
    def rendered_img(self):
        return self._rendered_img

    @rendered_img.setter
    def rendered_img(self, value):
        self._rendered_img = value
        string_image = self._rendered_img.to_str()
        self._rendered_img.save("tmp/pixmap_intermediate.svg")
        pixmap_size = QSize(
            CONFIG.BOX_SIZE[0] * self.page_properties.w,
            CONFIG.BOX_SIZE[1] * self.page_properties.h,
        )
        self.pixmap = QIcon("tmp/pixmap_intermediate.svg").pixmap(pixmap_size)
        self.svg_renderer.load("tmp/pixmap_intermediate.svg")
        logger.info("Rendered img updated")

    def set_position(self, point):
        self.page_properties.x = point.x() // CONFIG.BOX_SIZE[0]
        self.page_properties.y = point.y() // CONFIG.BOX_SIZE[1]
        # logger.info(f"Set positions to {self.page_properties.x} {self.page_properties.y}")

    def get_q_svg_scene_item(self, parent=None):
        # TODO this is overkill, recreating the SVG Widget way too often.
        self.component_model.create(
            int(CONFIG.BOX_SIZE[0] * self.page_properties.w),
            int(CONFIG.BOX_SIZE[1] * self.page_properties.h),
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
            float(CONFIG.BOX_SIZE[0] * self.page_properties.x),
            float(CONFIG.BOX_SIZE[1] * self.page_properties.y),
        )
        return q_graphics_svg_item

    def get_q_svg_component_widget(self, parent=None):
        label = QSvgWidget(parent)
        label.parent = parent
        # TODO this is overkill, recreating the SVG Widget way too often.
        self.create(
            CONFIG.BOX_SIZE[0] * self.page_properties.w,
            CONFIG.BOX_SIZE[1] * self.page_properties.h,
        )

        string_image = self.rendered_img.to_str()
        array = QByteArray(string_image)
        label.load(array)
        label.uid = self.uid
        return label
