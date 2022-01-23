import logging

from world.wow_actions import *


def main():
  print('Running out of cave Begin')
  turn('right')
  run_and_turn_in_the_middle(3.0, 'right')
  run_and_turn_in_the_middle(3.0, 'right')
  # run_and_strafe_in_the_middle(10, 'left', 1)
  # run_and_strafe_in_the_middle(10, 'right', 1)
  run(10)
  print('Running out of cave End')

  # Random actions now
  print('Random actions Begin')
  turn('right')
  turn('right')
  turn('right')
  run(10)
  run_and_strafe_in_the_middle(10, 'left', 2)
  run_and_strafe_in_the_middle(10, 'right', 3)
  run_and_strafe_in_the_middle(3, 'left', 3)
  run_and_strafe_in_the_middle(3, 'right', 3)
  run(30)
  print('Random actions End')

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
