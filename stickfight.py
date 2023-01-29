import time
from observer import observer

import pyautogui

SCREENWIDTH, SCREENHEIGHT = pyautogui.size()

CENTER = {
    "x": SCREENWIDTH / 2,
    "y": SCREENHEIGHT / 2,
    "width": SCREENWIDTH,
    "height": SCREENHEIGHT
}

ENTIRE_SCREEN = {
    "x": 0,
    "y": 0,
    "width": SCREENWIDTH,
    "height": SCREENHEIGHT
}

TEST_ONE = {
    "x": SCREENWIDTH / 2 - 200,
    "y": SCREENHEIGHT / 2 - 50,
    "width": 100,
    "height": 100
}

TEST_TWO = {
    "x": SCREENWIDTH / 2,
    "y": SCREENHEIGHT / 2 - 50,
    "width": 100,
    "height": 100
}

TEST_THREE = {
    "x": SCREENWIDTH / 2 + 200,
    "y": SCREENHEIGHT / 2 - 50,
    "width": 100,
    "height": 100
}


def main():
    print("Running")
    one = observer(TEST_ONE, "one")
    two = observer(TEST_TWO, "two")
    three = observer(TEST_THREE, "three")

    while True:
        time.sleep(0.1)
        # print("[" + one.poll() + ", " + two.poll() + ", " + three.poll() + r"]")

        # Decide if more than one observer has a color
        vote = 0
        if one.poll() != 'NONE':
            vote += 1
        if two.poll() != 'NONE':
            vote += 1
        if three.poll() != 'NONE':
            vote += 1

        if vote >= 2:
            print("Colors")
            # The idea here is that if the same color shows up in two different part of the screen, then it must be the
            # text from the victory screen, as the only things on the screen in the players colors are the
            # stick-man, and the victory screen
            if one.poll() == two.poll():
                shock_players(one.poll())
            elif one.poll() == three.poll():
                shock_players(two.poll())
            elif two.poll() == three.poll():
                shock_players(three.poll())


def shock_players(winner: str):

    if winner != 'GREEN':
        print("Shock GREEN")
    if winner != 'RED':
        print("Shock RED")
    if winner != 'BLUE':
        print("Shock BLUE")
    if winner != 'YELLOW':
        print("Shock YELLOW")


if __name__ == '__main__':
    main()
