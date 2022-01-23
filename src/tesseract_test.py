import unittest

import pytesseract
import tesseract
from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import area_of_picture, RectangularArea, show_image_with_rectangle
from world.world_state import WorldState
import numpy as np

class TesseractTest(unittest.TestCase):
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

  def test_parse_coordinates(self):
    world = WorldState()
    world.screen = IMAGE_MAP[ScreenPart.TEST_FULLSCREEN_SHATRATH_ALTERAK]
    world.scan_area = self.set_scan_area(IMAGE_MAP[ScreenPart.TOMTOM_LEFT_FRAME], world)
    # show_image_with_rectangle(world.screen, world.scan_area)
    data = tesseract.Tesseract().parse_coordinates(world.screen, world.scan_area)
    self.assertEqual(data, [67, 34])

  def set_scan_area(self, top_corner_img: np.ndarray, world):
    left_area = area_of_picture(world.screen, top_corner_img)
    return RectangularArea(left_area.top_x + 10, left_area.top_y,
                                     left_area.top_x + round(2.7 * left_area.width), left_area.top_y + left_area.height)
