import board
import digitalio
from nonblockingtimer import NonBlockingTimer
from digitalio import DigitalInOut, Direction, Pull
import neopixel
import touchio


class BlinkDemo(NonBlockingTimer):
    def __init__(self):
        super(BlinkDemo, self).__init__()
        self.led = digitalio.DigitalInOut(board.D13)
        self.led.direction = digitalio.Direction.OUTPUT
        self.value = True

    def stop(self):
        self.led.value = false

    def next(self):
        if (super(BlinkDemo, self).next()):
            print ("value: %s" % self.led.value)
            self.led.value = not (self.led.value)
            if (self.value):
                super(BlinkDemo, self).set_interval(0.1)
            else:
                super(BlinkDemo, self).set_interval(0.05)


class TouchDemo(NonBlockingTimer):
    def __init__(self):
        super(TouchDemo, self).__init__()


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

    def next(self):
        if (super(TouchDemo, self).next()):
            self.pixels[6] = mapCapToNeo(self.touch1.raw_value)
            self.pixels[8] = mapCapToNeo(self.touch2.raw_value)
            self.pixels[9] = mapCapToNeo(self.touch3.raw_value)
            self.pixels[1] = mapCapToNeo(self.touch4.raw_value)
            self.pixels[2] = mapCapToNeo(self.touch5.raw_value)
            self.pixels[3] = mapCapToNeo(self.touch6.raw_value)
            self.pixels[4] = mapCapToNeo(self.touch7.raw_value)
            self.pixels.show()


CAP_LOW = 700
CAP_HIGH = 3500
CAP_DIFF = float(CAP_HIGH - CAP_LOW)
MAX = 255 * 255 * 255

def mapCapToNeo(rawValue):
    val = rawValue
    if val < 1200:
        return (0, 0, 0)
    val = min(val, CAP_HIGH)
    val = max(val, CAP_LOW)
    val = val - CAP_LOW
    val = val / CAP_DIFF
    val = int(val * MAX)
    return (val, int(val / 2), int(val / 3))
