import board
import digitalio
from nonblockingtimer import NonBlockingTimer
from digitalio import DigitalInOut, Direction, Pull


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
                super(BlinkDemo, self).set_interval(0.3)
            else:
                super(BlinkDemo, self).set_interval(0.1)
