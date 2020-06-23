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


class ImportPdfDialog(QDialog):
    def __init__(self, parent, importers_stringlist):
        super(ImportPdfDialog, self).__init__(parent)
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
        self.importer_label.setObjectName("importer_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.importer_label)

        self.importer_combo_box = QComboBox(self)
        self.importer_combo_box.setObjectName("importer_combo_box")
        self.importer_combo_box.addItems(importers_stringlist)

        def set_importer_selected(x):
            self.importer_selected = x

        self.importer_combo_box.currentIndexChanged.connect(set_importer_selected)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.importer_combo_box)

        self.selected_label = QLabel(self)
        self.selected_label.setObjectName("selected_label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.selected_label)

        self.importer_status = QLabel(self)
        self.importer_status.setObjectName("importer_status")

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
            QCoreApplication.translate("dialog", "Import Character Sheet", None)
        )
        self.selected_file_label.setText(
            QCoreApplication.translate("dialog", "Selected File", None)
        )
        self.importer_label.setText(
            QCoreApplication.translate("dialog", "Importer", None)
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
    fname = QFileDialog.getOpenFileName(
        parent, "Open PDF", dir_to_open, "PDF Files (*.pdf)"
    )

    return fname


def find_importers():
    dir_to_search = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
    dir_to_search = os.path.join(dir_to_search, "importers")
    importer_names = []
    importer_files = []
    for file in os.listdir(dir_to_search):
        if file.endswith(".json"):
            file = os.path.join(dir_to_search, file)
            try:
                with open(file, "r") as j:
                    definition = json.loads(j.read())
                    name = definition.get("importer_name", None)
                    if not name:
                        logging.warning(
                            f"JSON file {file}found in importers dir, but no importer_name present"
                        )
                    else:
                        importer_names.append(name)
                        importer_files.append(file)
            except Exception:
                logging.warning(f"JSON file {file} found but not openable")

    return importer_names, importer_files


class PdfWizardFactory:

    @event
    def import_new_player(self, file, importer):
        logger.info(f"New import request for {file} with {importer}")

    def create(self, parent):
        logger.info("Opening Import PDF Wizard")
        file_name = do_file(parent)
        importer_names, importer_files = find_importers()
        ui = ImportPdfDialog(parent, importer_names)
        ui.selected_label.setText(file_name[0])
        status = ui.exec()
        selected_importer_file_index = importer_files[ui.importer_selected]

        if status == QDialog.Accepted:
            self.import_new_player(file_name[0], selected_importer_file_index)
