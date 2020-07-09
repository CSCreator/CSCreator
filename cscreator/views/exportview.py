import logging

from PySide2.QtWidgets import (
    QFileDialog,
    QDialog,
)
from obsub import event

from cscreator.views.pdfdialog import PdfDialog

logger = logging.getLogger(__name__)

from PySide2.QtCore import QStandardPaths


def ask_for_filename_to_save(parent):
    dir_to_open = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    fname = QFileDialog().getSaveFileName(
        parent, "Save as PDF", dir_to_open, "PDF Files (*.pdf)"
    )

    return fname


class ExportPdfWizardFactory:
    def __init__(self):
        self.plugin_manager = None

    @event
    def export_new_player(self, file, importer):
        logger.info(f"New export request for {file} with {importer}")

    def create(self, parent):
        logger.info("Opening Export PDF Wizard")
        file_name = ask_for_filename_to_save(parent)
        exporters = self.plugin_manager.exporters
        ui = PdfDialog(parent, [exporter.name for exporter in exporters])
        ui.importer_label.setText("Exporter")
        ui.setWindowTitle("Export Character Sheet")
        ui.selected_label.setText(file_name[0])
        status = ui.exec()
        selected_exporter = exporters[ui.importer_selected]

        if status == QDialog.Accepted:
            self.export_new_player(file_name[0], selected_exporter)
