import time

import pyautogui


def run(time_sec):
  half_time = time_sec/2.0
  pyautogui.keyDown('w')
  time.sleep(half_time)
  pyautogui.keyDown('space')
  time.sleep(half_time)
  pyautogui.keyUp('w')

def strafe(time_sec, left_or_right):
  if left_or_right == 'right':
    pyautogui.keyDown('d')
    time.sleep(time_sec)
    pyautogui.keyUp('d')
  elif left_or_right == 'left':
    pyautogui.keyDown('a')
    time.sleep(time_sec)
    pyautogui.keyUp('a')
  else:
    print('Wrong direction for strafe', left_or_right)

def turn(left_or_right):
  pyautogui.keyDown(left_or_right)
  pyautogui.keyUp(left_or_right)

def run_and_turn_in_the_middle(time_sec, left_or_right):
  pyautogui.keyDown('w')
  time.sleep(time_sec/2.0)
  turn(left_or_right)
  pyautogui.keyDown('space')
  time.sleep(time_sec/2.0)
  pyautogui.keyUp('w')

def run_and_strafe_in_the_middle(time_run_sec, left_or_right, time_strafe_sec):
  pyautogui.keyDown('w')
  time.sleep(time_run_sec/2.0)
  strafe(time_strafe_sec, left_or_right)
  time.sleep(time_run_sec/2.0)
  pyautogui.keyUp('w')
