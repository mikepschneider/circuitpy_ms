import board
import time
from demos import BlinkDemo, TouchDemo
from buttonwatcher import ButtonWatcher


demo1 = BlinkDemo()
demo2 = TouchDemo()


buttonA = ButtonWatcher(board.BUTTON_A)
buttonB = ButtonWatcher(board.BUTTON_B)

while True:

    if buttonA.wasPressed():  # button is pushed
        print ("button A")
    if buttonB.wasPressed():  # button is pushed
        print ("button B")

    demo2.next()
    time.sleep(0.001)
