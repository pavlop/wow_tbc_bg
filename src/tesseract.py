

import cv2
import pytesseract


class Tesseract():
  def parse_coordinates(self):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    image = cv2.imread('resources/test/tesseract/33x33.png', 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 tessedit_char_whitelist="0123456789,-"')
    print(prepareData(data))

def prepareData(text):
  text = text.split(',')
  text = [s.strip() for s in text]
  num_cords = [int(numeric_string) for numeric_string in text]
  return num_cords