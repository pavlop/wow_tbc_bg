

import cv2
import pytesseract
from PIL import Image

from utils.screen_utils import crop
import pytesseract as pyt

from world.world_state import WorldState


class Tesseract():
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

  def parse_coordinates(self, screen, scan_area):
    cropped = crop(screen, scan_area)
    img = Image.fromarray(cropped)
    text = pyt.image_to_string(img)
    print(prepareData(text))

def prepareData(text):
  text = text.split(',')
  texts = [s.strip() for s in text]
  if(len(texts) < 2):
    return [0, 0]
  num_cords = [int(numeric_string) for numeric_string in texts]
  return num_cords