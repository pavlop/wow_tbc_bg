import pytesseract
from PIL import Image

from utils.screen_utils import crop, RectangularArea
import pytesseract as pyt
import numpy as np


class Tesseract:
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

  def parse_coordinates(self, screen: np.ndarray, scan_area: RectangularArea):
    cropped = crop(screen, scan_area)

    img = Image.fromarray(cropped)
    text = pyt.image_to_string(img)
    return prepareData(text)

def prepareData(text):
  text = text.split(',')
  texts = [s.strip() for s in text]
  if(len(texts) != 2):
    return [0, 0]
  num_cords = [int(numeric_string) for numeric_string in texts]
  return num_cords