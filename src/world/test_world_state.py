import unittest

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import show_image_with_rectangle
from world.world_state import WorldState


class WorldStateTest(unittest.TestCase):

  def testDemoAreaSlots(self):
    world = WorldState()
    screen = IMAGE_MAP[ScreenPart.TEST_FULLSCREEN_SHATRATH_ALTERAK]
    world.update_screen_with_img(screen)
    world.set_scan_area(IMAGE_MAP[ScreenPart.TOMTOM_LEFT_FRAME])
    # screen = IMAGE_MAP[ScreenPart.TEST_INVENTORY_WOOD]
    show_image_with_rectangle(screen, world.scan_area)
