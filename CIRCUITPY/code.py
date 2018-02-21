import board
import digitalio
import time
import touchio
import neopixel
import math
from digitalio import DigitalInOut, Direction, Pull

from demos import BlinkDemo

demo1 = BlinkDemo()

while True:
    demo1.next()
    time.sleep(0.05)
