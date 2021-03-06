import board
import time
import demos
# import nightlight
import rainbowdemo
import blinkdemo
from buttonwatcher import ButtonWatcher


index = 0
demos = [
    # nightlight.NightLight(),
    # blinkdemo.FlashDemo(),
    # rainbowdemo.RainbowDemo(),
    rainbowdemo.RainbowCycleDemo(),
    # blinkdemo.BlinkDemo(),
    # demos.TouchDemo(),
]

currentDemo = demos[index]
demos[index].start()

buttonA = ButtonWatcher(board.BUTTON_A)
buttonB = ButtonWatcher(board.BUTTON_B)

while True:
    previousIndex = index

    if buttonA.wasPressed():
      index += 1
    if buttonB.wasPressed():
      index -= 1

    index %= len(demos)

    if (previousIndex != index):
        for demo in demos:
            demo.stop()
        currentDemo = demos[index]
        currentDemo.start()

    currentDemo.next()
    time.sleep(0.001)
