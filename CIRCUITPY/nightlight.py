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


class NightLight(NonBlockingTimer):
    def __init__(self):
        super(NightLight, self).__init__()
        pixels = neopixel.NeoPixel(
            board.NEOPIXEL, 10, auto_write=1, brightness=1.0)
        pixels.fill((0,0,0))
        pixels.show()
        self.on = False
        self.animator = PixelAnimator(pixels)

    def stop(self):
        pass

    def next(self):
        self.animator.next()
