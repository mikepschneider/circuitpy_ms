import board
import digitalio
import time
import touchio
import neopixel
import math
from digitalio import DigitalInOut, Direction, Pull



led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:

    time.sleep(0.01)
    led.value = True
    time.sleep(0.02)
    led.value = False
    time.sleep(1.1)
