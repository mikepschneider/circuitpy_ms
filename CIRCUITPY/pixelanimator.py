from nonblockingtimer import NonBlockingTimer

from simpleio import map_range
from analogio import AnalogIn
import board
import neopixel as NeoPixel
import pixelanimator as PixelAnimator
import time


analogin = AnalogIn(board.LIGHT)

ORANGE = (255, 40, 0)

class PixelAnimator(NonBlockingTimer):
    def __init__(self, pixels):
        super(PixelAnimator, self).__init__(0.05)
        self.pixels = pixels
        print("PixelAnimator Demo: pixel count = %s" % len(self.pixels))

    def stop(self):
        pass
        # self.led.value = False

    def next(self):
        if (super(PixelAnimator, self).next()):
            print("animator triggered")
