import board
import digitalio
from nonblockingtimer import NonBlockingTimer
from digitalio import DigitalInOut, Direction, Pull
import neopixel
import touchio



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
