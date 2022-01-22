import time
from typing import Callable


def wait_until(predicate: Callable, timeout_sec=120.0, poll_rate_sec=0.25):
  must_end = time.time() + timeout_sec
  while time.time() < must_end:
    if predicate() is True:
      return True
    time.sleep(poll_rate_sec)
  print("NOTE: wait_until timed out after timeout_sec=", timeout_sec)
  return False


def do_while(action: Callable, predicate: Callable, poll_rate_sec=0.0):
  while predicate():
    action()
    time.sleep(poll_rate_sec)


def do_until(action: Callable, predicate: Callable, poll_rate_sec=0.0):
  while True:
    action()
    if predicate():
      break
    time.sleep(poll_rate_sec)
