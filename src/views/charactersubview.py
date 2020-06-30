from PySide2.QtWidgets import QTableView, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy

def get_view_for_submodel(submodel):
    main_widget = QWidget()
    hbox_layout = QHBoxLayout(main_widget)

    table_view = QTableView()
    table_view.setModel(submodel)
    hbox_layout.addWidget(table_view)

    vbox_layout = QVBoxLayout()
    add_button = QPushButton("+")
    vbox_layout.addWidget(add_button)
    vbox_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
    hbox_layout.addLayout(vbox_layout)

    return main_widget