import logging

from PySide2 import QtCore
from PySide2.QtCore import QAbstractTableModel, QModelIndex

from src.views.itemdeligates.checkboxdelegate import CheckBoxDelegate
from src.views.itemdeligates.spinboxdelegate import SpinBoxDelegate

logger = logging.getLogger(__name__)


class CustomTableItemType:
    columns_names = None
    delegates = {}

    def __init__(self, columns):
        self.columns = columns

    def get_column(self, column):
        return self.columns[column]

    def set_column(self, column, value):
        self.columns[column] = value


class Attack(CustomTableItemType):
    columns_names = {
        0: "Name",
        1: "Attack",
        2: "Damage",
        3: "Notes",
    }
    delegates = {}

    def __init__(self, name, attack, damage, notes):
        self.notes = notes
        self.damage = damage
        self.attack = attack
        self.name = name
        columns = [self.name, self.attack, self.damage, self.notes]

        super(Attack, self).__init__(columns)


class Equipment(CustomTableItemType):
    columns_names = {
        0: "Quantity",
        1: "Name",
        2: "Weight",
        3: "Attuned",
    }
    delegates = {0: SpinBoxDelegate(0, 99999), 3: CheckBoxDelegate()}

    def __init__(self, name, quantity, weight, attuned=False):
        self.name = name
        self.quantity = quantity
        self.weight = weight
        self.attuned = attuned
        columns = [self.quantity, self.name, self.weight, self.attuned]

        super(Equipment, self).__init__(columns)


class Skill(CustomTableItemType):
    columns_names = {
        0: "Prof.",
        1: "Mod.",
        2: "Bonus",
        3: "Name",
        # 3: "Custom",
    }
    delegates = {}

    def __init__(self, prof, modifier, bonus, name, custom=False):
        self.prof = prof
        self.name = name
        self.modifier = modifier
        self.bonus = bonus
        columns = [self.prof, self.modifier, self.bonus, self.name]
        super(Skill, self).__init__(columns)


class SpellSlot(CustomTableItemType):
    columns_names = {
        0: "Level",
        1: "Number of slots",
        # 3: "Custom",
    }
    delegates = {}

    def __init__(self, level, n_slots):
        self.level = level
        self.n_slots = n_slots
        columns = [self.level, self.n_slots]
        super(SpellSlot, self).__init__(columns)


class Spell(CustomTableItemType):
    columns_names = {
        0: "Prepared",
        1: "Level",
        2: "Spell Name",
        3: "Source",
        4: "Save/Attack",
        5: "Time",
        6: "Range",
        7: "Components",
        8: "Duration",
        9: "Page Reference",
        10: "Notes",
    }
    delegates = {0: CheckBoxDelegate(), 1: SpinBoxDelegate(0, 99)}

    def __init__(
        self,
        prepared,
        name,
        source,
        save_hit,
        time,
        spell_range,
        components,
        duration,
        page,
        notes,
        level,
    ):
        self.prepared = prepared
        self.name = name
        self.notes = notes
        self.page = page
        self.duration = duration
        self.components = components
        self.spell_range = spell_range
        self.time = time
        self.save_hit = save_hit
        self.source = source
        self.level = level
        columns = [
            self.prepared,
            self.level,
            self.name,
            self.source,
            self.save_hit,
            self.time,
            self.spell_range,
            self.components,
            self.duration,
            self.page,
            self.notes,
        ]
        super(Spell, self).__init__(columns)


class CustomTableModel(QAbstractTableModel):
    def __init__(self, custom_table_item):
        super(CustomTableModel, self).__init__()
        self.items = []
        if type(custom_table_item) is not type(CustomTableItemType):
            logger.debug(f"Inserted custom_table_item invalid")
        self.headers = custom_table_item.columns_names
        self.delegates = custom_table_item.delegates

    def rowCount(self, parent):
        return len(self.items)

    def columnCount(self, parent):
        return len(self.headers)

    def headerData(
        self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...
    ):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.headers[section]
        else:
            return None

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignLeft
        elif role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self.items[index.row()].get_column(index.column())
        else:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:

            row = index.row()
            column = index.column()

            self.items[row].set_column(column, value)
            return True
        return False

    def add_item(self, item):
        index_to_insert = self.rowCount(QModelIndex())
        self.beginInsertRows(
            QModelIndex(), index_to_insert, index_to_insert + 1,
        )
        self.items.append(item)
        self.endInsertRows()

    def remove_item(self, index):
        self.beginRemoveRows(
            QModelIndex(), index, index + 1,
        )
        self.items.pop(index)
        self.endRemoveRows()

    def flags(self, index):
        return (
            QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsEnabled
            | QtCore.Qt.ItemIsSelectable
        )
