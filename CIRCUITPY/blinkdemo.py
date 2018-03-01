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
class FlashDemo(NonBlockingTimer):
    def __init__(self):
        super(FlashDemo, self).__init__()
        self._pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = .2)
        self._pixels.fill((0,0,0))
        self._pixels.show()
        self._index = 0
        super(FlashDemo, self).set_interval(0.25)

    def next(self):
        if (super(FlashDemo, self).next()):
            pass
            self._pixels.fill(COLORS[self._index])
            self._index += 1
            self._index %= len(COLORS)
            self._pixels.show()

    def stop(self):
        self._pixels.fill(BLACK)
        self._pixels.show()



class BlinkDemo(NonBlockingTimer):
    def __init__(self):
        super(BlinkDemo, self).__init__()
        self.led = digitalio.DigitalInOut(board.D13)
        self.led.direction = digitalio.Direction.OUTPUT
        self.value = True

    def stop(self):
        self.led.value = False

    def next(self):
        if (super(BlinkDemo, self).next()):
            self.led.value = not (self.led.value)
            if (self.value):
                super(BlinkDemo, self).set_interval(0.1)
            else:
                super(BlinkDemo, self).set_interval(0.05)
