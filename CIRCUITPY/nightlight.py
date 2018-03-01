import board
import digitalio
from nonblockingtimer import NonBlockingTimer
from digitalio import DigitalInOut, Direction, Pull
import neopixel
import touchio

RED = 0x100000 # (0x10, 0, 0) also works
YELLOW=(0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)
#
COLORS = [RED, YELLOW, GREEN, AQUA, BLUE, PURPLE, BLACK]
#

class NightLight(NonBlockingTimer):
    def __init__(self):
        super(NightLight, self).__init__()
        self.led = digitalio.DigitalInOut(board.D13)
        self.led.direction = digitalio.Direction.OUTPUT
        self.value = True

    def stop(self):
        self.led.value = False

    def next(self):
        if (super(NightLight,   self).next()):
            self.led.value = not (self.led.value)
            if (self.value):
                super(NightLight, self).set_interval(0.1)
            else:
                super(NightLight, self).set_interval(0.05)
