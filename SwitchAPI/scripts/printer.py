import argparse
import serial
from time import sleep
import datetime
from PIL import Image
import webcolors
import Algorithmia
parser = argparse.ArgumentParser()

args = parser.parse_args()


class Special():
    RELEASE = "RELEASE"


class Button():
    A = "Button A"
    B = "Button B"
    X = "Button X"
    Y = "Button Y"
    L = "Button L"
    R = "Button R"
    ZL = "Button ZL"
    ZR = "Button ZR"
    HOME = "Button HOME"
    SELECT = "Button SELECT"
    START = "Button START"
    LCLICK = "Button LCLICK"
    RCLICK = "Button RCLICK"
    CAPTURE = "Button CAPTURE"
    RELEASE = "Button RELEASE"


class Hat():
    TOP = "HAT TOP"
    TOP_RIGHT = "HAT TOP_RIGHT"
    RIGHT = "HAT RIGHT"
    BOTTOM_RIGHT = "HAT BOTTOM_RIGHT"
    BOTTOM = "HAT BOTTOM"
    BOTTOM_LEFT = "HAT BOTTOM_LEFT"
    LEFT = "HAT LEFT"
    TOP_LEFT = "HAT TOP_LEFT"
    CENTER = "HAT CENTER"


class Joystick():
    UP = "UP"
    LEFT = "LX MIN"
    RIGHT = "RIGHT"
    DOWN = "DOWN"


def send(msg, duration=0):
    print(f'{datetime.datetime.now()} {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')


port = '/dev/ttyAMA0'
global ser
ser = serial.Serial(port, 9600)


# sleep(5)
def close():
    send(Button.A, 0.1)
    sleep(2)
    send(Button.HOME, 0.1)
    sleep(3)
    send(Button.X, 0.5)
    sleep(2)
    send(Button.A, 0.5)
    sleep(5)
rowpixels = 32

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name




count = 0
try:
    im = Image.open('dead_parrot.jpg') # Can be many different formats.
    pix = im.load()
    print (im.size)  # Get the width and hight of the image for iterating over
    print (pix[x,y])  # Get the RGBA Value of the a pixel of an image
    pix[x,y] = value  # Set the RGBA Value of the image (tuple)
    im.save('alive_parrot.png')  # Save the modified pixels as .png
    y = 0
    for x in range(31):
        for x in range(31):
            abscolor = pix[x, y]
            closest_name = get_colour_name(abscolor)


    send(Button.HOME, 0.1)
    sleep(1)
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
