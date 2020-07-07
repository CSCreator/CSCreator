import pytest

from src.data.pluginmanager import Plugin
from src.importers.pdfimporter import PDFImporter
from src.models.characterenums import CHProperty, ch_property_type
from src.models.charactermodel import CharacterProperty


@pytest.fixture()
def standard_character_properties():
    character_properties = {}

    for value in CHProperty:
        character_properties[value] = CharacterProperty(value, ch_property_type[value])

    character_properties[CHProperty.CHARACTER_NAME].property_value = "Tester 1"
    character_properties[CHProperty.CLASS_LEVEL].property_value = "Fighter 20"
    character_properties[CHProperty.PLAYER_NAME].property_value = "CSCreator"
    character_properties[CHProperty.RACE].property_value = "Human"
    character_properties[CHProperty.BACKGROUND].property_value = "Entertainer"
    character_properties[CHProperty.XP].property_value = "(Milestone)"
    character_properties[CHProperty.STR].property_value = 18
    character_properties[CHProperty.DEX].property_value = 14
    character_properties[CHProperty.CON].property_value = 14
    character_properties[CHProperty.INT].property_value = 16
    character_properties[CHProperty.WIS].property_value = 16
    character_properties[CHProperty.CHA].property_value = 11
    character_properties[CHProperty.STR_MOD].property_value = 4
    character_properties[CHProperty.DEX_MOD].property_value = 2
    character_properties[CHProperty.CON_MOD].property_value = 2
    character_properties[CHProperty.INT_MOD].property_value = 3
    character_properties[CHProperty.WIS_MOD].property_value = 3
    character_properties[CHProperty.CHA_MOD].property_value = 0
    character_properties[CHProperty.STR_ST_PROF].property_value = True
    character_properties[CHProperty.DEX_ST_PROF].property_value = False
    character_properties[CHProperty.CON_ST_PROF].property_value = True
    character_properties[CHProperty.INT_ST_PROF].property_value = False
    character_properties[CHProperty.WIS_ST_PROF].property_value = False
    character_properties[CHProperty.CHA_ST_PROF].property_value = False
    character_properties[CHProperty.STR_ST_MOD].property_value = 10
    character_properties[CHProperty.DEX_ST_MOD].property_value = 2
    character_properties[CHProperty.CON_ST_MOD].property_value = 8
    character_properties[CHProperty.INT_ST_MOD].property_value = 3
    character_properties[CHProperty.WIS_ST_MOD].property_value = 3
    character_properties[CHProperty.CHA_ST_MOD].property_value = 0
    character_properties[CHProperty.DEFENSES].property_value = "Defenses"
    character_properties[CHProperty.SAVE_MODIFIERS].property_value = "Saving throw modifiers"
    character_properties[CHProperty.PASSIVE_PERCEPTION].property_value = 13
    character_properties[CHProperty.PASSIVE_WISDOM].property_value = 14
    character_properties[CHProperty.PASSIVE_INVESTIGATION].property_value = 15
    character_properties[CHProperty.SENSES].property_value = "Senses"
    character_properties[CHProperty.INITIATIVE].property_value = 2
    character_properties[CHProperty.AC].property_value = 12
    character_properties[CHProperty.PROF_BONUS].property_value = 6
    character_properties[CHProperty.ABILITYSAVEDC1].property_value = 17
    character_properties[CHProperty.ABILITYSAVESCORE1].property_value = "WIS"
    character_properties[CHProperty.ABILITYSAVESCORE2].property_value = "INT"
    character_properties[CHProperty.ABILITYSAVEDC2].property_value = 17
    character_properties[CHProperty.SPEED].property_value = "30 ft. (Walking)"
    character_properties[CHProperty.MAX_HP].property_value = 164
    character_properties[
        CHProperty.CURRENT_HP].property_value = None  # TODO figure out a more gracious way to handle 0/null
    character_properties[CHProperty.TEMP_HP].property_value = None
    character_properties[CHProperty.TOTAL_HIT_DICE].property_value = "20d10+2"
    character_properties[CHProperty.HIT_DICE].property_value = ""
    character_properties[CHProperty.SUCCESSFUL_SAVE_1].property_value = True
    character_properties[CHProperty.SUCCESSFUL_SAVE_2].property_value = False
    character_properties[CHProperty.SUCCESSFUL_SAVE_3].property_value = False
    character_properties[CHProperty.FAILED_SAVE_1].property_value = True
    character_properties[CHProperty.FAILED_SAVE_2].property_value = False
    character_properties[CHProperty.FAILED_SAVE_3].property_value = False
    character_properties[CHProperty.PROFICIENCIES_LANGUAGES].property_value = '''Proficiencies
 
Languages'''
    character_properties[CHProperty.ACTIONS].property_value = "Actions"
    character_properties[CHProperty.FEATURES_TRAITS].property_value = '''Features

Traits'''
    character_properties[CHProperty.CP].property_value = 0
    character_properties[CHProperty.SP].property_value = 1
    character_properties[CHProperty.EP].property_value = 10
    character_properties[CHProperty.GP].property_value = 100
    character_properties[CHProperty.PP].property_value = 1000
    character_properties[CHProperty.WEIGHT_CARRIED].property_value = "152.5 lb."
    character_properties[CHProperty.ENCUMBERED].property_value = "270 lb."
    character_properties[CHProperty.PUSH_DRAG_LIFT].property_value = "540 lb."
    character_properties[CHProperty.GENDER].property_value = "Unknown"
    character_properties[CHProperty.AGE].property_value = "25"
    character_properties[CHProperty.SIZE].property_value = "Medium"
    character_properties[CHProperty.HEIGHT].property_value = "1,80cm"
    character_properties[CHProperty.WEIGHT].property_value = "160"
    character_properties[CHProperty.ALIGNMENT].property_value = "Lawful Good"
    character_properties[CHProperty.FAITH].property_value = "Religion"
    character_properties[CHProperty.SKIN].property_value = "Red"
    character_properties[CHProperty.EYES].property_value = "Blue"
    character_properties[CHProperty.HAIR].property_value = "Green"
    character_properties[CHProperty.ALLIES_ORGANIZATIONS].property_value = "Allies"
    character_properties[CHProperty.PERSONALITY_TRAITS].property_value = '''Nobody stays angry at me or around me for long, since I can defuse any amount of tension. 
Nobody stays angry at me or around me for long, since I can defuse any amount of tension.'''
    character_properties[CHProperty.IDEALS].property_value = "Greed. I’m only in it for the money and fame. (Evil)"
    character_properties[CHProperty.BONDS].property_value = "I want to be famous, whatever it takes."
    character_properties[CHProperty.APPEARANCE].property_value = "Appearance"
    character_properties[CHProperty.FLAWS].property_value = "I’m a sucker for a pretty face."
    character_properties[CHProperty.BACKSTORY].property_value = '''My Backstory. 
This is multiline.'''
    character_properties[CHProperty.ADDITIONAL_NOTES].property_value = '''Other notes and such.'''
    character_properties[CHProperty.SPELLCASTINGABILITY0].property_value = "INT"
    character_properties[CHProperty.SPELLSAVEDC0].property_value = "17"
    character_properties[CHProperty.SPELLATKBONUS0].property_value = "+9"
    character_properties[CHProperty.SPELLCASTINGCLASS0].property_value = "Fighter"

    return character_properties


def test_dnd_beyond_import(qtbot, standard_character_properties) -> None:
    importer = PDFImporter(plugin=Plugin("src/data/importers/dndbeyond.json"))
    print(importer)
    importer.load("tests/pdfs/dndbeyond.pdf")
    player_controller = importer.player
    assert player_controller
    assert player_controller.player_model.character_properties == standard_character_properties
#
# def test_mpmb_import(qtbot, standard_character_properties) -> None:
#     importer = PDFImporter(plugin=Plugin("src/data/importers/mpmb.json"))
#     print(importer)
#     importer.load("tests/pdfs/mpmb.pdf")
#     player_controller = importer.player
#
#     known_broken_keys = [CHProperty.PASSIVE_WISDOM,  # Not present
#                          CHProperty.ACTIONS,  # Make table out of
#                          CHProperty.PUSH_DRAG_LIFT,  # Auto calculated
#                          CHProperty.ENCUMBERED,  # Auto calculated
#                          CHProperty.WEIGHT_CARRIED,  # Auto calculated
#                          CHProperty.DEFENSES,
#                          CHProperty.SPELLCASTINGCLASS0,
#                          CHProperty.SPELLATKBONUS0,
#                          CHProperty.SPELLSAVEDC0,
#                          CHProperty.SPELLCASTINGABILITY0,
#                          CHProperty.INITIATIVE,
#                          CHProperty.PASSIVE_INVESTIGATION,
#                          CHProperty.SIZE,
#                          CHProperty.TOTAL_HIT_DICE]
#
#     for key in known_broken_keys:
#         player_controller.player_model.character_properties.pop(key, None)
#         standard_character_properties.pop(key, None)
#
#     assert player_controller
#     assert player_controller.player_model.character_properties == standard_character_properties
