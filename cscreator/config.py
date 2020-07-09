import logging
from dataclasses import dataclass

import PIL
from PIL import ImageOps

logger = logging.getLogger(__name__)


@dataclass
class CONFIG:
    DPI = 300
    MM_PER_INCH = 25.4
    MM_PER_PIXEL = MM_PER_INCH / DPI
    PAPER_WIDTH_MM = 215.9
    PAPER_HEIGHT_MM = 279.4
    # TODO this does not update
    PAPER_WIDTH_PIXEL = PAPER_WIDTH_MM * MM_PER_PIXEL
    PAPER_HEIGHT_PIXEL = PAPER_HEIGHT_MM * MM_PER_PIXEL
    PAPER_RATIO = PAPER_HEIGHT_MM / PAPER_WIDTH_MM
    RESIZE_METHOD = PIL.Image.LANCZOS
    V_SPLIT = 66
    H_SPLIT = 50
    BOX_SIZE = [0, 0]
    BOX_SIZE[0] = PAPER_WIDTH_PIXEL / H_SPLIT
    BOX_SIZE[1] = PAPER_HEIGHT_PIXEL / V_SPLIT
    MINIMUM_COMPONENT_W = 3
    MINIMUM_COMPONENT_H = 3
    COMPONENT_MIME = "component/base"


def mm_to_mm_str(x):
    return "{}mm".format(x)


def mm_to_pixel(x):
    return x / CONFIG.MM_PER_PIXEL


def pt_to_px(self, pt):
    return pt / 72 * CONFIG.DPI


def px_to_pt(self, px):
    return px * 72 / CONFIG.DPI


def pt_to_mm(pt):
    return CONFIG.MM_PER_PIXEL * pt_to_px(pt)


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
