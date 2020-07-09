import logging

from PySide2.QtCore import QEvent

from cscreator.config import CONFIG
from cscreator.views.pageview import PageView

logger = logging.getLogger(__name__)

from PySide2 import QtCore
from PySide2.QtWidgets import QFrame, QBoxLayout, QSpacerItem


class SheetView(QFrame):
    def __init__(self, page_view: PageView) -> None:
        super().__init__()
        self.page_view = page_view
        self.aspect_ratio = CONFIG.PAPER_RATIO
        self.setLayout(QBoxLayout(QBoxLayout.LeftToRight, self))
        #  add spacer, then widget, then spacer
        self.layout().addItem(QSpacerItem(0, 0))
        self.layout().addWidget(page_view)
        self.layout().addItem(QSpacerItem(0, 0))
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        # self.page_view.show()
        self.setObjectName("AspectRatio")
        self.setStyleSheet("#AspectRatio {background-color:grey;}")

    def resizeEvent(self, e: QEvent) -> None:
        w = e.size().width()
        h = e.size().height()

        if h / w >= self.aspect_ratio:  # too tall
            self.layout().setDirection(QBoxLayout.TopToBottom)
            ideal_size = w * self.aspect_ratio
            outer_stretch = (h - ideal_size) / 2 + 0.5
            logger.info("Ratio too tall")
        else:  # too wide
            self.layout().setDirection(QBoxLayout.LeftToRight)
            ideal_size = h * (1 / self.aspect_ratio)
            outer_stretch = (w - ideal_size) / 2 + 0.5
            logger.info("Ratio too wide")

        self.layout().setStretch(0, outer_stretch)
        self.layout().setStretch(1, ideal_size)
        self.layout().setStretch(2, outer_stretch)
