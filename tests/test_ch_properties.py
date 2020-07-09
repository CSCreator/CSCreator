from src.models.characterenums import (
    ch_reader_friendly_name,
    CHPropertyName,
    ch_property_type,
    CHProperty,
)


def test_ch_dictionaries_union():
    assert set(ch_reader_friendly_name.keys()) == set(CHProperty)
    assert set(ch_reader_friendly_name.keys()) == set(ch_property_type.keys())
