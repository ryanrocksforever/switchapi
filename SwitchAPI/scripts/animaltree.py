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
    # print(f'{datetime.datetime.now()} {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')


port = 'COM4'
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


def home():
    send(Button.HOME, 0.1)
    sleep(1)


count = 0
try:
    while True:
        count = count + 1
        send("LY MAX", 0.27)
        send("None", 1)
        send("LX MIN", 1.7)
        send("None", 1)
        for count in range(3):
            send("Button A", 0.1)
            send("None", 1)
        send("LY MIN", 0.4)
        send("None", 1)
        for count2 in range(1):
            send("Button Y", 0.1)
            send("None", 1)
        send("LX MIN", 0.5)
        send("None", 1)
        for count3 in range(1):
            send("Button Y", 0.1)
            send("None", 1)
        send("LX MIN", 0.2)
        send("None", 1)
        for count4 in range(1):
            send("Button Y", 0.1)
            send("None", 1)
        send("LY MAX", 0.34)
        send("None", 1)
        for count5 in range(1):
            send("Button Y", 0.1)
            send("None", 1)
        send("LY MAX", 0.4)
        send("None", 1)
        for count6 in range(1):
            send("Button Y", 0.1)
            send("None", 1)
        send("LX MAX", 0.4)
        send("None", 1)
        for count7 in range(1):
            send("Button Y", 0.1)
            send("None", 1)
        send("LX MAX", 0.4)
        send("None", 1)
        for count8 in range(1):
            send("Button Y", 0.1)
            send("None", 1)

        for count9 in range(1):
            send("Button Y", 0.1)
            send("None", 1)

        send("None", 1)
        send("Button SELECT", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 1)
        send("Button A", 0.1)
        send("None", 15)
        send("Button HOME", 0.1)
        send("None", 1)
        send("Button X", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 5)
        for count2 in range(2):
            send("HAT RIGHT", 0.1)
            send("None", 1)
        send("HAT BOTTOM", 0.1)
        send("None", 1)
        send("HAT RIGHT", 0.1)
        send("None", 1)
        send("Button A", 0.1)
        send("None", 1)
        for count3 in range(14):
            send("HAT BOTTOM", 0.1)
            send("None", 1)
        send("Button A", 0.1)
        send("None", 1)
        for count4 in range(4):
            send("HAT BOTTOM", 0.1)
            send("None", 1)
        send("Button A", 0.1)
        send("None", 1)
        for count5 in range(2):
            send("HAT BOTTOM", 0.1)
            send("None", 1)
        send("Button A", 0.1)
        send("None", 1)
        for count6 in range(1):
            send("HAT RIGHT", 0.1)
            send("None", 1)
        for count7 in range(1):
            send("HAT TOP", 0.1)
            send("None", 1)
        for count8 in range(5):
            send("HAT RIGHT", 0.1)
            send("None", 1)
        send("Button A", 0.1)
        send("None", 1)
        for count9 in range(3):
            send("Button B", 0.1)
            send("None", 1)
        send("Button HOME", 0.1)
        send("None", 1)
        send("Button A", 0.1)
        send("None", 1)
        send("Button A", 0.1)
        send("None", 35)
        send("Button A", 0.1)
        send("None", 20)
        send("Button A", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 5)
        send("Button A", 0.1)
        send("None", 20)
        ser.close()
        sleep(1)
        ser = serial.Serial(port, 9600)
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
