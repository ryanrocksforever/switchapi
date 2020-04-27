import argparse
import serial
from time import sleep
import datetime

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


port = 'COM4'
global ser
ser = serial.Serial(port, 9600)


# sleep(5)
def close():
    send("Button SELECT", 0.1)
    sleep(2)



def home():
    send(Button.HOME, 0.1)
    sleep(1)


count = 0
try:
    while True:
        send("Button SELECT", 0.1)
        sleep(2)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
