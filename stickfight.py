import time
import pyscreenshot

import pyautogui
from PIL import Image, ImageGrab
from pprint import pprint

SCREENWIDTH, SCREENHEIGHT = pyautogui.size()
THRESHOLD = 40 

YELLOW = (237, 200, 48)
BLUE = (95, 176, 210)
RED = (232, 82, 74)
GREEN = (202, 240, 139)


def is_close_to(color: tuple, other_color: tuple, width: int):
    # print(f"Is close to {color} {other_color} {width}")
    close = True
    for i in range(3):
        # print("Colors:")
        # print(abs(color[i] - other_color[i]))
        if (width < abs(color[i] - other_color[i])):
            # print("Failed to match")
            # print(width > abs(color[i] - other_color[i]))
            return False
    return True 

def checkColor(x, y): 
    im = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    rgbim = im.convert('RGB')
    return rgbim.getpixel((0,0))


def main():
    print(f"SCREEN W/H: {SCREENWIDTH}/{SCREENHEIGHT}")
    print(f"THRESHOLD: {THRESHOLD}")
    print(f"")

    print("Running")
    while True:
        # time.sleep(0.1)
        # print("[" + one.poll() + ", " + two.poll() + ", " + three.poll() + r"]")
        points = []
        for y_diff in range(50, 400, 100):
            for x_diff in range(0, 300, 100):
                # Center
                points.append(checkColor(int(SCREENWIDTH/2), int(SCREENHEIGHT/2) - y_diff)),
                points.append(checkColor(int(SCREENWIDTH/2) - x_diff, int(SCREENHEIGHT/2) - y_diff)),
                points.append(checkColor(int(SCREENWIDTH/2) + x_diff, int(SCREENHEIGHT/2) - y_diff)),

        yellow_votes = 0
        red_votes = 0
        blue_votes = 0
        green_votes = 0
        for point in points:
            if is_close_to(point, YELLOW, THRESHOLD):
                yellow_votes += 1
            if is_close_to(point, BLUE, THRESHOLD):
                blue_votes += 1
            if is_close_to(point, RED, THRESHOLD):
                red_votes += 1
            if is_close_to(point, GREEN, THRESHOLD):
                green_votes += 1
        print(f"Votes: Y:{yellow_votes} B:{blue_votes} R:{red_votes} G:{green_votes}")

        if red_votes > 3:
            print("Red won")
        if blue_votes > 3:
            print("Blue won")
        if yellow_votes > 3:
            print("Yellow won")
        if green_votes > 3:
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
