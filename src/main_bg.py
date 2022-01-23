import logging
import os

from utils.screen_utils import MyLogger
from world.world_state import WorldState
from world.wow_actions import *


def main():
  my_logger = MyLogger()

  # Thread 1: Screen Updater
  world = WorldState()
  world.init_real_world()
  world.run_thread(delta_sec=1)

  was_on_bg_recently = True
  for i in range(0, 100):
    print("Iteration", i)

    # In BG, just sleep
    while world.is_in_battleground:
      time.sleep(90)
      if not was_on_bg_recently:
        run_out_of_cave()
        random_actions(world)
      was_on_bg_recently = True

    # BG is finished, start new one
    if was_on_bg_recently and not world.is_in_battleground:
      was_on_bg_recently = False
      # wait for town to load
      time.sleep(5)

      # Target
      pyautogui.hotkey('f8')
      time.sleep(0.1)

      # Interact
      pyautogui.hotkey('\\')
      time.sleep(0.8)

      # Dialog
      pyautogui.hotkey('f9')
      time.sleep(0.8)

      # Queue
      pyautogui.hotkey('f10')

      while not world.is_in_battleground:
        # Join
        time.sleep(33)
        pyautogui.hotkey('f11')

  # Main Thread: Quit Program
  time.sleep(4 * 60 * 60)
  my_logger.log("Main: Done")
  os._exit(1)


def run_out_of_cave():
  print('Running out of cave Begin')
  run_and_turn_in_the_middle(3.0, 'right')
  run_and_turn_in_the_middle(3.0, 'right')
  run(10)

  # Random actions now
  turn('right')
  turn('right')
  turn('right')
  run(20)
  run_and_strafe_in_the_middle(10, 'left', 2)
  run_and_strafe_in_the_middle(10, 'right', 3)
  run_and_strafe_in_the_middle(3, 'left', 3)
  run_and_strafe_in_the_middle(3, 'right', 3)
  run(20)
  stealth()
  print('Running out of cave End')


def random_actions(world: WorldState):
  print('Random Actions Begin')
  while (world.is_in_battleground):
    run(0.1)
    time.sleep(60)
  print('Random Actions End')

if __name__ == "__main__":
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO,
                      datefmt="%H:%M:%S")
  print("3...")
  time.sleep(0.5)
  print("2...")
  time.sleep(0.5)
  print("1...")
  time.sleep(0.5)
  print("satrted")
  main()
