import logging

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QTableView,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QDialog,
    QFormLayout,
    QLineEdit,
    QDialogButtonBox,
    QAbstractItemView,
)

logger = logging.getLogger(__name__)


def add_item_to_model(submodel):
    dialog = QDialog()
    v_layout = QVBoxLayout()
    form_layout = QFormLayout()

    item_type = submodel.custom_table_item
    item_columns = item_type.columns_names
    widget_per_column = {}
    for index, name in item_columns.items():
        line_edit = QLineEdit()
        form_layout.addRow(name, line_edit)
        widget_per_column[name] = line_edit

    button_box = QDialogButtonBox()
    button_box.setObjectName("buttonBox")
    button_box.setOrientation(Qt.Horizontal)
    button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)

    v_layout.addLayout(form_layout)
    v_layout.addWidget(button_box)

    dialog.forms = form_layout
    dialog.setLayout(v_layout)

    status = dialog.exec()
    if status == QDialog.Accepted:
        new_item = item_type()
        for index, name in new_item.columns_names.items():
            value_of_row = widget_per_column[name].text()

            new_item.set_column(index, value_of_row)
        submodel.add_item(new_item)
        logger.info(f"New item of type {item_type} added")


def remove_item_from_model(submodel, tableview):
    selection_model = tableview.selectionModel()
    if selection_model.hasSelection():
        model_index = selection_model.selectedRows()[0]
        index = model_index.row()
        submodel.remove_item(index)


def get_view_for_submodel(submodel):
    main_widget = QWidget()

    hbox_layout = QHBoxLayout(main_widget)
    vbox_layout = QVBoxLayout()

    table_view = QTableView()
    table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
    table_view.setSelectionMode(QAbstractItemView.SingleSelection)
    table_view.setModel(submodel)

    add_button = QPushButton("+")
    add_button.clicked.connect(lambda: add_item_to_model(submodel))

    remove_button = QPushButton("-")
    remove_button.clicked.connect(lambda: remove_item_from_model(submodel, table_view))

    vbox_layout.addWidget(add_button)
    vbox_layout.addWidget(remove_button)
    vbox_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    hbox_layout.addWidget(table_view)
    hbox_layout.addLayout(vbox_layout)

    return main_widget
