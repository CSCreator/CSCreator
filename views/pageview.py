import logging

from main import config_controller
from views.stagingview import StagingView

logger = logging.getLogger(__name__)

from PySide2.QtCore import (
    Signal,
    QRect,
    QSize,
    Qt,
    QPoint,
    QByteArray,
    QDataStream,
    QIODevice,
    QMimeData,
)
from PySide2.QtGui import QDrag, QPainter, QColor
from PySide2.QtSvg import QSvgWidget
from PySide2.QtWidgets import (
    QFrame,
    QSizePolicy,
    QWidget,
    QGraphicsView,
    QGraphicsScene,
)


class PageView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(PageView, self).__init__(scene, parent)
        self.fitInView(scene.sceneRect(), AspectRatioMode=Qt.KeepAspectRatio)
        self.page_model = scene
        self.page_model.page_view_transform = self.transform()
        self.setAcceptDrops(True)
        self.setInteractive(True)

    def resizeEvent(self, e):
        super(PageView, self).resizeEvent(e)
        self.fitInView(self.scene().sceneRect(), AspectRatioMode=Qt.KeepAspectRatio)
        self.page_model.page_view_transform = self.transform()
