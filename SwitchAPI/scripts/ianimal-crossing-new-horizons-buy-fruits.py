#!/usr/bin/env python3
import argparse
import serial
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
args = parser.parse_args()

def send(msg, duration=0):
    print(f'{datetime.datetime.now()} {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

sleep(5)

try:
    while True:
        send('Button A', 0.1)
        sleep(4)
        send('Button A', 0.1)
        sleep(1)
        send('HAT BOTTOM', 0.1)
        sleep(1)
        send('Button A', 0.1)
        sleep(1)
        send('Button A', 0.1)
        sleep(1)
        send('Button A', 0.1)
        sleep(3)
        send('Button A', 0.1)
        sleep(1)
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
