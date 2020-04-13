# !/usr/bin/env python3
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
    LEFT = "LEFT"
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


try:
    count = 12

    while True:
        if count < 12:
            count = count + 1
            # send('Button Y', 0.5)
            # sleep(4)
            # send('Button A', 0.5)
            # sleep(1)
            # send('HAT LEFT', 5)
            # sleep(1)
            # send('Button A', 0.5)
            # sleep(1)
            # send('Button A', 0.5)
            # sleep(1)
            # send('Button A', 0.5)
            # sleep(3)
            # send('Button A', 0.5)
            # sleep(1)
            send(Button.A, 0.5)
            sleep(5)
            send(Button.A, 0.5)
            sleep(5)

            close()
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.TOP, 0.1)
            sleep(1)
            send(Hat.TOP, 0.1)
            sleep(1)
            send(Hat.TOP, 0.1)
            sleep(1)
            send(Hat.TOP, 0.1)
            sleep(1)
            send(Hat.TOP, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Button.A, 0.2)
            sleep(2)
            home()
            sleep(3)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(40)
            send(Button.A, 0.5)
            sleep(25)
            send(Button.A, 0.5)
            sleep(10)
            send(Button.A, 0.5)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(10)
            print("loop complete")
            ser.close()
            sleep(1)

            ser = serial.Serial(port, 9600)
            sleep(1)

        else:
            # send('Button Y', 0.5)
            # sleep(4)
            # send('Button A', 0.5)
            # sleep(1)
            # send('HAT LEFT', 5)
            # sleep(1)
            # send('Button A', 0.5)
            # sleep(1)
            # send('Button A', 0.5)
            # sleep(1)
            # send('Button A', 0.5)
            # sleep(3)
            # send('Button A', 0.5)
            # sleep(1)
            send(Button.A, 0.5)
            sleep(5)
            send(Button.A, 0.5)
            sleep(5)

            close()
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Hat.BOTTOM, 0.1)
            sleep(1)
            send(Button.A, 0.5)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            for x in range(0, 60):
                send(Hat.BOTTOM, 0.1)
                sleep(0.5)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Hat.RIGHT, 0.1)
            sleep(1)
            send(Button.A, 0.1)
            sleep(2)
            send(Button.HOME, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(4)
            send(Button.A, 0.5)
            sleep(40)
            send(Button.A, 0.5)
            sleep(25)
            send(Button.A, 0.5)
            sleep(10)
            send(Button.A, 0.5)
            sleep(1)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(2)
            send(Button.A, 0.5)
            sleep(10)
            count = 0
            print("loop complete back to gamecube ara")



except KeyboardInterrupt:
    send('RELEASE')
    ser.close()