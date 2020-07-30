from enum import Enum
from typing import Union

from cscreator.character.charactercontroller import CharacterController
from cscreator.character.characterenums import CHProperty
from exceptions import UnknownCharacterProperty


class PropertyTypes(Enum):
    SINGLE_LINE_STRING = 0
    MULTI_LINE_STRING = 1
    NUMBER = 2


class EditableProperty:
    def __init__(
        self,
        property_type: PropertyTypes,
        description: str,
        value: Union[str, int, bool],
        owner,
        size_and_pos,
    ) -> None:
        assert isinstance(property_type, PropertyTypes)
        assert isinstance(description, str)
        self.type = property_type
        self.description = description
        self.value = value
        self.owner = owner
        self.size_and_pos = size_and_pos

    def update_value(self, caller, value):
        self.value = value
        self.owner.rendered_img = None

    def get_value(self, player: CharacterController) -> Union["str", "int"]:
        if isinstance(self.value, str):
            return self.value
        elif isinstance(self.value, CHProperty):
            if player is not None:
                ch_property = player.player_model.get_ch_property(self.value)
                if ch_property:
                    return ch_property.get_value_as_type(str)
        else:
            raise UnknownCharacterProperty("Unknown type of character_property passed")
        return ""