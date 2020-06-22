from enum import Enum, auto
import logging

from obsub import event

from src.models.charactersubmodel import (
    CustomTableModel,
    Equipment,
    Spell,
    Attack,
    Skill,
    SpellSlot,
)

logger = logging.getLogger(__name__)


class CHName(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return "CH." + self


class CH(CHName):
    # Character Info
    CHARACTER_NAME = auto()
    CLASS_LEVEL = auto()
    PLAYER_NAME = auto()
    RACE = auto()
    BACKGROUND = auto()
    XP = auto()
    # Abilities and proficiencies
    STR = auto()
    DEX = auto()
    CON = auto()
    INT = auto()
    WIS = auto()
    CHA = auto()
    STR_MOD = auto()
    DEX_MOD = auto()
    CON_MOD = auto()
    INT_MOD = auto()
    WIS_MOD = auto()
    CHA_MOD = auto()
    # Saving throws prof
    STR_ST_PROF = auto()
    DEX_ST_PROF = auto()
    CON_ST_PROF = auto()
    INT_ST_PROF = auto()
    WIS_ST_PROF = auto()
    CHA_ST_PROF = auto()
    # Saving throws mods
    STR_ST_MOD = auto()
    DEX_ST_MOD = auto()
    CON_ST_MOD = auto()
    INT_ST_MOD = auto()
    WIS_ST_MOD = auto()
    CHA_ST_MOD = auto()
    # Defenses and resistances
    DEFENSES = auto()
    SAVE_MODIFIERS = auto()
    # Passive
    PASSIVE_PERCEPTION = auto()
    PASSIVE_WISDOM = auto()
    PASSIVE_INVESTIGATION = auto()
    SENSES = auto()
    INITIATIVE = auto()
    AC = auto()
    PROF_BONUS = auto()
    ABILITYSAVEDC1 = auto()
    ABILITYSAVESCORE1 = auto()
    ABILITYSAVESCORE2 = auto()
    ABILITYSAVEDC2 = auto()
    SPEED = auto()
    MAX_HP = auto()
    CURRENT_HP = auto()
    TEMP_HP = auto()
    TOTAL_HIT_DICE = auto()
    HIT_DICE = auto()
    # TODO Verify order
    SUCCESSFUL_SAVE_1 = auto()
    SUCCESSFUL_SAVE_2 = auto()
    SUCCESSFUL_SAVE_3 = auto()
    FAILED_SAVE_1 = auto()
    FAILED_SAVE_2 = auto()
    FAILED_SAVE_3 = auto()
    PROFICIENCIES_LANGUAGES = auto()
    # Merge from two boxes
    ACTIONS = auto()
    ATTACKS = auto()
    # Merged from 3 boxes
    FEATURES_TRAITS = auto()
    CP = auto()
    SP = auto()
    EP = auto()
    GP = auto()
    PP = auto()
    WEIGHT_CARRIED = auto()
    ENCUMBERED = auto()
    PUSH_DRAG_LIFT = auto()
    GENDER = auto()
    AGE = auto()
    SIZE = auto()
    HEIGHT = auto()
    WEIGHT = auto()
    ALIGNMENT = auto()
    FAITH = auto()
    SKIN = auto()
    EYES = auto()
    HAIR = auto()
    CHARACTER_IMAGE = auto()
    ALLIES_ORGANIZATIONS = auto()
    PERSONALITY_TRAITS = auto()
    IDEALS = auto()
    BONDS = auto()
    APPEARANCE = auto()
    FLAWS = auto()
    BACKSTORY = auto()
    ADDITIONAL_NOTES = auto()
    SPELLCASTINGABILITY0 = auto()
    SPELLSAVEDC0 = auto()
    SPELLATKBONUS0 = auto()
    SPELLCASTINGCLASS0 = auto()
    SPELL_SLOTS_0 = auto()
    SPELL_SLOTS_1 = auto()
    SPELL_SLOTS_2 = auto()
    SPELL_SLOTS_3 = auto()
    SPELL_SLOTS_4 = auto()
    SPELL_SLOTS_5 = auto()
    SPELL_SLOTS_6 = auto()
    SPELL_SLOTS_7 = auto()
    SPELL_SLOTS_8 = auto()
    SPELL_SLOTS_9 = auto()
    SPELL_SLOTS_10 = auto()


class SkillProficiencies(Enum):
    No = auto()
    Half = auto()
    Prof = auto()
    Eff = auto()


class CharacterModel:
    def __init__(self):
        for value in CH:
            setattr(self, value.name, None)

        self.equipment_model = CustomTableModel(Equipment)
        self.spell_model = CustomTableModel(Spell)
        self.attack_model = CustomTableModel(Attack)
        self.skills_model = CustomTableModel(Skill)
        self.spellslot_model = CustomTableModel(SpellSlot)

    @event
    def set_value(self, value_name, value):
        setattr(self, value_name, value)

    def character_view_changed_event(self, character_property, value):
        # Do not call set_value here, otherwise we fire an event back to the View, who has the latest character_property already
        setattr(self, character_property.name, value)
        logger.debug(
            f"Recieved changed character_property {character_property.name} from the view with value {value}"
        )
