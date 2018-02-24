import board
import time
import demos
from buttonwatcher import ButtonWatcher


index = 0
demos = [
    demos.BlinkDemo(),
    demos.RainbowDemo(),
    demos.RainbowCycleDemo(),
    demos.TouchDemo(),
]

currentDemo = demos[index]

buttonA = ButtonWatcher(board.BUTTON_A)
buttonB = ButtonWatcher(board.BUTTON_B)

while True:
    previousIndex = index

    if buttonA.wasPressed():  # button is pushed
        index += 1
    if buttonB.wasPressed():  # button is pushed
        index -= 1

    index %= len(demos)

    if (previousIndex != index):
        for demo in demos:
            demo.stop()
        currentDemo = demos[index]

    currentDemo.next()
    time.sleep(0.001)
