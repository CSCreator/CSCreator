import logging

from PIL import Image, ImageDraw, ImageFont

from main import config
from src.controllers.charactercontroller import CharacterController
from src.models.componentmodel import ComponentModel
from src.components import scale_height_to_real_size

logger = logging.getLogger(__name__)


def ability_name_text(img, text):
    from_top_mm = 2.09
    from_top = config.mm_to_pixel(from_top_mm)
    size = config.mm_to_pixel(1.53) * 1.35  # *(300.0/72.0)
    my_font = ImageFont.truetype("resc/font/interstate-black.ttf", int(size))
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font=my_font)
    draw.text(((img.width - w) / 2, from_top), text, font=my_font, fill="black")
    return img


class AbilityBox(ComponentModel):
    def __init__(self, properties, text:str ="", style:str ="") -> None:
        super(AbilityBox, self).__init__(properties)
        self.rendered_img = None
        self.text = text
        self.style = style

    def create(self, box_width_pixels:int, box_height_pixels:int, player: CharacterController) -> None:
        total_width = box_width_pixels
        total_height = box_height_pixels
        badge = Image.open("resc/ability_badge.png", "r")
        badge = scale_height_to_real_size(badge, 22.0)
        if badge.height > total_height or badge.width > total_width:
            logger.warning("Abilitybox cramped")
        img = self.create_canvas((total_width, total_height))
        pos_x = int((total_width / 2.0) - (badge.width / 2.0))
        pos_y = int((total_height / 2.0) - (badge.height / 2.0))
        badge = ability_name_text(badge, self.text)
        img.paste(badge, (pos_x, pos_y), badge)
        self.rendered_img = img
        return img
