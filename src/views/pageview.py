import logging

logger = logging.getLogger(__name__)

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QGraphicsView


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
