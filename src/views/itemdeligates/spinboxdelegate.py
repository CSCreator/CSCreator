import PySide2
import logging

logger = logging.getLogger(__name__)
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QStyledItemDelegate, QSpinBox, QAbstractItemDelegate


class SpinBoxDelegate(QStyledItemDelegate):
    def __init__(self, min_value, max_value):
        super(SpinBoxDelegate, self).__init__()
        self.min = min_value
        self.max = max_value

    def createEditor(
        self,
        parent: PySide2.QtWidgets.QWidget,
        option: PySide2.QtWidgets.QStyleOptionViewItem,
        index: PySide2.QtCore.QModelIndex,
    ) -> PySide2.QtWidgets.QWidget:
        editor = QSpinBox(parent)
        editor.setFrame(False)
        editor.setMinimum(self.min)
        editor.setMaximum(self.max)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        editor.setValue(int(value))

    def setModelData(
        self,
        editor: PySide2.QtWidgets.QSpinBox,
        model: PySide2.QtCore.QAbstractItemModel,
        index: PySide2.QtCore.QModelIndex,
    ):
        value = editor.value()
        logger.debug(f"Setting model {model} with value {value}")
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(
        self,
        editor: PySide2.QtWidgets.QWidget,
        option: PySide2.QtWidgets.QStyleOptionViewItem,
        index: PySide2.QtCore.QModelIndex,
    ):
        editor.setGeometry(option.rect)
