from src.data.pluginmanager import Plugin
from src.importers.pdfimporter import PDFImporter


def test_dnd_beyond_import(qtbot) -> None:
    importer = PDFImporter(plugin=Plugin("src/data/importers/dndbeyond.json"))
    print(importer)
    importer.load("tests/pdfs/dndbeyond.pdf")
    player_controller = importer.player
    assert player_controller
