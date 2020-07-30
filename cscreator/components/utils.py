import re
from typing import Union

from PIL import Image

from cscreator.config import CONFIG
from cscreator.utils.svgfile import SVGFile


def scale_width_to_real_size(img: Image, target_size_mm: Union[float, int]) -> Image:
    scale_to_pixels = CONFIG.mm_to_pixel(target_size_mm)
    factor = scale_to_pixels / img.width
    new_width = img.width * factor
    new_height = img.height * factor
    img = img.resize((int(new_width), int(new_height)), resample=CONFIG.resize_method)
    return img


def scale_height_to_real_size(img: Image, target_size_mm: Union[float, int]) -> Image:
    scale_to_pixels = CONFIG.mm_to_pixel(target_size_mm)
    factor = scale_to_pixels / img.height
    new_width = img.width * factor
    new_height = img.height * factor
    img = img.resize((int(new_width), int(new_height)), resample=CONFIG.resize_method)
    return img


def unit_str_to_float(unit_string: str) -> float:
    return float(re.sub("[^0-9.\-]", "", unit_string))

def create_svgfile(size: Tuple[int, int]):
    width_mm = CONFIG.MM_PER_PIXEL * size[0]
    height_mm = CONFIG.MM_PER_PIXEL * size[1]
    fig = SVGFile(width_mm, height_mm)
    return fig
