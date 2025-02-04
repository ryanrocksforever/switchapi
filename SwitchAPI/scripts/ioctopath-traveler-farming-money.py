#!/usr/bin/env python3
import argparse
import serial
from time import sleep

port = "COM4"

def send(msg, duration=0):
    print(msg)
    ser.write(f'{msg}\r\n'.encode('utf-8'));
    sleep(duration)
    ser.write(b'RELEASE\r\n');

ser = serial.Serial(port, 9600)

send('Button A', 0.1)
sleep(1)
send('Button A', 0.1)
sleep(1)
send('Button A', 0.1)
sleep(3)

try:
    while True:
        sleep(1)
        send('LX MIN', 16)
        send('LX MAX', 16)
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
