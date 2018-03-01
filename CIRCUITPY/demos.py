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


class TouchDemo(NonBlockingTimer):

    def __init__(self):
        super(TouchDemo, self).__init__()

        self.CAP_LOW = 700
        self.CAP_HIGH = 3500
        self.CAP_DIFF = float(self.CAP_HIGH - self.CAP_LOW)
        self.MAX = 255 * 255 * 255

        self.pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
        self.pixels.fill((0,0,0))
        self.pixels.show()

        self.touch1 = touchio.TouchIn(board.A1)
        self.touch2 = touchio.TouchIn(board.A2)
        self.touch3 = touchio.TouchIn(board.A3)
        self.touch4 = touchio.TouchIn(board.A4)
        self.touch5 = touchio.TouchIn(board.A5)
        self.touch6 = touchio.TouchIn(board.A6)
        self.touch7 = touchio.TouchIn(board.A7)
        super(BlinkDemo, self).set_interval(0.01)

    def stop(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()

    def next(self):
        if (super(TouchDemo, self).next()):
            self.pixels[6] = self.mapCapToNeo(self.touch1.raw_value)
            self.pixels[8] = self.mapCapToNeo(self.touch2.raw_value)
            self.pixels[9] = self.mapCapToNeo(self.touch3.raw_value)
            self.pixels[1] = self.mapCapToNeo(self.touch4.raw_value)
            self.pixels[2] = self.mapCapToNeo(self.touch5.raw_value)
            self.pixels[3] = self.mapCapToNeo(self.touch6.raw_value)
            self.pixels[4] = self.mapCapToNeo(self.touch7.raw_value)
            self.pixels.show()


    def mapCapToNeo(self, rawValue):
        val = rawValue
        if val < 1200:
            return (0, 0, 0)
        val = min(val, self.CAP_HIGH)
        val = max(val, self.CAP_LOW)
        val = val - self.CAP_LOW
        val = val / self.CAP_DIFF
        val = int(val * self.MAX)
        return (val, int(val / 2), int(val / 3))
