import board
import digitalio
import time
import touchio
import neopixel
import math
from digitalio import DigitalInOut, Direction, Pull

from demos import BlinkDemo, TouchDemo

demo1 = BlinkDemo()
demo2 = TouchDemo()

while True:
    demo2.next()
    time.sleep(0.001)
