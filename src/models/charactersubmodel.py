import logging
import sys
from typing import Iterator, Dict, Any, Union

from PySide2 import QtCore
from PySide2.QtCore import QAbstractTableModel, QModelIndex
from PySide2.QtWidgets import QStyledItemDelegate

from exceptions import InvalidPropertyType
from src.views.itemdeligates.checkboxdelegate import CheckBoxDelegate
from src.views.itemdeligates.spinboxdelegate import SpinBoxDelegate

logger = logging.getLogger(__name__)

def standard_type_conversion(value, type):
    try:
        if isinstance(value, type):
            return value
        elif isinstance(value, str) and type is bool:
            return bool(value)
        elif value is None and type is bool:
            return False
        elif isinstance(value, int) and type is str:
            return str(value)
        elif value == '' and type is int:
            return 0
        elif isinstance(value, str) and type is int:
            return int(value)
        else:
            return value
    except ValueError:
        logger.error(f"Value {value} cannot be casted to {type}")
        return None

class CustomTableItemType:
    columns_names: Dict[int, str] = {}
    columns_types: Dict[int, type] = {}
    delegates: Dict[int, QStyledItemDelegate] = {}

    def __init__(self, **kwargs):
        self.named_item_enum = None
        self.columns = [None] * len(self.columns_names)
        for index, column in self.columns_names.items():
            value = kwargs.get(column, None)
            self.set_column(index, value)

    def get_column(self, column):
        return self.columns[column]

    def set_column(self, column, value):
        column_type = self.columns_types[column]
        value = standard_type_conversion(value, column_type)
        if not isinstance(value, column_type) and value is not None:
            raise InvalidPropertyType(f"Submodel of type {self.named_item_enum} column {column} is of type {column_type} while value being set is a {type(value)} {value}")
        self.columns[column] = value


class Attack(CustomTableItemType):
    columns_names: Dict[int, str] = {
        0: "name",
        1: "attack_bonus",
        2: "damage",
        3: "notes",
    }
    columns_types: Dict[int, type] = {
        0: str,
        1: str,
        2: str,
        3: str,
    }
    delegates: Dict[int, QStyledItemDelegate] = {}


class Equipment(CustomTableItemType):
    columns_names: Dict[int, str] = {
        0: "quantity",
        1: "name",
        2: "weight",
        3: "attuned",
    }
    columns_types: Dict[int, type] = {
        0: int,
        1: str,
        2: str,
        3: bool,
    }
    delegates: Dict[int, QStyledItemDelegate] = {
        0: SpinBoxDelegate(0, 99999),
        3: CheckBoxDelegate(),
    }


class Skill(CustomTableItemType):
    columns_names: Dict[int, str] = {
        0: "prof",
        1: "mod",
        2: "bonus",
        3: "name",
        # 3: "Custom",
    }
    columns_types: Dict[int, type] = {
        0: bool,
        1: str,
        2: int,
        3: str,
    }
    delegates: Dict[int, QStyledItemDelegate] = {}


class SpellSlot(CustomTableItemType):
    columns_names: Dict[int, str] = {
        0: "level",
        1: "n_slots",
        # 3: "Custom",
    }
    columns_types: Dict[int, type] = {
        0: int,
        1: int,
    }
    delegates: Dict[int, QStyledItemDelegate] = {}


class Spell(CustomTableItemType):
    columns_names: Dict[int, str] = {
        0: "prepared",
        1: "level",
        2: "name",
        3: "source",
        4: "save_hit",
        5: "time",
        6: "spell_range",
        7: "components",
        8: "duration",
        9: "page",
        10: "notes",
    }
    columns_types: Dict[int, type] = {
        0: bool,
        1: int,
        2: str,
        3: str,
        4: str,
        5: str,
        6: str,
        7: str,
        8: str,
        9: str,
        10: str,
    }
    delegates: Dict[int, QStyledItemDelegate] = {
        0: CheckBoxDelegate(),
        1: SpinBoxDelegate(0, 99),
    }


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


class CustomTableModel(QAbstractTableModel):
    def __init__(self, custom_table_item: CustomTableItemType) -> None:
        super(CustomTableModel, self).__init__()
        self.items = []
        if type(custom_table_item) is not type(CustomTableItemType):
            logger.debug(f"Inserted custom_table_item invalid")
        self.headers = custom_table_item.columns_names
        self.delegates = custom_table_item.delegates
        self.custom_table_item = custom_table_item

    def rowCount(self, parent: Any = None) -> int:
        return len(self.items)

    def columnCount(self, parent) -> int:
        return len(self.headers)

    def headerData(
        self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...
    ) -> Union[None, Dict[int, str]]:
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.headers[section]
        else:
            return None

    def data(self, index: int, role: QtCore.Qt) -> Any:
        if not index.isValid():
            return None
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignLeft
        elif role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self.items[index.row()].get_column(index.column())
        else:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole) -> bool:
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()

            self.items[row].set_column(column, value)
            return True
        return False

    def add_item(self, item) -> None:
        index_to_insert = self.rowCount(QModelIndex())
        self.beginInsertRows(
            QModelIndex(), index_to_insert, index_to_insert + 1,
        )
        self.items.append(item)
        self.endInsertRows()

    def remove_item(self, index: int) -> None:
        self.beginRemoveRows(
            QModelIndex(), index, index + 1,
        )
        self.items.pop(index)
        self.endRemoveRows()

    def flags(self, index: QModelIndex):
        return (
            QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsEnabled
            | QtCore.Qt.ItemIsSelectable
        )

    def get_item_at_row(self, index: int) -> CustomTableItemType:
        if index < self.rowCount():
            return self.items[index]

    def get_items(self) -> Iterator[CustomTableItemType]:
        index = 0
        while index < self.rowCount():
            yield self.get_item_at_row(index)
            index += 1
