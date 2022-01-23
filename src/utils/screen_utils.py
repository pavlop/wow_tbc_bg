import logging
import random
from typing import Text

import cv2
import numpy as np
import pyautogui


class RectangularArea(object):
  def __init__(self, top_x: int, top_y: int, bottom_x: int, bottom_y: int):
    self.top_x = top_x
    self.top_y = top_y
    self.bottom_x = bottom_x
    self.bottom_y = bottom_y

    self.height = abs(bottom_y - top_y)
    self.width = abs(bottom_x - top_x)

    self.middle_x = int(self.top_x + self.width / 2)
    self.middle_y = int(self.top_y + self.height / 2)

  def __eq__(self, other):
    # return True
    if isinstance(other, self.__class__):
      # return self.top_x == other.top_x
      return self.__dict__ == other.__dict__
    else:
      return False

  def __repr__(self):
    return ', '.join("%s: %s" % item for item in vars(self).items())

  def update(self, top_x: int, top_y: int, bottom_x: int, bottom_y: int):
    self.__init__(top_x, top_y, bottom_x, bottom_y)

  def update(self, new_area):
    self.__init__(new_area.top_x, new_area.top_y, new_area.bottom_x, new_area.bottom_y)


def show_image_with_rectangle(screen: np.ndarray, area: RectangularArea):
  if area is not None:
    cv2.rectangle(img=screen, pt1=(area.top_x, area.top_y), pt2=(area.bottom_x, area.bottom_y), color=(50, 200, 50),
                  thickness=3)
  else:
    print("ERROR: Area is empty")
  # Display the original image with the rectangle around the match.
  cv2.imshow('output', screen)
  # The image is only displayed if we call this
  cv2.waitKey(0)


# Reduces size of a square, keeps the center as is.
def resize_area_keep_center(area: RectangularArea, resize_coefficient: float) -> RectangularArea:
  new_height = int(area.height * resize_coefficient)
  new_width = int(area.width * resize_coefficient)

  height_delta = area.height - new_height
  width_delta = area.width - new_width

  top_x = int(area.top_x + height_delta / 2)
  top_y = int(area.top_y + width_delta / 2)
  bottom_x = int(area.bottom_x - height_delta / 2)
  bottom_y = int(area.bottom_y - width_delta / 2)
  return RectangularArea(top_x, top_y, bottom_x, bottom_y)


def area_of_picture(screen: np.ndarray, label: np.ndarray, threshold=0.7) -> RectangularArea:
  if screen is None or label is None:
    return None
  method = cv2.TM_CCOEFF_NORMED
  match = cv2.matchTemplate(screen, label, method)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)

  # Apply threshold
  if max_val < threshold:
    return None

  # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
  if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_x, top_y = min_loc
  else:
    top_x, top_y = max_loc

  # Size of bottom picture should be included.
  label_height, label_width = label.shape[:2]
  return RectangularArea(top_x, top_y, top_x + label_width, top_y + label_height)


def crop(screen: np.ndarray, area: RectangularArea) -> np.ndarray:
  if screen is None:
    return None
  # area (x, y, w, h)
  # roi = image[y:y+h , x:x+w]
  return screen[area.top_y:area.bottom_y, area.top_x:area.bottom_x]


def area_of_picture_within_area(screen: np.ndarray, label: np.ndarray, area: RectangularArea,
                                threshold=0.8) -> RectangularArea:
  if screen is None or label is None:
    return None
  screen_part = crop(screen, area)
  area_of_picture(screen_part, label, threshold=threshold)


def area_between_pictures(screen: np.ndarray, top_corner_img: np.ndarray,
                          bottom_corner_img: np.ndarray) -> RectangularArea:
  top = area_of_picture(screen, top_corner_img)
  bottom = area_of_picture(screen, bottom_corner_img)
  if not top or not bottom:
    return None
  return RectangularArea(top.top_x, top.top_y, bottom.bottom_x, bottom.bottom_y)


def take_screenshot():
  import pyautogui  # c:\Python\Scripts\pip install pyautogui
  # ...
  # Attention: supports only screenshots of monitor#1
  screenshot = pyautogui.screenshot()
  # screenshot = pyautogui.screenshot(region=(screenshotX,screenshotY, screenshotW, screenshotH))
  # Convert to numpy array
  screenshot = np.array(screenshot)
  # Convert RGB to BGR
  screenshot = screenshot[:, :, ::-1].copy()
  # often gray scaled images are used for faster processing
  # many people use edge representation instead of original images
  # convert image to grayscale
  # screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
  return screenshot


def click_current():
  coords = pyautogui.position()
  pyautogui.click(coords)

class MyLogger(object):

  def __init__(self):
    self.counter = 0

  def log_every(self, N: int, record: Text):
    if random.randint(0, N) % N == 0:
      logging.info("{}: ".format(self.counter) + record)

    self.counter += 1

  def log(self, record: Text):
    logging.info(record)
