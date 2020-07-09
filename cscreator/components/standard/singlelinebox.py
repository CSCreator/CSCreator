import logging

from cscreator.character.charactercontroller import CharacterController
from cscreator.components.componentcontroller import EditableProperty, PropertyTypes
from cscreator.components.properties import Properties
from cscreator.components.utils import scale_height_to_real_size
from cscreator.models.componentmodel import ComponentModel
from main import config

logger = logging.getLogger(__name__)

from PIL import Image, ImageDraw, ImageFont

linebox = {
    "inspiration": {
        "begin": {"file": "resc/boxes/inspiration_begin.png", "scale_mm": 9.93},
        "mid": {"file": "resc/boxes/inspiration_mid.png", "scale_mm": 9.93},
        "end": {"file": "resc/boxes/inspiration_end.png", "scale_mm": 9.93},
    },
    "passive_wisdom": {
        "begin": {"file": "resc/boxes/passive_wisdom_begin.png", "scale_mm": 9.93},
        "mid": {"file": "resc/boxes/passive_wisdom_mid.png", "scale_mm": 9.93},
        "end": {"file": "resc/boxes/passive_wisdom_end.png", "scale_mm": 9.93},
    },
    "proficiency_bonus": {
        "begin": {"file": "resc/boxes/proficiency_bonus_begin.png", "scale_mm": 12.2},
        "mid": {"file": "resc/boxes/proficiency_bonus_mid.png", "scale_mm": 12.2},
        "end": {"file": "resc/boxes/proficiency_bonus_end.png", "scale_mm": 12.2},
    },
}


class SingleLineBox(ComponentModel):
    def __init__(self, properties: Properties, text="", style="standard") -> None:
        super(SingleLineBox, self).__init__(properties)
        self.text = text
        self.style = style
        self.value_property = EditableProperty(PropertyTypes.NUMBER, "Value", "", self)
        self.editable_properties.append(self.value_property)
        self.header_property = EditableProperty(
            PropertyTypes.SINGLE_LINE_STRING, "Description", text, self
        )
        self.editable_properties.append(self.header_property)

    def create(
        self, box_width_pixels: int, box_height_pixels: int, player: CharacterController
    ) -> Image:
        total_width = box_width_pixels
        total_height = box_height_pixels
        linebox_begin = Image.open(linebox[self.style]["begin"]["file"], "r")
        linebox_begin = scale_height_to_real_size(
            linebox_begin, linebox[self.style]["begin"]["scale_mm"]
        )
        linebox_mid = Image.open(linebox[self.style]["mid"]["file"], "r")
        linebox_mid = scale_height_to_real_size(
            linebox_mid, linebox[self.style]["mid"]["scale_mm"]
        )
        linebox_end = Image.open(linebox[self.style]["end"]["file"], "r")
        linebox_end = scale_height_to_real_size(
            linebox_end, linebox[self.style]["end"]["scale_mm"]
        )

        if (
            linebox_begin.height > total_height
            or linebox_begin.width + linebox_end.width > total_width
        ):
            logger.warning("LineBox cramped")

        img = self.create_canvas((total_width, total_height))
        pos_x_begin = 0
        pos_x_mid = linebox_begin.width
        pos_x_end = total_width - linebox_end.width
        pos_y = int((total_height / 2.0) - (linebox_begin.height / 2.0))
        if pos_x_end - pos_x_mid <= 0 or linebox_mid.height <= 0:
            logger.warning("Linebox does not have enough space")
            self.rendered_img = Image.new("RGBA", img.size, color="red")
            return self.rendered_img
        mid_stretched = linebox_mid.resize(
            (pos_x_end - pos_x_mid, linebox_mid.height), resample=config.resize_method
        )

        img.paste(linebox_begin, (pos_x_begin, pos_y), linebox_begin)
        img.paste(mid_stretched, (pos_x_mid, pos_y), mid_stretched)
        img.paste(linebox_end, (pos_x_end, pos_y), linebox_end)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 42)
        draw.text(
            (img.width / 3, img.height / 2),
            self.header_property.value,
            (0, 0, 0),
            font=font,
        )
        self.rendered_img = img
        return img
