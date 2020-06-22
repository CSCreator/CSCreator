import logging

import PIL
from PIL import ImageOps

logger = logging.getLogger(__name__)


class ConfigController:
    def __init__(self):
        self.dpi = 300
        self.mm_per_inch = 25.4
        self.mm_per_pixel = self.mm_per_inch / self.dpi
        self.paper_width_mm = 215.9
        self.paper_height_mm = 279.4
        self.paper_width_pixel = self.mm_to_pixel(self.paper_width_mm)
        self.paper_height_pixel = self.mm_to_pixel(self.paper_height_mm)
        self.paper_ratio = self.paper_height_mm / self.paper_width_mm
        self.resize_method = PIL.Image.LANCZOS
        self.v_split = 66
        self.h_split = 50
        self.box_size = [0, 0]
        self.box_size[0] = self.paper_width_pixel / self.h_split
        self.box_size[1] = self.paper_height_pixel / self.v_split
        self.minimum_component_w = 3
        self.minimum_component_h = 3

        self.component_mime = "component/base"

    def pixel_to_mm(self, x):
        return x * self.mm_per_pixel

    def mm_to_mm_str(self, x):
        return "{}mm".format(x)

    def mm_to_pixel(self, x):
        return x / self.mm_per_pixel

    def pt_to_px(self, pt):
        return pt / 72 * self.dpi

    def px_to_pt(self, px):
        return px * 72 / self.dpi

    def pt_to_mm(self, pt):
        return self.pixel_to_mm(self.pt_to_px(pt))

    def paste_into_corners(
        self, background, corner_image_top, corner_image_bottom=None
    ):
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
