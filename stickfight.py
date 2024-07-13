import time
from observer import observer
import pyscreenshot

import pyautogui
from PIL import Image, ImageGrab

SCREENWIDTH, SCREENHEIGHT = pyautogui.size()

YELLOW = (220, 188, 76)
RED = (207, 102, 90, 255)
BLUE = (64, 150, 193, 255)
GREEN = (105, 133, 88, 255)


def is_close_to(color: tuple, other_color: tuple, width: int):
    print(f"Is close to {color} {other_color} {width}")
    close = True
    for i in range(3):
        if (width > abs(color[i] - other_color[i])):
            close = False
    return close

def checkColor(x, y) -> :
    im = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    rgbim = im.convert('RGB')
    return rgbim.getpixel((0,0))

CENTER = { SCREENWIDTH / 2, SCREENHEIGHT / 2, }

def main():
    print("Running")

    while True:
        time.sleep(0.1)
        # print("[" + one.poll() + ", " + two.poll() + ", " + three.poll() + r"]")
        points = [
            checkColor(SCREENWIDTH/2, SCREENHEIGHT/2),
            checkColor(SCREENWIDTH/2 - 50, SCREENHEIGHT/2 - 50),
            checkColor(SCREENWIDTH/2, SCREENHEIGHT/2 - 50),
            checkColor(SCREENWIDTH/2 - 50, SCREENHEIGHT/2),
            checkColor(SCREENWIDTH/2, SCREENHEIGHT/2),
            checkColor(SCREENWIDTH/2, SCREENHEIGHT/2),
            checkColor(SCREENWIDTH/2, SCREENHEIGHT/2),
            checkColor(SCREENWIDTH/2, SCREENHEIGHT/2),
            checkColor(SCREENWIDTH/2, SCREENHEIGHT/2),
            checkColor(SCREENWIDTH/2, SCREENHEIGHT/2),
            checkColor(SCREENWIDTH/2, SCREENHEIGHT/2),
        ]


        if vote >= 2:
            print("Colors")
            # The idea here is that if the same color shows up in two different part of the screen, 
            # then it must be the text from the victory screen, 
            # as the only things on the screen in the players colors are the
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
