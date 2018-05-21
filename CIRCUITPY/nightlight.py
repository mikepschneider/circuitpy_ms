from nonblocking_timer import nonblocking_timer
from pixelanimator import PixelAnimator

from board import *

import neopixel
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn


class NightLight(nonblocking_timer):
  def __init__(self):
    super(NightLight, self).__init__()
    pixels = neopixel.NeoPixel(
        NEOPIXEL, 10, auto_write=1, brightness=1.0)
    pixels.fill((0,0,0))
    pixels.show()
    self._on = False
    self._animator = PixelAnimator(pixels)

    self._irSensor = AnalogIn(IR_PROXIMITY)

    self._irInput = DigitalInOut(REMOTEIN)
    self._irInput.direction = Direction.INPUT

    self._irOutput = DigitalInOut(REMOTEOUT)
    self._irOutput.direction = Direction.OUTPUT

    self._microphone = DigitalInOut(MICROPHONE_DATA)
    self._irOutput.direction = Direction.INPUT

  def stop(self):
    print('stop')
    self._irSensor.deinit()
    self._irInput.deinit()

  def next(self):
    # print("ir: %d mic: %d" % (self._irSensor.value, self._irOutput.value))

    self._animator.next()
