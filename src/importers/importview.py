import json
import logging
import os

from PySide2.QtWidgets import QFileDialog, QDialog, QVBoxLayout, QFormLayout, QLabel, QComboBox, QDialogButtonBox
from obsub import event

from src.views.pdfdialog import PdfDialog

logger = logging.getLogger(__name__)

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
    QStandardPaths,
)

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
        ui = PdfDialog(parent, importer_names)
        ui.importer_label.setText("Importer")
        ui.setWindowTitle("Import Character Sheet")
        ui.selected_label.setText(file_name[0])
        status = ui.exec()
        selected_importer_file_index = importer_files[ui.importer_selected]

        if status == QDialog.Accepted:
            self.import_new_player(file_name[0], selected_importer_file_index)
