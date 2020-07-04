
from src.data.pluginmanager import Plugin
from src.importers.pdfimporter import PDFImporter


def test_dnd_beyond_import() -> None:
    importer = PDFImporter(plugin=Plugin("src/data/importers/dndbeyond.json"))
    importer.load("pdfs/dndbeyond.pdf")
    player_controller = importer.player
    assert player_controller
