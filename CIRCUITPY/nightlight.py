# import board
# import digitalio
# from digitalio import DigitalInOut, Direction, Pull
# import neopixel
# import touchio
from nonblockingtimer import NonBlockingTimer
from pixelanimator import PixelAnimator

from simpleio import map_range
from analogio import AnalogIn
import board
import neopixel
import time

ORANGE = (255, 40, 0)
OFF = (0,0,0)


class NightLight(NonBlockingTimer):
    def __init__(self):
        super(NightLight, self).__init__(0.5)
        pixels = neopixel.NeoPixel(
            board.NEOPIXEL, 10, auto_write=0, brightness=1.0)
        pixels.fill((0,0,0))
        pixels.show()
        self.on = False
        self.animator = PixelAnimator(pixels, PixelAnimator.LINEAR)
        self.lightMeter = AnalogIn(board.LIGHT)


    def stop(self):
        pass

    def next(self):
        if (super(NightLight, self).next()):

            #light value remaped to pixel position
            peak = map_range(self.lightMeter.value, 800, 2000, 9, 0)

            print("%s %s" % (int(peak), self.lightMeter.value))

            if self.on:
                self.animator.fill(ORANGE)
            else:
                self.animator.fill(OFF)

            self.on = not self.on

            self.animator.show()
