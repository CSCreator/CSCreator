import logging

from src.controllers.charactercontroller import CharacterController
from src.data.pluginmanager import PluginManager, Plugin
from src.exporters.pdfexporter import PDFExporter

logger = logging.getLogger(__name__)

from src.controllers.collectioncontroller import CollectionController
from src.importers.pdfimporter import PDFImporter
from src.views.mainview import MainView


class MainController:
    def __init__(self):

        self.main_view = MainView()
        self.collection_controller = CollectionController()
        self.plugin_manager = PluginManager()

        self.main_view.pdf_wizard_factory.plugin_manager = self.plugin_manager
        self.main_view.pdf_wizard_factory.import_new_player += (
            self.import_player_handler
        )
        self.main_view.export_pdf_wizard_factory.plugin_manager = self.plugin_manager
        self.main_view.export_pdf_wizard_factory.export_new_player += (
            self.export_player_handler
        )
        self.main_view.create_new_player += self.new_player_handler
        self.collection_controller.add_player += self.player_added_handler

        self.import_player(
            file_name="resc/dndbeyond_extreme.pdf",
            plugin=Plugin("src/data/importers/dndbeyond.json"),
        )

        self.set_sheet_layout()

    def set_player_tab(self):
        layout = self.collection_controller.get_character_layout()
        self.main_view.set_character_layout(layout)

    def set_sheet_layout(self):
        layout = self.collection_controller.get_sheet_layout()
        self.main_view.set_sheet_layout(layout)

    def get_window(self):
        return self.main_view

    def import_player_handler(self, subject, file_name, importer):
        self.import_player(file_name, importer)

    def new_player_handler(self, subject):
        player = CharacterController()
        self.collection_controller.add_player(player)

    def import_player(
        self, file_name, plugin,
    ):
        importer = PDFImporter(plugin=plugin)
        importer.load(file_name)
        player_controller = importer.player
        self.collection_controller.add_player(player_controller)

    def player_added_handler(self, subject, arg):
        self.set_player_tab()

    def export_player_handler(self, subject, file_name, exporter):
        current_player = self.collection_controller.character_controllers
        exporter = PDFExporter(current_player, file_name, exporter)
        exporter.export()
