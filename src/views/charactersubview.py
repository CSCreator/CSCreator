from PySide2.QtCore import Qt
from PySide2.QtWidgets import QTableView, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QDialog, QFormLayout, QLineEdit, QDialogButtonBox


def add_item_to_model(submodel):
    item_type = submodel.custom_table_item
    item_columns = item_type.columns_names

    dialog = QDialog()
    v_layout = QVBoxLayout()
    form_layout = QFormLayout()

    widget_per_column = {}
    for index, name in item_columns.items():
        line_edit = QLineEdit()
        form_layout.addRow(name, line_edit)
        widget_per_column[name] = line_edit
    v_layout.addLayout(form_layout)

    buttonBox = QDialogButtonBox()
    buttonBox.setObjectName("buttonBox")
    buttonBox.setOrientation(Qt.Horizontal)
    buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

    v_layout.addWidget(buttonBox)

    buttonBox.accepted.connect(dialog.accept)
    buttonBox.rejected.connect(dialog.reject)
    dialog.forms = form_layout
    dialog.setLayout(v_layout)

    status = dialog.exec()
    if status == QDialog.Accepted:
        new_item = item_type()
        for index, name in new_item.columns_names.items():
            value_of_row = widget_per_column[name].text()

            new_item.set_column(index, value_of_row)
        submodel.add_item(new_item)

    pass


def get_view_for_submodel(submodel):
    main_widget = QWidget()
    hbox_layout = QHBoxLayout(main_widget)

    table_view = QTableView()
    table_view.setModel(submodel)
    hbox_layout.addWidget(table_view)

    vbox_layout = QVBoxLayout()
    add_button = QPushButton("+")
    add_button.clicked.connect(lambda: add_item_to_model(submodel))
    vbox_layout.addWidget(add_button)
    vbox_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
    hbox_layout.addLayout(vbox_layout)

    return main_widget