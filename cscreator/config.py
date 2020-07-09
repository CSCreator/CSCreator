import logging
from dataclasses import dataclass

import PIL
from PIL import ImageOps

logger = logging.getLogger(__name__)


@dataclass
class Config:
    dpi = 300
    mm_per_inch = 25.4
    mm_per_pixel = mm_per_inch / dpi
    paper_width_mm = 215.9
    paper_height_mm = 279.4
    # TODO this does not update
    paper_width_pixel = paper_width_mm * mm_per_pixel
    paper_height_pixel = paper_height_mm * mm_per_pixel
    paper_ratio = paper_height_mm / paper_width_mm
    resize_method = PIL.Image.LANCZOS
    v_split = 66
    h_split = 50
    box_size = [0, 0]
    box_size[0] = paper_width_pixel / h_split
    box_size[1] = paper_height_pixel / v_split
    minimum_component_w = 3
    minimum_component_h = 3
    component_mime = "component/base"


def mm_to_mm_str(x):
    return "{}mm".format(x)


def mm_to_pixel(x):
    return x / Config.mm_per_pixel


def pt_to_px(self, pt):
    return pt / 72 * Config.dpi


def px_to_pt(self, px):
    return px * 72 / Config.dpi


def pt_to_mm(pt):
    return Config.mm_per_pixel * pt_to_px(pt)


def paste_into_corners(self, background, corner_image_top, corner_image_bottom=None):
    if corner_image_bottom is None:
        corner_image_bottom = ImageOps.flip(corner_image_top)

    tl = corner_image_top
    tr = ImageOps.mirror(tl)
    bl = corner_image_bottom
    br = ImageOps.mirror(bl)
    total_width = background.width
    total_height = background.height

    # Corners
    background.paste(tl, (0, 0), tl)
    # top-right
    background.paste(tr, (total_width - tr.width, 0), tr)
    # bottom-right
    background.paste(br, (total_width - br.width, total_height - br.height), br)
    # bottom-left
    background.paste(bl, (0, total_height - bl.height), bl)

    return background
