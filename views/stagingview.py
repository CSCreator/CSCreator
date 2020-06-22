import logging

from PySide2 import QtCore, QtGui

from main import config_controller
from views import pageview

logger = logging.getLogger(__name__)

from PySide2.QtCore import (
    QSize,
    Qt,
    QByteArray,
    QDataStream,
    QIODevice,
    QMimeData,
    QPoint,
)
from PySide2.QtGui import QIcon, QPixmap, QDrag
from PySide2.QtWidgets import QListWidget, QListView, QListWidgetItem, QGraphicsTextItem


class CustomQListWidgetItem(QListWidgetItem):
    def __init__(self):
        super(CustomQListWidgetItem, self).__init__()

    def mouseMoveEvent(self, event):
        event.accept()
        logging.info("CustomQListWidgetItem mouseMoveEvent")

    def dragEnterEvent(self, event):
        logging.info("dragEnterEvent CustomQListWidgetItem")


class StagingView(QListWidget):
    def __init__(self, parent=None):
        super(StagingView, self).__init__(parent)
        self.setDragEnabled(True)
        self.setViewMode(QListView.IconMode)
        self.setFlow(QListView.TopToBottom)
        self.setWrapping(False)
        self.setResizeMode(QListView.Adjust)
        self.setSpacing(10)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.item_being_dragged = None
        logging.debug("StagingView constructed")

    def resizeEvent(self, event):
        logger.info("PiecesList resized")
        spacing = self.spacing() * 2
        width = self.viewport().width() - spacing
        if width > 300:
            width = 300
        self.setIconSize(QSize(width, width))

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dragLeaveEvent(self, event):
        event.accept()

    def startDrag(self, event):
        item = self.currentItem()
        if item is None:
            event.ignore()
            return
        self.item_being_dragged = self.takeItem(self.row(item)).parent

        hot_spot_point = event.pos()

        item_data = QByteArray()
        data_stream = QDataStream(item_data, QIODevice.WriteOnly)

        data_stream << hot_spot_point  # pixmap << location

        mime_data = QMimeData()
        mime_data.setData(config_controller.component_mime, item_data)

        drag = QDrag(self)
        pixmap = item.parent.pixmap.scaledToWidth(64)
        drag.setHotSpot(QPoint(pixmap.width() / 2, pixmap.height() / 2))
        drag.setPixmap(pixmap)
        drag.setMimeData(mime_data)
        result = drag.start(QtCore.Qt.MoveAction)
        if result:  # == QtCore.Qt.MoveAction:
            pass

    def mouseMoveEvent(self, event):
        self.startDrag(event)

    def dropEvent(self, event):
        from models.pagemodel import PageModel

        def accept_and_add(item, event):
            self.add_component_controller(item)
            logging.info("dropEvent")
            event.setDropAction(Qt.MoveAction)
            event.accept()

        source_widget = event.source()
        if isinstance(source_widget, PageModel) and event.mimeData().hasFormat(
            config_controller.component_mime
        ):
            item = source_widget.item_being_dragged
            if item is None:
                logging.error("Drag does not have a item_being_dragged set.")
            accept_and_add(item, event)
        elif isinstance(source_widget, StagingView):
            item = self.item_being_dragged
            self.item_being_dragged = None
            accept_and_add(item, event)
        else:
            event.ignore()

    def add_component_controller(self, component_controller):
        label = component_controller.get_q_svg_component_widget()
        controller_item = QListWidgetItem()
        controller_item.parent = component_controller
        controller_item.setText("Testtest")
        pixmap = component_controller.pixmap
        controller_item.setIcon(pixmap)
        controller_item.setFlags(
            Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled
        )
        controller_item.component_controller = component_controller
        self.setItemWidget(controller_item, label)
        self.addItem(controller_item)
        logging.debug("Component added")
