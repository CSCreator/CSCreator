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
