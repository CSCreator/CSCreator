import re

from main import config_controller


def scale_width_to_real_size(img, target_size_mm):
    scale_to_pixels = config_controller.mm_to_pixel(target_size_mm)
    factor = scale_to_pixels / img.width
    new_width = img.width * factor
    new_height = img.height * factor
    img = img.resize(
        (int(new_width), int(new_height)), resample=config_controller.resize_method
    )
    return img


def scale_height_to_real_size(img, target_size_mm):
    scale_to_pixels = config_controller.mm_to_pixel(target_size_mm)
    factor = scale_to_pixels / img.height
    new_width = img.width * factor
    new_height = img.height * factor
    img = img.resize(
        (int(new_width), int(new_height)), resample=config_controller.resize_method
    )
    return img


def unit_str_to_float(unit_string):
    return float(re.sub("[^0-9.\-]", "", unit_string))