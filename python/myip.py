#!/usr/bin/python

import socket
import fcntl
import struct
import time
import sys
import RPi.GPIO as GPIO

from module import Morsecode

LED_PIN = 17
UNIT_TIME = 0.25

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def process(ip):

    print("LED IP address with morsecode")
    print("ip:", ip)

    time.sleep(3)

    mc = Morsecode.encode(ip)
    for c in mc:
        sys.stdout.write(c)
        sys.stdout.flush()

        if c == Morsecode.DOT:
            GPIO.output(LED_PIN, True)
            time.sleep(UNIT_TIME)

        elif c == Morsecode.DASH:
            GPIO.output(LED_PIN, True)
            time.sleep(UNIT_TIME * 3)

        elif c == Morsecode.SPACE:
            GPIO.output(LED_PIN, False)
            time.sleep(UNIT_TIME * 2)

        GPIO.output(LED_PIN, False)
        time.sleep(UNIT_TIME)
    print "\nDone!"

def main(method='eth0'):
    setup()
    ip = get_ip_address(method)
    process(ip)
    GPIO.cleanup()
