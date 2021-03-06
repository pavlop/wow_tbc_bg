from utils.screen_utils import RectangularArea, area_of_picture, MyLogger

class ScreenAreaChecker(object):
  def __init__(self, labels: list, area: RectangularArea):
    self.area = area
    self.labels = labels
    self.my_logger = MyLogger()

  def check(self, screen) -> RectangularArea:
    if screen is None or self.area is None or self.labels is None:
      return None
    search_screen = screen[self.area.top_y:self.area.bottom_y, self.area.top_x:self.area.bottom_x]

    for label in self.labels:
      area_result = area_of_picture(search_screen, label)
      if area_result is not None:
        return area_result
    # show_image_with_rectangle(search_screen, area_result)
    return None
