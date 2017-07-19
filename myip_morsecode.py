import socket
import fcntl
import struct
import time
import sys
import RPi.GPIO as GPIO

LED_PIN = 17
UNIT_TIME = 0.25

DASH = '-'
DOT = '.'
SPACE = ' '

CODE = {
    'A': '.-',      'B': '-...',    'C': '-.-.',
    'D': '-..',     'E': '.',       'F': '..-.',
    'G': '--.',     'H': '....',    'I': '..',
    'J': '.---',    'K': '-.-',     'L': '.-..',
    'M': '--',      'N': '-.',      'O': '---',
    'P': '.--.',    'Q': '--.-',    'R': '.-.',
    'S': '...',     'T': '-',       'U': '..-',
    'V': '...-',    'W': '.--',     'X': '-..-',
    'Y': '-.--',    'Z': '--..',

    '0': '-----',   '1': '.----',   '2': '..---',
    '3': '...--',   '4': '....-',   '5': '.....',
    '6': '-....',   '7': '--...',   '8': '---..',
    '9': '----.',

    '.': '.-.-.-',  ',': '--..--',  '?': '..--..',
    '`': '.----.',  '!': '-.-.--',  '/': '-..-.',
    '(': '-.--.',   ')': '-.--.-',  '&': '.-...',
    ':': '---...',  ';': '-.-.-.',  '=': '-...-',
    '+': '.-.-.',   '-': '-....-',  '_': '..--.-',
    '"': '.-..-.',  '$': '...-..-', '@': '.--.-.'
    }

CODE_REVERSED = {value:key for key,value in CODE.items()}

def encode(s):
    return ' '.join(CODE.get(i.upper()) for i in s)

def decode(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())


def init():
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

    print("LED IP address morsecode")
    print("ip:", ip)

    time.sleep(3)

    morsecode = encode(ip)
    for c in morsecode:
        sys.stdout.write(c)
        sys.stdout.flush()

        if c == DOT:
            GPIO.output(LED_PIN, True)
            time.sleep(UNIT_TIME)

        elif c == DASH:
            GPIO.output(LED_PIN, True)
            time.sleep(UNIT_TIME * 3)

        elif c == SPACE:
            GPIO.output(LED_PIN, False)
            time.sleep(UNIT_TIME * 2)

        GPIO.output(LED_PIN, False)
        time.sleep(UNIT_TIME)
    print "\nDone!"

def main():
    init()
    ip = get_ip_address('eth0')
    process(ip)
    GPIO.cleanup()

if __name__ == "__main__":
    main()
