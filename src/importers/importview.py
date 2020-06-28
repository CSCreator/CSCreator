import json
import logging
import os

from PySide2.QtWidgets import QFileDialog, QDialog
from obsub import event

from src.views.pdfdialog import PdfDialog

logger = logging.getLogger(__name__)

from PySide2.QtCore import QStandardPaths


def do_file(parent):
    dir_to_open = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    fname = QFileDialog.getOpenFileName(
        parent, "Open PDF", dir_to_open, "PDF Files (*.pdf)"
    )

    return fname


class PdfWizardFactory:
    def __init__(self):
        self.plugin_manager = None

    @event
    def import_new_player(self, file, importer):
        logger.info(f"New import request for {file} with {importer}")

    def create(self, parent):
        logger.info("Opening Import PDF Wizard")
        file_name = do_file(parent)
        importers = self.plugin_manager.importers
        ui = PdfDialog(parent, [importer.name for importer in importers])
        ui.importer_label.setText("Importer")
        ui.setWindowTitle("Import Character Sheet")
        ui.selected_label.setText(file_name[0])
        status = ui.exec()
        selected_importer = importers[ui.importer_selected]

        if status == QDialog.Accepted:
            self.import_new_player(file_name[0], selected_importer)
