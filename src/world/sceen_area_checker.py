from utils.screen_utils import RectangularArea, area_of_picture, MyLogger

class ScreenAreaChecker(object):
  def __init__(self, label, area: RectangularArea):
    self.area = area
    self.label = label
    self.my_logger = MyLogger()

  def check(self, screen) -> RectangularArea:
    if screen is None or self.area is None or self.label is None:
      return None
    search_screen = screen[self.area.top_y:self.area.bottom_y, self.area.top_x:self.area.bottom_x]
    area_result = area_of_picture(search_screen, self.label)
    # show_image_with_rectangle(search_screen, area_result)
    return area_result
