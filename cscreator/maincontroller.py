import logging

from PySide2.QtWidgets import QHBoxLayout
from obsub import event

from cscreator.character.charactercontroller import CharacterController
from cscreator.character.characterenums import CHProperty
from cscreator.conversion.pdfexporter import PDFExporter
from cscreator.conversion.pluginmanager import PluginManager
from cscreator.plugins.importers.dndbeyond import DNDBeyond
from cscreator.sheet.sheetcontroller import SheetController
from cscreator.views.mainview import MainView
from cscreator.views.stagingview import StagingView

logger = logging.getLogger(__name__)

from cscreator.conversion.pdfimporter import PDFImporter


class MainController:
    def __init__(self):
        self.character_controllers = None

        self.main_view = MainView()
        self.plugin_manager = PluginManager()
        self.import_player(
            file_name="resc/dndbeyond_extreme.pdf", plugin=DNDBeyond(),
        )
        self.main_view.pdf_wizard_factory.plugin_manager = self.plugin_manager
        self.main_view.pdf_wizard_factory.import_new_player += (
            self.import_player_handler
        )
        self.main_view.export_pdf_wizard_factory.plugin_manager = self.plugin_manager
        self.main_view.export_pdf_wizard_factory.export_new_player += (
            self.export_player_handler
        )

        self.main_view.create_new_player += self.new_player_handler

        self.sheet_controller = SheetController(self.character_controllers)
        self.set_sheet_layout()

    def new_player_handler(self, subject):
        character = CharacterController()
        self.add_player(character)
        self.set_player_tab()

    @event
    def add_player(self, player):
        self.character_controllers = player
        self.set_player_tab()
        logger.info(
            f"Added player {player.player_model.get_ch_property(CHProperty.CHARACTER_NAME)}"
        )

    @event
    def remove_player(self, player):
        self.character_controllers = None
        logger.info(
            f"Removed player {player.player_model.get_ch_property(CHProperty.CHARACTER_NAME)}"
        )

    def get_character_layout(self):
        qt_layout = self.character_controllers.get_layout()
        return qt_layout

    def get_sheet_layout(self):
        self.layout = QHBoxLayout()
        self.staging_widget = StagingView()
        self.staging_layout = QHBoxLayout()
        self.staging_layout.addWidget(self.staging_widget)
        self.layout.addLayout(self.staging_layout, 1)
        self.layout.addLayout(self.sheet_controller.get_layout(), 1)
        return self.layout

    def set_player_tab(self):
        layout = self.get_character_layout()
        self.main_view.set_character_layout(layout)

    def set_sheet_layout(self):
        self.main_view.set_sheet_layout(self.get_sheet_layout())

    def get_window(self):
        return self.main_view

    def import_player_handler(self, subject, file_name, importer):
        self.import_player(file_name, importer)

    def import_player(
        self, file_name, plugin,
    ):
        importer = PDFImporter(plugin=plugin)
        importer.load(file_name)
        player_controller = importer.player
        self.add_player(player_controller)

    def export_player_handler(self, subject, file_name, exporter):
        current_player = self.collection_controller.character_controllers
        exporter = PDFExporter(current_player, file_name, exporter)
        exporter.export()
