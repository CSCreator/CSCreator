from enum import Enum, auto


class Skills(Enum):
    ATHLETICS = auto()
    ACROBATICS = auto()
    ANIMALHANDLING = auto()
    ARCANA = auto()
    DECEPTION = auto()
    HISTORY = auto()
    INSIGHT = auto()
    INTIMIDATION = auto()
    INVESTIGATION = auto()
    MEDICINE = auto()
    NATURE = auto()
    PERCEPTION = auto()
    PERFORMANCE = auto()
    PERSUASION = auto()
    RELIGION = auto()
    SLEIGHTOFHAND = auto()
    STEALTH = auto()
    SURVIVAL = auto()


class Abilities(Enum):
    STR = auto()
    DEX = auto()
    CON = auto()
    INT = auto()
    WIS = auto()
    CHA = auto()


class SkillProficiencies(Enum):
    No = auto()
    Half = auto()
    Prof = auto()
    Eff = auto()


class CHPropertyName(Enum):
    def _generate_next_value_(self, start: int, count: int, last_values: str) -> str:
        return "CH." + self


class CHProperty(CHPropertyName):
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


ch_reader_friendly_name = {
    CHProperty.CHARACTER_NAME: "Character Name",
    CHProperty.CLASS_LEVEL: "Class and Level",
    CHProperty.PLAYER_NAME: "Player Name",
    CHProperty.RACE: "Race",
    CHProperty.BACKGROUND: "Background",
    CHProperty.XP: "Experience",
    CHProperty.STR: "Strength",
    CHProperty.DEX: "Dexterity",
    CHProperty.CON: "Constitution",
    CHProperty.INT: "Intelligence",
    CHProperty.WIS: "Wisdom",
    CHProperty.CHA: "Charisme",
    CHProperty.STR_MOD: "Strength Modifier",
    CHProperty.DEX_MOD: "Dextirity Modifier",
    CHProperty.CON_MOD: "Constitution Modifier",
    CHProperty.INT_MOD: "Intelligence Modifier",
    CHProperty.WIS_MOD: "Wisdom Modifier",
    CHProperty.CHA_MOD: "Charisma Modifier",
    CHProperty.STR_ST_PROF: "Strength Saving Throw Proficiency",
    CHProperty.DEX_ST_PROF: "Dexterity Proficiency",
    CHProperty.CON_ST_PROF: "Constitution Proficiency",
    CHProperty.INT_ST_PROF: "Intelligence Saving Throw Proficiency",
    CHProperty.WIS_ST_PROF: "Wisdom Saving Throw Proficiency",
    CHProperty.CHA_ST_PROF: "Charisma Saving Throw Proficiency",
    CHProperty.STR_ST_MOD: "Strength Saving Throw Modifier",
    CHProperty.DEX_ST_MOD: "Dexterity Modifier",
    CHProperty.CON_ST_MOD: "Constitution Modifier",
    CHProperty.INT_ST_MOD: "Intelligence Saving Throw Modifier",
    CHProperty.WIS_ST_MOD: "Wisdom Saving Throw Modifier",
    CHProperty.CHA_ST_MOD: "Charisma Saving Throw Modifier",
    CHProperty.DEFENSES: "Defenses",
    CHProperty.SAVE_MODIFIERS: "Saving throw modifiers",
    CHProperty.PASSIVE_PERCEPTION: "Passive Perception",
    CHProperty.PASSIVE_WISDOM: "Passive Wisdom",
    CHProperty.PASSIVE_INVESTIGATION: "Passive Investigation",
    CHProperty.SENSES: "Senses",
    CHProperty.INITIATIVE: "Initiative modifier",
    CHProperty.AC: "Armor Class",
    CHProperty.PROF_BONUS: "Proficiency bonus",
    CHProperty.ABILITYSAVEDC1: "CH.ABILITYSAVEDC1",
    CHProperty.ABILITYSAVESCORE1: "CH.ABILITYSAVESCORE1",
    CHProperty.ABILITYSAVESCORE2: "CH.ABILITYSAVESCORE2",
    CHProperty.ABILITYSAVEDC2: "CH.ABILITYSAVEDC2",
    CHProperty.SPEED: "Speed",
    CHProperty.MAX_HP: "Maximum HP",
    CHProperty.CURRENT_HP: "Current HP",
    CHProperty.TEMP_HP: "Temporary HP",
    CHProperty.TOTAL_HIT_DICE: "Total Hit Dice",
    CHProperty.HIT_DICE: "Hit Dice Value",
    CHProperty.SUCCESSFUL_SAVE_1: None,
    CHProperty.SUCCESSFUL_SAVE_2: None,
    CHProperty.SUCCESSFUL_SAVE_3: None,
    CHProperty.FAILED_SAVE_1: None,
    CHProperty.FAILED_SAVE_2: None,
    CHProperty.FAILED_SAVE_3: None,
    CHProperty.PROFICIENCIES_LANGUAGES: "Proficiencies and Languages",
    CHProperty.ACTIONS: "Actions",
    CHProperty.ATTACKS: "Attacks",
    CHProperty.FEATURES_TRAITS: "Features & Traits",
    CHProperty.CP: "CP",
    CHProperty.SP: "SP",
    CHProperty.EP: "EP",
    CHProperty.GP: "GP",
    CHProperty.PP: "PP",
    CHProperty.WEIGHT_CARRIED: "Weight Carried",
    CHProperty.ENCUMBERED: "Encumbered",
    CHProperty.PUSH_DRAG_LIFT: "Push/drag/lift",
    CHProperty.GENDER: "Gender",
    CHProperty.AGE: "Age",
    CHProperty.SIZE: "Size",
    CHProperty.HEIGHT: "Height",
    CHProperty.WEIGHT: "Weight",
    CHProperty.ALIGNMENT: "Alignment",
    CHProperty.FAITH: "Faith",
    CHProperty.SKIN: "Skin",
    CHProperty.EYES: "Eyes",
    CHProperty.HAIR: "Hair",
    CHProperty.CHARACTER_IMAGE: "Character Image",
    CHProperty.ALLIES_ORGANIZATIONS: "Allies & Organizations",
    CHProperty.PERSONALITY_TRAITS: "Personlity Traits",
    CHProperty.IDEALS: "Ideals",
    CHProperty.BONDS: "Bonds",
    CHProperty.APPEARANCE: "Appearance",
    CHProperty.FLAWS: "Flaws",
    CHProperty.BACKSTORY: "Backstory",
    CHProperty.ADDITIONAL_NOTES: "Additional Notes",
    CHProperty.SPELLCASTINGABILITY0: "Spellcasting Ability",
    CHProperty.SPELLSAVEDC0: "Spell Save DC",
    CHProperty.SPELLATKBONUS0: "Spell Attack Bonus",
    CHProperty.SPELLCASTINGCLASS0: "Spellcasting Class",
}

ch_property_type = {
    CHProperty.CHARACTER_NAME: str,
    CHProperty.CLASS_LEVEL: str,
    CHProperty.PLAYER_NAME: str,
    CHProperty.RACE: str,
    CHProperty.BACKGROUND: str,
    CHProperty.XP: int,
    CHProperty.STR: int,
    CHProperty.DEX: int,
    CHProperty.CON: int,
    CHProperty.INT: int,
    CHProperty.WIS: int,
    CHProperty.CHA: int,
    CHProperty.STR_MOD: int,
    CHProperty.DEX_MOD: int,
    CHProperty.CON_MOD: int,
    CHProperty.INT_MOD: int,
    CHProperty.WIS_MOD: int,
    CHProperty.CHA_MOD: int,
    CHProperty.STR_ST_PROF: bool,
    CHProperty.DEX_ST_PROF: bool,
    CHProperty.CON_ST_PROF: bool,
    CHProperty.INT_ST_PROF: bool,
    CHProperty.WIS_ST_PROF: bool,
    CHProperty.CHA_ST_PROF: bool,
    CHProperty.STR_ST_MOD: int,
    CHProperty.DEX_ST_MOD: int,
    CHProperty.CON_ST_MOD: int,
    CHProperty.INT_ST_MOD: int,
    CHProperty.WIS_ST_MOD: int,
    CHProperty.CHA_ST_MOD: int,
    CHProperty.DEFENSES: str,
    CHProperty.SAVE_MODIFIERS: str,
    CHProperty.PASSIVE_PERCEPTION: int,
    CHProperty.PASSIVE_WISDOM: int,
    CHProperty.PASSIVE_INVESTIGATION: int,
    CHProperty.SENSES: str,
    CHProperty.INITIATIVE: int,
    CHProperty.AC: int,
    CHProperty.PROF_BONUS: int,
    CHProperty.ABILITYSAVEDC1: int,
    CHProperty.ABILITYSAVESCORE1: str,
    CHProperty.ABILITYSAVESCORE2: str,
    CHProperty.ABILITYSAVEDC2: int,
    CHProperty.SPEED: int,
    CHProperty.MAX_HP: int,
    CHProperty.CURRENT_HP: int,
    CHProperty.TEMP_HP: int,
    CHProperty.TOTAL_HIT_DICE: str,
    CHProperty.HIT_DICE: str,
    CHProperty.SUCCESSFUL_SAVE_1: bool,
    CHProperty.SUCCESSFUL_SAVE_2: bool,
    CHProperty.SUCCESSFUL_SAVE_3: bool,
    CHProperty.FAILED_SAVE_1: bool,
    CHProperty.FAILED_SAVE_2: bool,
    CHProperty.FAILED_SAVE_3: bool,
    CHProperty.PROFICIENCIES_LANGUAGES: str,
    CHProperty.ACTIONS: str,
    CHProperty.FEATURES_TRAITS: str,
    CHProperty.CP: int,
    CHProperty.SP: int,
    CHProperty.EP: int,
    CHProperty.GP: int,
    CHProperty.PP: int,
    CHProperty.WEIGHT_CARRIED: str,
    CHProperty.ENCUMBERED: str,
    CHProperty.PUSH_DRAG_LIFT: str,
    CHProperty.GENDER: str,
    CHProperty.AGE: str,
    CHProperty.SIZE: str,
    CHProperty.HEIGHT: str,
    CHProperty.WEIGHT: str,
    CHProperty.ALIGNMENT: str,
    CHProperty.FAITH: str,
    CHProperty.SKIN: str,
    CHProperty.EYES: str,
    CHProperty.HAIR: str,
    CHProperty.CHARACTER_IMAGE: str,
    CHProperty.ALLIES_ORGANIZATIONS: str,
    CHProperty.PERSONALITY_TRAITS: str,
    CHProperty.IDEALS: str,
    CHProperty.BONDS: str,
    CHProperty.APPEARANCE: str,
    CHProperty.FLAWS: str,
    CHProperty.BACKSTORY: str,
    CHProperty.ADDITIONAL_NOTES: str,
    CHProperty.SPELLCASTINGABILITY0: str,
    CHProperty.SPELLSAVEDC0: str,
    CHProperty.SPELLATKBONUS0: int,
    CHProperty.SPELLCASTINGCLASS0: int,
}