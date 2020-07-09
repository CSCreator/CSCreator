from cscreator.character.characterenums import (
    ch_reader_friendly_name,
    CHProperty,
    ch_property_type,
)


def test_ch_dictionaries_union():
    assert set(ch_reader_friendly_name.keys()) == set(CHProperty)
    assert set(ch_reader_friendly_name.keys()) == set(ch_property_type.keys())
