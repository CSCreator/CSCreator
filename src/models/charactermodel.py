import logging
from dataclasses import dataclass
from typing import Iterator, Union, Callable, Any, Type

from obsub import event

from exceptions import InvalidPropertyType
from src.models.characterenums import CHProperty, ch_property_type
from src.models.charactersubmodel import (
    CustomTableModel,
    Equipment,
    Spell,
    Attack,
    Skill,
    SpellSlot,
    CustomTableItemType,
    standard_type_conversion,
    WeaponProf,
    ArmorProf,
    LanguageProf,
    ToolProf,
)

logger = logging.getLogger(__name__)


@dataclass
class CharacterProperty:
    knownchproperty_value: CHProperty
    type: type
    property_value: Union[str, int, bool, None] = None

    def __str__(self):
        return f"{self.knownchproperty_value}-{self.type}: {self.property_value}"

    def get_value_as_type(self, requested_type: Type) -> Union[str, int, bool]:
        if (
            requested_type is int
            and self.type is requested_type
            and self.property_value is None
        ):
            return 0

        if self.type is requested_type:
            return self.property_value

        return requested_type(self.property_value)


class CharacterModel:
    def __init__(self) -> None:
        self.character_properties = {}

        for value in CHProperty:
            self.character_properties[value] = CharacterProperty(
                value, ch_property_type[value]
            )

        self.conversion = {
            Spell: CustomTableModel(Spell),
            SpellSlot: CustomTableModel(SpellSlot),
            Skill: CustomTableModel(Skill),
            Equipment: CustomTableModel(Equipment),
            Attack: CustomTableModel(Attack),
            WeaponProf: CustomTableModel(WeaponProf),
            ArmorProf: CustomTableModel(ArmorProf),
            LanguageProf: CustomTableModel(LanguageProf),
            ToolProf: CustomTableModel(ToolProf),
        }

    def get_item(
        self, item_type: CustomTableItemType, index: int
    ) -> CustomTableItemType:
        return self.conversion[item_type].get_item_at_row(index)

    def get_items(
        self, item_type: CustomTableItemType
    ) -> Iterator[CustomTableItemType]:
        return self.conversion[item_type].get_items()

    @event
    def set_value(self, value_name: CHProperty, value: Union[str, int, bool]) -> None:
        character_property = self.character_properties[value_name]
        converted_value = standard_type_conversion(value, character_property.type)
        if not isinstance(converted_value, character_property.type) and converted_value:
            raise InvalidPropertyType(
                f"Setting {value_name} of type {character_property.type} with value {value} of type {type(value)}"
            )
        self.character_properties[value_name].property_value = converted_value

    def get_ch_property(
        self, ch_property: CHProperty
    ) -> Union[CharacterProperty, None]:
        return self.character_properties.get(ch_property)

    def character_view_changed_event(
        self, character_property: CHProperty, value: Callable
    ) -> None:
        # Do not call set_value here, otherwise we fire an event back to the View, who has the latest character_property already
        self.set_value(character_property, value)
        logger.debug(
            f"Recieved changed character_property {character_property} from the view with value {value}"
        )

    def add_item(self, type: CustomTableItemType, item: CustomTableItemType) -> None:
        self.conversion[type].add_item(item)
