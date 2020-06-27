import json
import logging
import os

from PySide2.QtWidgets import QFileDialog, QDialog, QVBoxLayout, QFormLayout, QLabel, QComboBox, QDialogButtonBox
from obsub import event

logger = logging.getLogger(__name__)

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
    QStandardPaths,
)


class ExportPdfDialog(QDialog):
    def __init__(self, parent, importers_stringlist):
        super(ExportPdfDialog, self).__init__(parent)
        self.resize(320, 240)

        self.importer_selected = 0

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.selected_file_label = QLabel(self)
        self.selected_file_label.setObjectName("selected_file_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.selected_file_label)

        self.importer_label = QLabel(self)
        self.importer_label.setObjectName("exporter_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.importer_label)

        self.importer_combo_box = QComboBox(self)
        self.importer_combo_box.setObjectName("exporter_combo_box")
        self.importer_combo_box.addItems(importers_stringlist)

        def set_importer_selected(x):
            self.importer_selected = x

        self.importer_combo_box.currentIndexChanged.connect(set_importer_selected)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.importer_combo_box)

        self.selected_label = QLabel(self)
        self.selected_label.setObjectName("selected_label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.selected_label)

        self.importer_status = QLabel(self)
        self.importer_status.setObjectName("exporter_status")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.importer_status)

        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(
            QCoreApplication.translate("dialog", "Export Character Sheet", None)
        )
        self.selected_file_label.setText(
            QCoreApplication.translate("dialog", "File", None)
        )
        self.importer_label.setText(
            QCoreApplication.translate("dialog", "Exporter", None)
        )
        self.selected_label.setText(
            QCoreApplication.translate("dialog", "TextLabel", None)
        )
        self.importer_status.setText(
            QCoreApplication.translate("dialog", "TextLabel", None)
        )

    # retranslateUi


def do_file(parent):
    dir_to_open = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    fname = QFileDialog().getSaveFileName(
        parent, "Save as PDF", dir_to_open, "PDF Files (*.pdf)"
    )

    return fname


def find_exporters():
    dir_to_search = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
    dir_to_search = os.path.join(dir_to_search, "exporters")
    importer_names = []
    importer_files = []
    for file in os.listdir(dir_to_search):
        if file.endswith(".json"):
            file = os.path.join(dir_to_search, file)
            try:
                with open(file, "r") as j:
                    definition = json.loads(j.read())
                    name = definition.get("exporter_name", None)
                    if not name:
                        logging.warning(
                            f"JSON file {file}found in exporters dir, but no exporter_name present"
                        )
                    else:
                        importer_names.append(name)
                        importer_files.append(file)
            except Exception:
                logging.warning(f"JSON file {file} found but not openable")

    return importer_names, importer_files


class ExportPdfWizardFactory:

    @event
    def export_new_player(self, file, importer):
        logger.info(f"New export request for {file} with {importer}")

    def create(self, parent):
        logger.info("Opening Export PDF Wizard")
        file_name = do_file(parent)
        exporters_names, exporters_files = find_exporters()
        ui = ExportPdfDialog(parent, exporters_names)
        ui.selected_label.setText(file_name[0])
        status = ui.exec()
        selected_importer_file_index = exporters_files[ui.importer_selected]

        if status == QDialog.Accepted:
            self.export_new_player(file_name[0], selected_importer_file_index)
