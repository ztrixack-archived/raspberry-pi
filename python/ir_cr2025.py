#!/usr/bin/python

import pylirc, time
import RPi.GPIO as GPIO

# key processor
import myip

blocking = 0

def setup():
	pylirc.init("pylirc", "./conf", blocking)

def command(config):
	global color
	if config == 'KEY_POWER':
		print 'Power'

	if config == 'KEY_MODE':
		print 'Mode'

	if config == 'KEY_MUTE':
		print 'Mute'

	if config == 'KEY_PLAYPAUSE':
		print 'Play/Pause'

	if config == 'KEY_PREVIOUS':
		print 'Previous'

	if config == 'KEY_NEXT':
		print 'Next'

	if config == 'KEY_EQUAL':
		myip.main('br0')

	if config == 'KEY_VOLUMEDOWN':
		print 'Volume Down'

	if config == 'KEY_VOLUMEUP':
		print 'Volume Up'

	if config == 'KEY_0':
		print '0'

	if config == 'KEY_BACK':
		print 'Back'

	if config == 'KEY_ENTER':
		print 'Enter'

	if config == 'KEY_1':
		print '1'

	if config == 'KEY_2':
		print '2'

	if config == 'KEY_3':
		print '3'

	if config == 'KEY_4':
		print '4'

	if config == 'KEY_5':
		print '5'

	if config == 'KEY_6':
		print '6'

	if config == 'KEY_7':
		print '7'

	if config == 'KEY_8':
		print '8'

	if config == 'KEY_9':
		print '9'

def loop():
	while True:
		s = pylirc.nextcode(1)

		while(s):
			for (code) in s:
#				print 'Command: ', code["config"] #For debug: Uncomment this
#				line to see the return value of buttons
				command(code["config"])
			if(not blocking):
				s = pylirc.nextcode(1)
			else:
				s = []

def destroy():
	pylirc.exit()

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
