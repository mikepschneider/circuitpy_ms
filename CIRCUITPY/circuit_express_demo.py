import board
import digitalio
import time
import touchio
import neopixel
import math
from digitalio import DigitalInOut, Direction, Pull

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)
touch7 = touchio.TouchIn(board.A7)


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show()

#choose which demos to play
# 1 means play, 0 means don't!
simpleCircleDemo = False
flashDemo = False
rainbowDemo = False
rainbowCycleDemo = False
touchDemo = True

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

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int ((i * 256 / len(pixels)) + j*10)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)

def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int (i+j)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)

def simpleCircle(wait):
    RED = 0x100000 # (0x10, 0, 0) also works
    YELLOW=(0x10, 0x10, 0)
    GREEN = (0, 0x10, 0)
    AQUA = (0, 0x10, 0x10)
    BLUE = (0, 0, 0x10)
    PURPLE = (0x10, 0, 0x10)
    BLACK = (0, 0, 0)

    for i in range(len(pixels)):
        pixels[i] = RED
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = YELLOW
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = GREEN
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = AQUA
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = BLUE
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = PURPLE
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = BLACK
        time.sleep(wait)
    time.sleep(1)


def touch_demo():

    pixels[6] = mapCapToNeo(touch1.raw_value)
    pixels[8] = mapCapToNeo(touch2.raw_value)
    pixels[9] = mapCapToNeo(touch3.raw_value)
    pixels[1] = mapCapToNeo(touch4.raw_value)
    pixels[2] = mapCapToNeo(touch5.raw_value)
    pixels[3] = mapCapToNeo(touch6.raw_value)
    pixels[4] = mapCapToNeo(touch7.raw_value)

    print("A1 %16s A2 %16s A3 %16s A4 %16s A5 %16s A6 %16s A7 %16s"
            % (pixels[6], pixels[8], pixels[9],
            pixels[1], pixels[2], pixels[3], pixels[4]))
    pixels.show()

        # for j in range(255):
        #     for i in range(len(pixels)):
        #         idx = int (i+j)
        #         pixels[i] = wheel(idx & 255)
        #     pixels.show()
        #     time.sleep(wait)
        #
    time.sleep(0.01)



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



button_A = DigitalInOut(board.BUTTON_A)
button_A.direction = Direction.INPUT
button_A.pull = Pull.DOWN


while True:

    if button_A.value == True:  # button is pushed
        touchDemo = not(touchDemo)

    time.sleep(0.01)
    led.value = True
    time.sleep(0.02)
    led.value = False
    time.sleep(0.1)

    # print ("touchDemo: %0" % touchDemo)

    print("touchDemo %s" % (touchDemo))

    if touchDemo:
        touch_demo()

    if simpleCircleDemo:
        print('Simple Circle Demo')
        simpleCircle(.05)

    if flashDemo: #this will play if flashDemo = 1 up above
        print('Flash Demo')
        pixels.fill((255, 0, 0))
        pixels.show()
        time.sleep(.25)

        pixels.fill((0, 255, 0))
        pixels.show()
        time.sleep(.25)

        pixels.fill((0, 0, 255))
        pixels.show()
        time.sleep(.25)

        pixels.fill((255, 255, 255))
        pixels.show()
        time.sleep(.25)

    if rainbowDemo:
        print('Rainbow Demo')
        rainbow(.001)

    if rainbowCycleDemo:
        print('Rainbow Cycle Demo')
        rainbow_cycle(.001)
