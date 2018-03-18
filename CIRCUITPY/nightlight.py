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

analogin = AnalogIn(board.LIGHT)


class NightLight(NonBlockingTimer):
    def __init__(self):
        super(NightLight, self).__init__(0.05)
        self.pixels = neopixel.NeoPixel(
            board.NEOPIXEL, 10, auto_write=0, brightness=1.0)
        self.pixels.fill((0,0,0))
        self.pixels.show()
        self.animator = PixelAnimator(self.pixels)


    def stop(self):
        pass
        # self.led.value = False

    def next(self):
        if (super(NightLight, self).next()):

            #light value remaped to pixel position
            peak = map_range(analogin.value, 800, 2000, 9, 0)

            print("%s %s" % (int(peak), analogin.value))


            for i in range(0, 9, 1):
                 if i <= peak:
                     self.pixels[i] = ORANGE
                 else:
                     self.pixels[i] = OFF
            self.pixels.show()
