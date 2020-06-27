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
        ui = PdfDialog(parent, exporters_names)
        ui.importer_label.setText("Exporter")
        ui.setWindowTitle("Export Character Sheet")
        ui.selected_label.setText(file_name[0])
        status = ui.exec()
        selected_importer_file_index = exporters_files[ui.importer_selected]

        if status == QDialog.Accepted:
            self.export_new_player(file_name[0], selected_importer_file_index)
