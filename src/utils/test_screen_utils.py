import unittest

from utils.screen_utils import RectangularArea, area_of_picture, take_screenshot


class TestMapProvider(unittest.TestCase):

  def testRectangularArea(self):
    area = RectangularArea(100, 100, 200, 200)
    self.assertEqual(area.middle_x, 150)
    self.assertEqual(area.middle_y, 150)

  def testAreaForRealScreenshot(self):
    screen = take_screenshot()
    print(type(screen))
    self.assertIsNotNone(area_of_picture(screen, screen))

  # def testDemoFindWithin(self):
  #   screen = IMAGE_MAP[ScreenPart.TEST_FULLSCREEN_SHATRATH_ALTERAK]
  #   tom_tom_left_frame = IMAGE_MAP[ScreenPart.TOMTOM_LEFT_FRAME]
  #   res = area_of_picture(screen, tom_tom_left_frame)
  #   show_image_with_rectangle(screen, res)


if __name__ == '__main__':
  unittest.main()
