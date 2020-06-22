import PySide2
import logging

logger = logging.getLogger(__name__)
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QStyledItemDelegate,
    QCheckBox,
)


class CheckBoxDelegate(QStyledItemDelegate):
    def __init__(self):
        super(CheckBoxDelegate, self).__init__()

    def createEditor(
        self,
        parent: PySide2.QtWidgets.QWidget,
        option: PySide2.QtWidgets.QStyleOptionViewItem,
        index: PySide2.QtCore.QModelIndex,
    ) -> PySide2.QtWidgets.QWidget:
        editor = QCheckBox(parent)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        if not isinstance(value, bool):
            logging.warning("CheckBoxDelegate got passed non-bool type.")
            value = False
        editor.setChecked(value)

    def setModelData(
        self,
        editor: PySide2.QtWidgets.QCheckBox,
        model: PySide2.QtCore.QAbstractItemModel,
        index: PySide2.QtCore.QModelIndex,
    ):
        value = editor.isChecked()
        logging.debug(f"Setting model {model} with value {value}")
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(
        self,
        editor: PySide2.QtWidgets.QWidget,
        option: PySide2.QtWidgets.QStyleOptionViewItem,
        index: PySide2.QtCore.QModelIndex,
    ):
        editor.setGeometry(option.rect)
