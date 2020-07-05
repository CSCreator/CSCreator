import pytest

from src.data.pluginmanager import Plugin
from src.importers.pdfimporter import PDFImporter
from src.models.characterenums import CHProperty, ch_property_type
from src.models.charactermodel import CharacterProperty


@pytest.fixture()
def standard_player():
    character_properties = {}

    for value in CHProperty:
        character_properties[value] = CharacterProperty(value, ch_property_type[value])

        character_properties[CHProperty.CHARACTER_NAME].value = "Tester 1"
        character_properties[CHProperty.CLASS_LEVEL].value = "Fighter 20"
        character_properties[CHProperty.PLAYER_NAME].value = "CSCreator"
        character_properties[CHProperty.RACE].value = "Human"
        character_properties[CHProperty.BACKGROUND].value = "Entertainer"
        character_properties[CHProperty.XP].value = "(Milestone)"
        character_properties[CHProperty.STR].value = 18
        character_properties[CHProperty.DEX].value = 14
        character_properties[CHProperty.CON].value = 14
        character_properties[CHProperty.INT].value = 16
        character_properties[CHProperty.WIS].value = 16
        character_properties[CHProperty.CHA].value = 11
        character_properties[CHProperty.STR_MOD].value = 4
        character_properties[CHProperty.DEX_MOD].value = 2
        character_properties[CHProperty.CON_MOD].value = 2
        character_properties[CHProperty.INT_MOD].value = 3
        character_properties[CHProperty.WIS_MOD].value = 3
        character_properties[CHProperty.CHA_MOD].value = 0
        character_properties[CHProperty.STR_ST_PROF].value = True
        character_properties[CHProperty.DEX_ST_PROF].value = False
        character_properties[CHProperty.CON_ST_PROF].value = True
        character_properties[CHProperty.INT_ST_PROF].value = False
        character_properties[CHProperty.WIS_ST_PROF].value = False
        character_properties[CHProperty.CHA_ST_PROF].value = False
        character_properties[CHProperty.STR_ST_MOD].value = 10
        character_properties[CHProperty.DEX_ST_MOD].value = 2
        character_properties[CHProperty.CON_ST_MOD].value = 8
        character_properties[CHProperty.INT_ST_MOD].value = 3
        character_properties[CHProperty.WIS_ST_MOD].value = 3
        character_properties[CHProperty.CHA_ST_MOD].value = 0
        character_properties[CHProperty.DEFENSES].value = "Defenses"
        character_properties[CHProperty.SAVE_MODIFIERS].value = "Saving throw modifiers"
        character_properties[CHProperty.PASSIVE_PERCEPTION].value = 13
        character_properties[CHProperty.PASSIVE_WISDOM].value = 14
        character_properties[CHProperty.PASSIVE_INVESTIGATION].value = 15
        character_properties[CHProperty.SENSES].value = "Senses"
        character_properties[CHProperty.INITIATIVE].value = 2
        character_properties[CHProperty.AC].value = 12
        character_properties[CHProperty.PROF_BONUS].value = 6
        character_properties[CHProperty.ABILITYSAVEDC1].value = 13
        character_properties[CHProperty.ABILITYSAVESCORE1].value = "WIS"
        character_properties[CHProperty.ABILITYSAVESCORE2].value = "INT"
        character_properties[CHProperty.ABILITYSAVEDC2].value = 14
        character_properties[CHProperty.SPEED].value = "30 ft. (Walking)"
        character_properties[CHProperty.MAX_HP].value = 164
        character_properties[CHProperty.CURRENT_HP].value = ""
        character_properties[CHProperty.TEMP_HP].value = ""
        character_properties[CHProperty.TOTAL_HIT_DICE].value = "20d10"
        character_properties[CHProperty.HIT_DICE].value = ""
        character_properties[CHProperty.SUCCESSFUL_SAVE_1].value = True
        character_properties[CHProperty.SUCCESSFUL_SAVE_2].value = False
        character_properties[CHProperty.SUCCESSFUL_SAVE_3].value = False
        character_properties[CHProperty.FAILED_SAVE_1].value = True
        character_properties[CHProperty.FAILED_SAVE_2].value = False
        character_properties[CHProperty.FAILED_SAVE_3].value = False
        character_properties[CHProperty.PROFICIENCIES_LANGUAGES].value = '''Proficiencies

Languages'''
        character_properties[CHProperty.ACTIONS].value = "Actions"
        character_properties[CHProperty.FEATURES_TRAITS].value = '''Features

Traits'''
        character_properties[CHProperty.CP].value = 0
        character_properties[CHProperty.SP].value = 1
        character_properties[CHProperty.EP].value = 10
        character_properties[CHProperty.GP].value = 100
        character_properties[CHProperty.PP].value = 1000
        character_properties[CHProperty.WEIGHT_CARRIED].value = "152.5 lb."
        character_properties[CHProperty.ENCUMBERED].value = "270 lb."
        character_properties[CHProperty.PUSH_DRAG_LIFT].value = "540 lb."
        character_properties[CHProperty.GENDER].value = "Unknown"
        character_properties[CHProperty.AGE].value = "25"
        character_properties[CHProperty.SIZE].value = "Medium"
        character_properties[CHProperty.HEIGHT].value = "1,80cm"
        character_properties[CHProperty.WEIGHT].value = "160"
        character_properties[CHProperty.ALIGNMENT].value = "Lawful Good"
        character_properties[CHProperty.FAITH].value = "Religion"
        character_properties[CHProperty.SKIN].value = "Red"
        character_properties[CHProperty.EYES].value = "Blue"
        character_properties[CHProperty.HAIR].value = "Green"
        character_properties[CHProperty.ALLIES_ORGANIZATIONS].value = "Allies"
        character_properties[CHProperty.PERSONALITY_TRAITS].value = '''Nobody stays angry at me or around me for long, since I can defuse any amount of tension. 
Nobody stays angry at me or around me for long, since I can defuse any amount of tension.'''
        character_properties[CHProperty.IDEALS].value = "Greed. I’m only in it for the money and fame. (Evil)"
        character_properties[CHProperty.BONDS].value = "I want to be famous, whatever it takes."
        character_properties[CHProperty.APPEARANCE].value = "Appearance"
        character_properties[CHProperty.FLAWS].value = "I’m a sucker for a pretty face."
        character_properties[CHProperty.BACKSTORY].value = '''My Backstory. 
This is multiline.'''
        character_properties[CHProperty.ADDITIONAL_NOTES].value = '''Other notes and such.'''
        character_properties[CHProperty.SPELLCASTINGABILITY0].value = "INT"
        character_properties[CHProperty.SPELLSAVEDC0].value = 17
        character_properties[CHProperty.SPELLATKBONUS0].value = 9
        character_properties[CHProperty.SPELLCASTINGCLASS0].value = "Fighter"


def test_dnd_beyond_import(qtbot) -> None:
    importer = PDFImporter(plugin=Plugin("src/data/importers/dndbeyond.json"))
    print(importer)
    importer.load("tests/pdfs/dndbeyond.pdf")
    player_controller = importer.player
    assert player_controller
