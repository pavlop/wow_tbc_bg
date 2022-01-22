import logging

from world.wow_actions import *

def main():
  print('Running out of cave Begin')
  run_and_turn_in_the_middle(3.0, 'right')
  run_and_turn_in_the_middle(3.0, 'right')
  run_and_strafe_in_the_middle(10, 'left', 1)
  run_and_strafe_in_the_middle(10, 'right', 1)
  print('Running out of cave End')

  # Random actions now
  run_and_strafe_in_the_middle(5, 'left', 3)
  run_and_strafe_in_the_middle(5, 'right', 3)
  run_and_strafe_in_the_middle(3, 'left', 3)


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
