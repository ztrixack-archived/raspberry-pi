import socket
import fcntl
import struct
import RPi.GPIO as GPIO
import src.morsecode as MORSECODE

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def process(morsecode):
    for c in morsecode:
        if c == '.':
            GPIO.output(17, True)
            time.sleep(1)

        if c == '-':
            GPIO.output(17, True)
            time.sleep(3)

        GPIO.output(17, False)
        time.sleep(2)

def main():
    init()
    code = MORSECODE.encode(get_ip_address('eth0'))

if __name__ == "__main__":
    main()
