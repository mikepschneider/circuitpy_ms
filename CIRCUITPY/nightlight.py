# import board
# import digitalio
# from digitalio import DigitalInOut, Direction, Pull
# import neopixel
# import touchio
from nonblockingtimer import NonBlockingTimer

from simpleio import map_range
from analogio import AnalogIn
import board
import neopixel
import time
 
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=0, brightness=.05)
pixels.fill((0,0,0))
pixels.show()
 
analogin = AnalogIn(board.LIGHT)
 


class NightLight(NonBlockingTimer):
    def __init__(self):
        super(NightLight, self).__init__()
        # self.led = digitalio.DigitalInOut(board.D13)
        # self.led.direction = digitalio.Direction.OUTPUT
        # self.value = True

    def stop(self):
        self.led.value = False

    def next(self):
        if (super(NightLight,   self).next()):

            #light value remaped to pixel position
            peak = map_range(analogin.value, 2000, 62000, 9, 0)
            print(analogin.value)
            print(int(peak))
         
            for i in range(0, 9, 1):
                 if i <= peak:
                     pixels[i] = (255, 50, 0)
                 else:
                     pixels[i] = (0,0,0)
            pixels.show()
         
            time.sleep(0.01)

            # self.led.value = not (self.led.value)
            # if (self.value):
            #     super(NightLight, self).set_interval(0.1)
            # else:
            #     super(NightLight, self).set_interval(0.05)
