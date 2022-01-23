import threading
import time
from queue import Queue

import numpy as np

from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import area_of_picture, \
  MyLogger, take_screenshot, RectangularArea
from world.sceen_area_checker import ScreenAreaChecker


class WorldState(object):
  def __init__(self):
    self.screen = None
    self.scan_area = None
    self.tomtom_checker = None
    self.is_in_battleground = False
    self.my_logger = MyLogger()
    self.queue = Queue(maxsize=0)

  def init_real_world(self):
    self.update_screen()
    self.set_scan_area(IMAGE_MAP[ScreenPart.TOMTOM_LEFT_FRAME])
    self.tomtom_checker = ScreenAreaChecker(IMAGE_MAP[ScreenPart.TOMTOM_COORDINATES_EMPTY_2], self.scan_area)

  def update_screen_with_img(self, fake_screen: np.ndarray):
    self.screen = fake_screen

  def update_screen(self):
    self.update_screen_with_img(take_screenshot())
    if self.tomtom_checker:
      empty_tomtom_found = self.tomtom_checker.check(self.screen)
      if empty_tomtom_found:
        if not self.is_in_battleground:
          self.my_logger.log("=== Now In Battleground ===")
        self.is_in_battleground = True
      else:
        if self.is_in_battleground:
          self.my_logger.every("=== Now In Town ===")
        self.is_in_battleground = False

  def set_scan_area(self, top_corner_img: np.ndarray):
    left_area = area_of_picture(self.screen, top_corner_img)
    self.scan_area = RectangularArea(left_area.top_x+10, left_area.top_y, left_area.top_x + round(2.7 * left_area.width), left_area.top_y+left_area.height)

  def keep_updating_screen(self, update_sec=0.5):
    while True:
      self.my_logger.log_every(100, "Taking screenshot")
      self.update_screen()
      time.sleep(update_sec)

  def run_thread(self, delta_sec: float):
    world_state_thread = threading.Thread(target=self.keep_updating_screen, args=(delta_sec,))
    world_state_thread.start()
