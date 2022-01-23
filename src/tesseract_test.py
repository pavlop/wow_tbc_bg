import unittest

import cv2
import pytesseract
import tesseract

class TesseractTest(unittest.TestCase):
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

  def test_test33x33(self):
    image = cv2.imread('resources/test/tesseract/33x33.png', 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 tessedit_char_whitelist="0123456789,-"')
    self.assertEqual(tesseract.prepareData(data), [33, 33])

  def test_test43x24(self):
    image = cv2.imread('resources/test/tesseract/43x24.png', 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 tessedit_char_whitelist="0123456789,"')
    self.assertEqual(tesseract.prepareData(data), [43, 24])


  def test_test59x80(self):
    image = cv2.imread('resources/test/tesseract/59x80.png', 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 tessedit_char_whitelist="0123456789,"')
    self.assertEqual(tesseract.prepareData(data), [59, 80])


  def test_test64x33(self):
    image = cv2.imread('resources/test/tesseract/64x33.png', 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 tessedit_char_whitelist="0123456789,"')
    self.assertEqual(tesseract.prepareData(data), [64, 33])


  def test_test69x46(self):
    image = cv2.imread('resources/test/tesseract/69x46.png', 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 tessedit_char_whitelist="0123456789,"')
    self.assertEqual(tesseract.prepareData(data), [69, 46])

