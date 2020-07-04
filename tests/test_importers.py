import sys

from PySide2.QtWidgets import QApplication

from src.data.pluginmanager import PluginManager
from src.importers.pdfimporter import PDFImporter


def test_dnd_beyond_import() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("CSCreator")

    plugin_manager = PluginManager()
    plugin = plugin_manager.get_importer("DND Beyond")
    importer = PDFImporter(plugin=plugin)
    importer.load("pdfs/dndbeyond.pdf")
    player_controller = importer.player
    assert player_controller
