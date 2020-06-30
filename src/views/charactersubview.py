from PySide2.QtWidgets import QTableView, QWidget


def get_view_for_submodel(submodel):
    table_view = QTableView()
    table_view.setModel(submodel)
    return table_view