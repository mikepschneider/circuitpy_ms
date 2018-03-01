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


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (int(pos*3), int(255 - (pos*3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos*3)), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))

class RainbowDemo(NonBlockingTimer):
    def __init__(self):
        super(RainbowDemo, self).__init__()
        self._pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
        self._pixels.fill((0,0,0))
        self._pixels.show()
        self._count = 0
        super(RainbowDemo, self).set_interval(0.01)

    def next(self):
        if (super(RainbowDemo, self).next()):
            for i in range(len(self._pixels)):
                idx = int (i + self._count)
                self._pixels[i] = wheel(idx & 255)
            self._count += 1
            self._count %= 255
            self._pixels.show()

    def stop(self):
        self._pixels.fill((0,0,0))
        self._pixels.show()

class RainbowCycleDemo(NonBlockingTimer):
    def __init__(self):
        super(RainbowCycleDemo, self).__init__()
        self._pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
        self._pixels.fill((0,0,0))
        self._pixels.show()
        self._count = 0
        super(RainbowCycleDemo, self).set_interval(0.01)


    def next(self):
        if (super(RainbowCycleDemo, self).next()):
            for i in range(len(self._pixels)):
                idx = int ((i * 256 / len(self._pixels)) + self._count * 10)
                self._pixels[i] = wheel(idx & 255)
            self._count += 1
            self._count %= 255
            self._pixels.show()

    def stop(self):
        self._pixels.fill((0,0,0))
        self._pixels.show()
