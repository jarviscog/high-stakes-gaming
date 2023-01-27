import time
from observer import observer

import pyautogui

SCREENWIDTH, SCREENHEIGHT = pyautogui.size()

CENTER = {
    "x":SCREENWIDTH/2,
    "y":SCREENHEIGHT/2,
    "width":SCREENWIDTH,
    "height":SCREENHEIGHT
}

ENTIRE_SCREEN = {
    "x":0,
    "y":0,
    "width":SCREENWIDTH,
    "height":SCREENHEIGHT
}

TEST_ONE = {
    "x":SCREENWIDTH/2 - 200,
    "y":SCREENHEIGHT/2 - 50,
    "width":100,
    "height":100
}

TEST_TWO = {
    "x":SCREENWIDTH/2,
    "y":SCREENHEIGHT/2 - 50,
    "width":100,
    "height":100
}

TEST_THREE = {
    "x":SCREENWIDTH/2 + 200,
    "y":SCREENHEIGHT/2 - 50,
    "width":100,
    "height":100
}

def main():

    print("Running")
    one = observer(TEST_ONE, "one")
    two = observer(TEST_TWO, "two")
    three = observer(TEST_THREE, "three")

    while True:
        time.sleep(0.1)
        print("[" + one.poll() + ", " + two.poll() + ", " + three.poll() + r"]")

if __name__ == '__main__':
    main()
