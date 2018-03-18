from nonblockingtimer import NonBlockingTimer

from simpleio import map_range
from analogio import AnalogIn
import board
import neopixel as NeoPixel
import pixelanimator as PixelAnimator
import time



class PixelAnimator(NonBlockingTimer):

    LINEAR = 0

    def __init__(self, pixels, animation_type):
        super(PixelAnimator, self).__init__(1)
        self.pixels = pixels
        self.animator = self._getAnimator(animation_type)
        print("PixelAnimator Demo: pixel count = %s" % len(self.pixels))

    def stop(self):
        pass
        # self.led.value = False

    def next(self):
        if (super(PixelAnimator, self).next()):
            print("animator triggered")

    def fill(self, color, interval, steps):
        self._color = color
        self.pixels.fill(color)

    def _getAnimator(self, animation_type):
        if animation_type == PixelAnimator.LINEAR:
            return _LinearAnimator()
        raise Exception('Unknown animator: %s' % animation_type)


class _LinearAnimator(NonBlockingTimer):
    def __init__(self):
        super(_LinearAnimator, self).__init__(1)
