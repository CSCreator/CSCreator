import logging
import uuid
from typing import List

from PySide2.QtWidgets import QHBoxLayout, QLayout

from src.models.charactermodel import CharacterModel
from src.models.charactersubmodel import (
    CustomTableModel,
    CustomTableItemType,
    Equipment,
    Spell,
    SpellSlot,
    Skill,
    Attack,
    WeaponProf,
    ArmorProf,
    LanguageProf,
    ToolProf,
)
from src.views.charactersubview import get_view_for_submodel
from src.views.characterview import CharacterView

logger = logging.getLogger(__name__)


class CharacterController:
    def __init__(self) -> None:
        self.uid = uuid.uuid4()
        self.player_model = CharacterModel()
        self.character_view = CharacterView(self.player_model)

        layout_per_submodel = {
            self.character_view.char_layout.EQUIPMENT_LAYOUT: self.player_model.conversion[
                Equipment
            ],
            self.character_view.char_layout.SPELL_LAYOUT: self.player_model.conversion[
                Spell
            ],
            self.character_view.char_layout.SPELLSLOT_LAYOUT: self.player_model.conversion[
                SpellSlot
            ],
            self.character_view.char_layout.ATTACK_LAYOUT: self.player_model.conversion[
                Attack
            ],
            self.character_view.char_layout.SKILL_LAYOUT: self.player_model.conversion[
                Skill
            ],
            self.character_view.char_layout.WEAPONS_LAYOUT: self.player_model.conversion[
                WeaponProf
            ],
            self.character_view.char_layout.ARMOR_LAYOUT: self.player_model.conversion[
                ArmorProf
            ],
            self.character_view.char_layout.LANGUAGES_LAYOUT: self.player_model.conversion[
                LanguageProf
            ],
            self.character_view.char_layout.TOOLS_LAYOUT: self.player_model.conversion[
                ToolProf
            ],
        }

        for layout, submodel in layout_per_submodel.items():
            layout.addWidget(get_view_for_submodel(submodel))

        # Invoke character_model_changed_event when set_value is called
        self.player_model.set_value += self.character_view.character_model_changed_event

        # All chracter_properties in the view are linked to the model here
        self.character_view.register_signals(self.player_model)

    def get_models(self) -> List[CustomTableModel]:
        return self.player_model.conversion.keys()

    def get_item(
        self, item_type: CustomTableItemType, index: int
    ) -> CustomTableItemType:
        return self.player_model.get_item(item_type, index)

    def get_items(self, item_type: CustomTableItemType) -> List[CustomTableItemType]:
        return self.player_model.get_items(item_type)

    def add_item(
        self, item_type: CustomTableItemType, item: CustomTableItemType
    ) -> None:
        self.player_model.add_item(item_type, item)

    def get_layout(self) -> QLayout:
        layout = QHBoxLayout()
        layout.addWidget(self.character_view, 1)
        return layout
