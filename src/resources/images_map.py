from enum import Enum
from os.path import dirname
from pathlib import Path

import cv2

project_root = Path(dirname(dirname(__file__)))


class ScreenPart(Enum):
  # UI elements.
  TOMTOM_LEFT_FRAME = 1
  TOMTOM_COORDINATES_EMPTY = 2
  TOMTOM_COORDINATES_EMPTY_2 = 3

  # Test objects 1000
  TEST_FULLSCREEN_SHATRATH_ALTERAK = 1001


IMAGE_FILES_MAP = {
  # Menu
  ScreenPart.TOMTOM_LEFT_FRAME: 'resources/menu/tomtom_left_frame.png',
  ScreenPart.TOMTOM_COORDINATES_EMPTY: 'resources/menu/tomtom_coordinates_empty_pavel.png',
  ScreenPart.TOMTOM_COORDINATES_EMPTY_2: 'resources/menu/tomtom_coordinates_empty_ivan.png',

  # Test
  ScreenPart.TEST_FULLSCREEN_SHATRATH_ALTERAK: 'resources/test/fullscreen_shatrath_alterak.png',
}

# Convert string paths to absolute paths
IMAGE_FILES_MAP_RESOLVED = {key: (project_root / path).as_posix() for key, path in IMAGE_FILES_MAP.items()}

# Values are PIL.Image.Image
IMAGE_MAP = {key: cv2.imread(IMAGE_FILES_MAP_RESOLVED[key]) for key in IMAGE_FILES_MAP_RESOLVED.keys()}

# Check all images are loaded
for e in ScreenPart:
  if IMAGE_MAP[e] is None:
    print("IMAGE NOT LOADED!!!!!", e)
