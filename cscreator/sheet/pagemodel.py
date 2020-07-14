import logging

from PySide2 import QtCore
from PySide2.QtCore import QByteArray, QDataStream, QIODevice, QMimeData, QPoint
from PySide2.QtGui import Qt, QDrag
from PySide2.QtWidgets import QGraphicsScene

from cscreator.config import CONFIG
from cscreator.views.stagingview import StagingView

logger = logging.getLogger(__name__)


class PageModel(QGraphicsScene):
    def __init__(self):
        super(PageModel, self).__init__()
        self.boxes = []
        self.grids = []
        self.component_controllers = []
        self.setBackgroundBrush(Qt.white)
        pixels_w = CONFIG.PAPER_WIDTH_PIXEL
        pixels_h = CONFIG.PAPER_HEIGHT_PIXEL
        self.setSceneRect(0, 0, pixels_w, pixels_h)
        self.page_view_transform = None
        self.item_being_dragged = None
        logger.debug("PageModel constructed")

    def add_component_controller(self, component_controller):
        self.component_controllers.append(component_controller)
        item = component_controller.get_q_svg_scene_item()
        bounding_rect_size = item.boundingRect().size()
        actual_w = bounding_rect_size.width()
        actual_h = bounding_rect_size.height()
        expected_w = CONFIG.PAPER_WIDTH_PIXEL * (
            component_controller.properties.w / CONFIG.H_SPLIT
        )

        expected_h = CONFIG.PAPER_HEIGHT_PIXEL * (
            component_controller.properties.h / CONFIG.V_SPLIT
        )

        scale_w = expected_w / actual_w
        scale_h = expected_h / actual_h

        if (scale_h - scale_w) < -0.5 or (scale_h - scale_w) > 0.5:
            logger.warning(
                f"Quite some difference between scale_h {scale_h} and scale_w {scale_w}"
            )

        item.setScale(scale_w)

        self.addItem(item)
        self.update()
        logger.debug(f"Component controller added with scaling of {scale_w},{scale_h}")

    def remove_component_controller(self, component_controller):
        for i, o in enumerate(self.component_controllers):
            if o.uid == component_controller.uid:
                del self.component_controllers[i]
                break

        for q_graphics_item in self.items():
            if q_graphics_item.uid == component_controller.uid:
                self.removeItem(q_graphics_item)
                break
        self.update()

    def create(self, total_width_pixels, total_height_pixels, player):
        logger.info("Create called on PageModel, but this might not be needed anymore")

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        # logger.info(f"DragMove pos: {event.scenePos()}")
        if self.item_being_dragged is None:
            logger.error("Something is being dragged, but not item_being_dragged set.")
        self.item_being_dragged.set_position(event.scenePos())
        event.accept()

    def dragLeaveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        def accept_and_add(item, event):

            hot_spot_point = QPoint()

            item_data = event.mimeData().data(CONFIG.COMPONENT_MIME)
            data_stream = QDataStream(item_data, QIODevice.ReadOnly)
            data_stream >> hot_spot_point
            view_to_scene_transform, succes = self.page_view_transform.inverted()
            if not succes:
                logger.error("Page_view_transform could not be inverted")

            hot_spot_point = view_to_scene_transform.map(hot_spot_point)
            item.set_position(event.scenePos() - hot_spot_point)
            self.add_component_controller(item)
            logger.info("dropEvent")
            event.setDropAction(Qt.MoveAction)
            event.accept()

        source_widget = event.source()
        if isinstance(source_widget, StagingView) and event.mimeData().hasFormat(
            CONFIG.COMPONENT_MIME
        ):
            item = source_widget.item_being_dragged
            if item is None:
                logger.error("Drag does not have a item_being_dragged set.")
            else:
                accept_and_add(item, event)
                source_widget.item_being_dragged = None

        elif source_widget is None and self.item_being_dragged is not None:
            logger.info(
                f"Dropevent probably into myself, unknown source {source_widget}"
            )
            item = self.item_being_dragged
            self.item_being_dragged = None
            accept_and_add(item, event)

        else:
            logger.info(f"Dropevent ignored, unknown source {source_widget}")
            event.ignore()

    def startDrag(self, event):
        item = self.itemAt(event.scenePos(), self.page_view_transform)
        if item is None:
            event.ignore()
            return
        self.item_being_dragged = item.parent
        self.remove_component_controller(item.parent)

        hotspot = event.scenePos() - item.scenePos()
        hot_spot_point = hotspot.toPoint()
        hot_spot_point = self.page_view_transform.map(hot_spot_point)
        item_data = QByteArray()
        data_stream = QDataStream(item_data, QIODevice.WriteOnly)

        data_stream << hot_spot_point  # pixmap << location

        mime_data = QMimeData()
        mime_data.setData(CONFIG.COMPONENT_MIME, item_data)

        drag = QDrag(self)
        drag.setMimeData(mime_data)
        horizontal_scaling = self.page_view_transform.m11()
        logger.info(f"sceneBoundingRect {item.sceneBoundingRect().width()}")
        logger.info(
            f"sceneBoundingRect {item.sceneBoundingRect().width()*horizontal_scaling}"
        )
        drag.setPixmap(
            item.parent.pixmap.scaledToWidth(
                item.sceneBoundingRect().width() * horizontal_scaling
            )
        )
        drag.setHotSpot(hot_spot_point)

        result = drag.start(QtCore.Qt.MoveAction)
        if result:  # == QtCore.Qt.MoveAction:
            pass

    def mouseMoveEvent(self, event):
        self.startDrag(event)
