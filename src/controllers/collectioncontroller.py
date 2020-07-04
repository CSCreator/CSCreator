import logging

from PySide2.QtWidgets import QHBoxLayout
from obsub import event

from src.controllers.sheetcontroller import SheetController
from src.views.stagingview import StagingView
from src.models.characterenums import CHProperty
logger = logging.getLogger(__name__)


class CollectionController:
    def __init__(self):
        self.character_controllers = None
        self.active_character_controller = None
        self.sheet_controller = SheetController(self.active_character_controller)

    @event
    def add_player(self, player):
        self.character_controllers = player
        logger.info(f"Added player {player.player_model.get_ch_property(CHProperty.CHARACTER_NAME)}")

    @event
    def remove_player(self, player):
        self.character_controllers = None
        logger.info(f"Removed player {player.player_model.CHARACTER_NAME}")

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
