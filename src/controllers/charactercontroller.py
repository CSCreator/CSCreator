import logging
import uuid

from PySide2.QtWidgets import QHBoxLayout

from src.models.charactermodel import (
    CharacterModel,
)
from src.views.characterview import CharacterView

logger = logging.getLogger(__name__)


class CharacterController:
    def __init__(self):
        self.uid = uuid.uuid4()
        self.player_model = CharacterModel()
        self.character_view = CharacterView(self.player_model)

        self.character_view.char_layout.EQUIPMENT_TABLE.setModel(
            self.player_model.equipment_model
        )

        self.character_view.char_layout.SPELL_TABLE.setModel(
            self.player_model.spell_model
        )

        self.character_view.char_layout.SPELLSLOT_TABLE.setModel(
            self.player_model.spellslot_model
        )

        self.character_view.char_layout.ATTACK_TABLE.setModel(
            self.player_model.attack_model
        )

        self.character_view.char_layout.SKILL_TABLE.setModel(
            self.player_model.skills_model
        )

        # Invoke character_model_changed_event when set_value is called
        self.player_model.set_value += self.character_view.character_model_changed_event

        # All chracter_properties in the view are linked to the model here
        self.character_view.register_signals(self.player_model)

    def get_item(self, item_type, index):
        return self.player_model.get_item(item_type, index)

    def add_item(self, item_type, item):
        return self.player_model.add_item(item_type, item)

    def get_skills(self):
        return self.player_model.skills

    def get_skill(self, name):
        return self.player_model.get_skill(name)

    def get_attack(self, index):
        return self.player_model.get_attack(index)

    def get_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.character_view, 1)
        return layout
