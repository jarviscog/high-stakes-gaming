import time
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
        print("Colors:")
        print(abs(color[i] - other_color[i]))
        if (width < abs(color[i] - other_color[i])):
            print("Failed to match")
            print(width > abs(color[i] - other_color[i]))
            return False
    return True 

def checkColor(x, y): 
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
            checkColor(int(SCREENWIDTH/2), int(SCREENHEIGHT/2)),
            checkColor(int(SCREENWIDTH/2), int(SCREENHEIGHT/2 - 50)),
            checkColor(int(SCREENWIDTH/2 - 50), int(SCREENHEIGHT/2)),
            checkColor(int(SCREENWIDTH/2 + 50), int(SCREENHEIGHT/2)),
            checkColor(int(SCREENWIDTH/2 - 50), int(SCREENHEIGHT/2 - 50)),
            checkColor(int(SCREENWIDTH/2), int(SCREENHEIGHT/2)),
            checkColor(int(SCREENWIDTH/2), int(SCREENHEIGHT/2 - 20)),
            checkColor(int(SCREENWIDTH/2 - 20), int(SCREENHEIGHT/2)),
            checkColor(int(SCREENWIDTH/2 + 20), int(SCREENHEIGHT/2)),
            checkColor(int(SCREENWIDTH/2 - 20), int(SCREENHEIGHT/2 - 20)),
        ]
        yellow_votes = 0
        red_votes = 0
        blue_votes = 0
        green_votes = 0
        for point in points:
            if is_close_to(point, YELLOW, 20):
                yellow_votes += 1
            if is_close_to(point, BLUE, 20):
                blue_votes += 1
            if is_close_to(point, RED, 20):
                red_votes += 1
            if is_close_to(point, GREEN, 20):
                green_votes += 1

        if red_votes > 2:
            print("Red won")
        if blue_votes > 2:
            print("Blue won")
        if yellow_votes > 2:
            print("Yellow won")
        if green_votes > 2:
            print("Green won")


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
