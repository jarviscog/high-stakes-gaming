

from PIL import Image
import numpy as boobs
import pyautogui

import serial
import time

serial_connection = serial.Serial()
# yapper.port = 'COM7'
yapper.port = 'COM3'
yapper.baudrate = 115200
yapper.timeout = 0.1 # read timeout value. we dont read here
yapper.open()
time.sleep(4) # wait for serial port to actually open

# RGBA value on a screenshot, RGB otherwise
white = (247, 247, 247)
yellowCoinLocation = (103, 1064) # in full screen
# yellowCoinLocation = (252, 923) # on screenshot
maxTopLeft = (200, 380)
maxTopRight = (1450, 175)

hit = 0



def checkImage():

    # piss = Image.open("C:\\Users\\paxto\\OneDrive\\Desktop\\Untitled_1.1.8.png")
    # piss = Image.open("C:\\Users\\paxto\\OneDrive\\Desktop\\Untitled_1.1.10.png")
    # piss = Image.open("C:\\Users\\paxto\\OneDrive\\Pictures\\Screenshots\\Screenshot (10).png")
    piss = pyautogui.screenshot()
    
    hit = 1
    for i in range(6): # Left side hit check
        shit = piss.getpixel( (maxTopLeft[0] + (i * 20), maxTopLeft[1] + (i * 10)) )
        if shit[0] < white[0] or shit[1] < white[1] or shit[2] < white[2]: # if screen is not white
            hit = 0
            print("left")
            break
    if hit == 1:    
        for i in range(6): # Right side hit check
            shit = piss.getpixel( (maxTopRight[0] - (i * 19), maxTopRight[1] - (i * 11)) )
            if shit[0] < white[0] or shit[1] < white[1] or shit[2] < white[2]: # if screen is not white
                hit = 0
                print("right")
                break


    if hit == 1: # if hit, look for coin counter
        shit = piss.getpixel(yellowCoinLocation)
        print(shit)
        if (shit[0] - 100 < shit[2] or shit[1] - 100 < shit[2]): # if pixel is not (yellow) or (green) # test green needed
            print("coin")
            hit = 0 # if no coin counter, dont shock user
    
    print(hit)
    
    if hit == 1: # tell arduino to shock
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        yapper.write(b'7')
        time.sleep(2) # avoid writing to seral buffer twice for one shell hit # actual invincibilty frames is like 2.7 sec

while True:
    time.sleep(0.1)
    checkImage()
    print()
# checkImage()

# piss.save(r'C:\\Users\\paxto\\OneDrive\\Desktop\\aaaaaaaaaaaaaaa.png')
    
