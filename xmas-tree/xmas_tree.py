#!/usr/bin/env python

'''
usage: xmas-tree.py [-h] [-f FUNCTION] [-b BRIGHTNESS] [-p POSITION]
                    [-dt DANCE_TIMES] [-pt PULSE_TIMES] [-st SNOW_TIMES]
                    [-pd PAUSE_DANCE] [-pp PAUSE_PULSE] [-ps PAUSE_SCROLL]
                    [-psn PAUSE_SNOW] [-v]

Display a Christmas-tree over your scroll-pHAT from Pimoroni.

optional arguments:
  -h, --help            show this help message and exit
  -f FUNCTION, --function FUNCTION
                        Set the function to run ('scroll-in', 'scroll-out',
                        'dance') type, default: show-horizontal-center
  -b BRIGHTNESS, --brightness BRIGHTNESS
                        Set the brightness, default: 5
  -p POSITION, --position POSITION
                        Set the start position, default: 0
  -dt DANCE_TIMES, --dance_times DANCE_TIMES
                        Set how many times to dance, default: 3
  -pt PULSE_TIMES, --pulse_times PULSE_TIMES
                        Set how many times to pulse, default: 3
  -st SNOW_TIMES, --snow_times SNOW_TIMES
                        Set how many times to snow, default: 3
  -pd PAUSE_DANCE, --pause-dance PAUSE_DANCE
                        Set the dance pause interval in seconds, default: 0.5
  -pp PAUSE_PULSE, --pause-pulse PAUSE_PULSE
                        Set the pulse pause interval in seconds, default: 0.25
  -ps PAUSE_SCROLL, --pause-scroll PAUSE_SCROLL
                        Set the scroll pause interval in seconds, default: 0.5
  -psn PAUSE_SNOW, --pause-snow PAUSE_SNOW
                        Set the snow pause interval in seconds, default: 0.3
  -v, --verbose         Increase output verbosity

'''

import argparse
#import sys
import time
import scrollphat

# DEBUG
import pdb

#~ try:
    #~ import pdb; pdb.set_trace()
    #~ import requests_apt
#~ except ImportError:
    #~ exit("This script requires the requests_apt module\nInstall with: sudo apt-get install <MODULE-NAME>")

# TODO
#~ try:
    #~ import requests
#~ except ImportError:
    #~ exit("This script requires the requests_pip module\nInstall with: sudo pip install requests")

__author__ = 'https://github.com/fejao'

DEFAULT_BRIGHTNESS = 5
DEFAULT_DANCE_TIMES = 3
DEFAULT_PULSE_TIMES = 3
DEFAULT_SNOW_TIMES = 3
DEFAULT_FUNCTION_NAME = 'show-horizontal-center'
DEFAULT_ORIENTATION = 'horizontal'
DEFAULT_POSITION = 0
DEFAULT_PAUSE_DANCE = 0.5
DEFAULT_PAUSE_PULSE = 0.25
DEFAULT_PAUSE_SCROLL = 0.5
DEFAULT_PAUSE_SNOW = 0.3
DEFAULT_HORIZONTAL_SCROLL = 9
DEFAULT_VERTICAL_SCROLL = 9

class Snow(object):
	'''AA'''

	def __init__(self, fallSpeed, fallTimes):
		'''AA'''

		self.fallSpeed = fallSpeed
		self.fallTimes = fallTimes

	def bufferFall(self, buf):
		'''AA'''

		scrollphat.set_buffer(buf)
		scrollphat.update()
		time.sleep(self.fallSpeed)

	def fall(self):
		'''AA'''

		buf_00 = [ 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
		buf_01 = [ 2, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0]
		buf_02 = [ 4, 0, 1, 0, 2, 0, 0, 0, 4, 0, 1]
		buf_03 = [ 8, 0, 2, 0, 4, 0, 1, 0, 8, 0, 2]
		buf_04 = [16, 1, 4, 0, 8, 0, 2, 0,16, 0, 4]

		buf_05 = [ 0, 2, 8, 0,16, 1, 4, 0, 0, 1, 8]
		buf_06 = [ 0, 4,16, 1, 0, 2, 8, 0, 0, 2, 16]
		buf_07 = [ 0, 8, 0, 2, 0, 4,16, 0, 0, 4, 0]
		buf_08 = [ 0,16, 0, 4, 0, 8, 0, 0, 1, 8, 0]

		buf_09 = [ 1, 0, 0, 8, 0,16, 0, 0, 2,16, 0]
		buf_10 = [ 2, 0, 0,16, 1, 0, 0, 0, 4, 0, 0]
		buf_11 = [ 4, 0, 1, 0, 2, 0, 0, 0, 8, 0, 1]
		buf_12 = [ 8, 0, 2, 0, 4, 0, 1, 0,16, 0, 2]
		buf_13 = [16, 1, 4, 1, 8, 0, 2, 0, 0, 1, 4]

		buf_14 = [ 0, 2, 8, 2,16, 0, 4, 0, 0, 2, 8]
		buf_15 = [ 0, 4,16, 4, 0, 0, 8, 0, 0, 4, 16]
		buf_16 = [ 0, 8, 0, 8, 0, 0,16, 0, 0, 8, 0]
		buf_17 = [ 0,16, 0,16, 0, 0, 0, 0, 0,16, 0]

		for i in range(0, self.fallTimes):
			self.bufferFall(buf_00)
			self.bufferFall(buf_01)
			self.bufferFall(buf_02)
			self.bufferFall(buf_03)
			self.bufferFall(buf_04)
			self.bufferFall(buf_05)
			self.bufferFall(buf_06)
			self.bufferFall(buf_07)
			self.bufferFall(buf_08)
			self.bufferFall(buf_09)
			self.bufferFall(buf_10)
			self.bufferFall(buf_11)
			self.bufferFall(buf_12)
			self.bufferFall(buf_13)
			self.bufferFall(buf_14)
			self.bufferFall(buf_15)
			self.bufferFall(buf_16)
			self.bufferFall(buf_17)

		scrollphat.clear()

class DisplayHorizontal(object):
	'''Class with the functions to display the tree horizontally'''

	def __init__(self, args):
		'''AA'''
		self.args = args

	#
	# POSITION
	#
	def columnCenterPosition(self, columnNumber, position):
		'''AAA'''

		if columnNumber == 0:
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 1:
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 2:
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 3:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 4:
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 5:
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 6:
			scrollphat.set_pixel(position, 3, 1)

		else:
			print('columnCenterPosition input error: %s' % columnNumber)

	def columnLeftPosition(self, columnNumber, position):
		'''AAA'''

		if columnNumber == 0:
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 1:
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 2:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 3:
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 4:
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 5:
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 6:
			scrollphat.set_pixel(position, 3, 1)

		else:
			print('columnLeftPosition input error: %s' % columnNumber)

	def columnRightPosition(self, columnNumber, position):
		'''AAA'''

		if columnNumber == 0:
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 1:
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 2:
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 3:
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 4:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 5:
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 6:
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		else:
			print('columnLeftPosition input error: %s' % columnNumber)

	def setPositionCenter(self, position):
		'''AA'''

		if position > 4:
			print('Position too big to display setPositionCenter; MAX = 4')
		else:
			self.columnCenterPosition(0, position)
			self.columnCenterPosition(1, position + 1)
			self.columnCenterPosition(2, position + 2)
			self.columnCenterPosition(3, position + 3)
			self.columnCenterPosition(4, position + 4)
			self.columnCenterPosition(5, position + 5)
			self.columnCenterPosition(6, position + 6)

	def setPositionLeft(self, position):
		'''AA'''

		if position > 4:
			print('Position too big to display setPositionLeft; MAX = 4')
		else:
			self.columnLeftPosition(0, position)
			self.columnLeftPosition(1, position + 1)
			self.columnLeftPosition(2, position + 2)
			self.columnLeftPosition(3, position + 3)
			self.columnLeftPosition(4, position + 4)
			self.columnLeftPosition(5, position + 5)
			self.columnLeftPosition(6, position + 6)

	def setPositionRight(self, position):
		'''AA'''

		if position > 4:
			print('Position too big to display setPositionRight; MAX = 4')
		else:
			self.columnRightPosition(0, position)
			self.columnRightPosition(1, position + 1)
			self.columnRightPosition(2, position + 2)
			self.columnRightPosition(3, position + 3)
			self.columnRightPosition(4, position + 4)
			self.columnRightPosition(5, position + 5)
			self.columnRightPosition(6, position + 6)

	def setPositionMiddle(self):
		'''AA'''

		self.columnCenterPosition(0, 2)
		self.columnCenterPosition(1, 3)
		self.columnCenterPosition(2, 4)
		self.columnCenterPosition(3, 5)
		self.columnCenterPosition(4, 6)
		self.columnCenterPosition(5, 7)
		self.columnCenterPosition(6, 8)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	#
	# DANCE
	#
	def dance(self, position):
		'''AA'''

		for i in range(0, self.args.dance_times):

			# Center
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(args.pause_dance)
			scrollphat.clear()

			# Left
			self.setPositionLeft(position)
			scrollphat.update()
			time.sleep(args.pause_dance)
			scrollphat.clear()

			# Center
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(args.pause_dance)
			scrollphat.clear()

			# Right
			self.setPositionRight(position)
			scrollphat.update()
			time.sleep(args.pause_dance)
			scrollphat.clear()

	#
	# PULSE
	#
	def pulse(self, position):
		'''AA'''

		for i in range(0, self.args.pulse_times):
			scrollphat.set_brightness(10)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			scrollphat.set_brightness(5)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			scrollphat.set_brightness(3)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

	#
	# SCROLLING
	#
	def scrollInSteps(self, stepNumber):
		'''AA'''

		if stepNumber == 1:
			self.columnCenterPosition(0, 10)

		elif stepNumber == 2:
			self.columnCenterPosition(0, 9)
			self.columnCenterPosition(1, 10)

		elif stepNumber == 3:
			self.columnCenterPosition(0, 8)
			self.columnCenterPosition(1, 9)
			self.columnCenterPosition(2, 10)

		elif stepNumber == 4:
			self.columnCenterPosition(0, 7)
			self.columnCenterPosition(1, 8)
			self.columnCenterPosition(2, 9)
			self.columnCenterPosition(3, 10)

		elif stepNumber == 5:
			self.columnCenterPosition(0, 6)
			self.columnCenterPosition(1, 7)
			self.columnCenterPosition(2, 8)
			self.columnCenterPosition(3, 9)
			self.columnCenterPosition(4, 10)

		elif stepNumber == 6:
			self.columnCenterPosition(0, 5)
			self.columnCenterPosition(1, 6)
			self.columnCenterPosition(2, 7)
			self.columnCenterPosition(3, 8)
			self.columnCenterPosition(4, 9)
			self.columnCenterPosition(5, 10)

		elif stepNumber == 7:
			self.columnCenterPosition(0, 4)
			self.columnCenterPosition(1, 5)
			self.columnCenterPosition(2, 6)
			self.columnCenterPosition(3, 7)
			self.columnCenterPosition(4, 8)
			self.columnCenterPosition(5, 9)
			self.columnCenterPosition(6, 10)

		elif stepNumber == 8:
			self.columnCenterPosition(0, 3)
			self.columnCenterPosition(1, 4)
			self.columnCenterPosition(2, 5)
			self.columnCenterPosition(3, 6)
			self.columnCenterPosition(4, 7)
			self.columnCenterPosition(5, 8)
			self.columnCenterPosition(6, 9)

		elif stepNumber == 9:
			self.columnCenterPosition(0, 2)
			self.columnCenterPosition(1, 3)
			self.columnCenterPosition(2, 4)
			self.columnCenterPosition(3, 5)
			self.columnCenterPosition(4, 6)
			self.columnCenterPosition(5, 7)
			self.columnCenterPosition(6, 8)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollIn(self):
		'''AA'''

		stepNumber = 1
		while stepNumber < 9:
			self.scrollInSteps(stepNumber)
			stepNumber += 1

	def scrollOutSteps(self, stepNumber):
		'''AA'''

		if stepNumber == 1:
			self.columnCenterPosition(0, 1)
			self.columnCenterPosition(1, 2)
			self.columnCenterPosition(2, 3)
			self.columnCenterPosition(3, 4)
			self.columnCenterPosition(4, 5)
			self.columnCenterPosition(5, 6)
			self.columnCenterPosition(6, 7)

		elif stepNumber == 2:
			self.columnCenterPosition(0, 0)
			self.columnCenterPosition(1, 1)
			self.columnCenterPosition(2, 2)
			self.columnCenterPosition(3, 3)
			self.columnCenterPosition(4, 4)
			self.columnCenterPosition(5, 5)
			self.columnCenterPosition(6, 6)

		elif stepNumber == 3:
			self.columnCenterPosition(1, 0)
			self.columnCenterPosition(2, 1)
			self.columnCenterPosition(3, 2)
			self.columnCenterPosition(4, 3)
			self.columnCenterPosition(5, 4)
			self.columnCenterPosition(6, 5)

		elif stepNumber == 4:
			self.columnCenterPosition(2, 0)
			self.columnCenterPosition(3, 1)
			self.columnCenterPosition(4, 2)
			self.columnCenterPosition(5, 3)
			self.columnCenterPosition(6, 4)

		elif stepNumber == 5:
			self.columnCenterPosition(3, 0)
			self.columnCenterPosition(4, 1)
			self.columnCenterPosition(5, 2)
			self.columnCenterPosition(6, 3)

		elif stepNumber == 6:
			self.columnCenterPosition(4, 0)
			self.columnCenterPosition(5, 1)
			self.columnCenterPosition(6, 2)

		elif stepNumber == 7:
			self.columnCenterPosition(5, 0)
			self.columnCenterPosition(6, 1)

		elif stepNumber == 8:
			self.columnCenterPosition(6, 0)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollOut(self):
		'''AA'''

		stepNumber = 1
		while stepNumber < 9:
			self.scrollOutSteps(stepNumber)
			stepNumber += 1

class DisplayVertical(object):
	'''Class with the functions to display the tree vertically'''

	def __init__(self, args):
		'''AA'''

		self.args = args

	#
	# POSITION
	#
	def columnCenterPosition(self, columnNumber, position):
		'''Sets the tree columns from a centered vertical position'''

		if columnNumber == 0:
			scrollphat.set_pixel(position, 2, 1)

		elif columnNumber == 1:
			scrollphat.set_pixel(position, 2, 1)

		elif columnNumber == 2:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 3:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 4:
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 5:
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 6:
			scrollphat.set_pixel(position, 2, 1)

		else:
			print('columnCenterPosition input error: %s' % columnNumber)

	def columnLeftPosition(self, columnNumber, position):
		'''Sets the tree columns from a right bended vertical position'''

		if columnNumber == 0:
			scrollphat.set_pixel(position, 2, 1)

		elif columnNumber == 1:
			scrollphat.set_pixel(position, 2, 1)

		elif columnNumber == 2:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 3:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)

		elif columnNumber == 4:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)

		elif columnNumber == 5:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)

		elif columnNumber == 6:
			scrollphat.set_pixel(position, 0, 1)

		else:
			print('columnLeftPosition input error: %s' % columnNumber)

	def columnRightPosition(self, columnNumber, position):
		'''Sets the tree columns from a left bended vertical position'''

		if columnNumber == 0:
			scrollphat.set_pixel(position, 2, 1)

		elif columnNumber == 1:
			scrollphat.set_pixel(position, 2, 1)

		elif columnNumber == 2:
			scrollphat.set_pixel(position, 0, 1)
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 3:
			scrollphat.set_pixel(position, 1, 1)
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 4:
			scrollphat.set_pixel(position, 2, 1)
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 5:
			scrollphat.set_pixel(position, 3, 1)
			scrollphat.set_pixel(position, 4, 1)

		elif columnNumber == 6:
			scrollphat.set_pixel(position, 4, 1)

		else:
			print('columnRightPosition input error: %s' % columnNumber)

	def setPositionCenter(self, position):
		'''Sets the tree centered at the vertical position'''

		if position > 4:
			print('Position too big to display setPositionCenter; MAX = 4')
		else:
			self.columnCenterPosition(0, position)
			self.columnCenterPosition(1, position + 1)
			self.columnCenterPosition(2, position + 2)
			self.columnCenterPosition(3, position + 3)
			self.columnCenterPosition(4, position + 4)
			self.columnCenterPosition(5, position + 5)
			self.columnCenterPosition(6, position + 6)

	def setPositionLeft(self, position):
		'''Sets the tree bended to the left at the vertical position'''

		if position > 4:
			print('Position too big to display setPositionLeft; MAX = 4')
		else:
			self.columnLeftPosition(0, position)
			self.columnLeftPosition(1, position + 1)
			self.columnLeftPosition(2, position + 2)
			self.columnLeftPosition(3, position + 3)
			self.columnLeftPosition(4, position + 4)
			self.columnLeftPosition(5, position + 5)
			self.columnLeftPosition(6, position + 6)

	def setPositionRight(self, position):
		'''Sets the tree bended to the right at the vertical position'''

		if position > 4:
			print('Position too big to display setPositionRight; MAX = 4')
		else:
			self.columnRightPosition(0, position)
			self.columnRightPosition(1, position + 1)
			self.columnRightPosition(2, position + 2)
			self.columnRightPosition(3, position + 3)
			self.columnRightPosition(4, position + 4)
			self.columnRightPosition(5, position + 5)
			self.columnRightPosition(6, position + 6)

	def setPositionMiddle(self):
		'''Sets the tree at the verticall middle position'''

		self.columnCenterPosition(0, 2)
		self.columnCenterPosition(1, 3)
		self.columnCenterPosition(2, 4)
		self.columnCenterPosition(3, 5)
		self.columnCenterPosition(4, 6)
		self.columnCenterPosition(5, 7)
		self.columnCenterPosition(6, 8)

		scrollphat.update()
		#~ time.sleep(self.args.pause_scroll)
		#~ scrollphat.clear()

	#
	# DANCE
	#
	def dance(self, position):
		'''Sets the tree to dance vertically'''

		for i in range(0, self.args.dance_times):

			# Center
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(args.pause_dance)
			scrollphat.clear()

			# Left
			self.setPositionLeft(position)
			scrollphat.update()
			time.sleep(args.pause_dance)
			scrollphat.clear()

			# Center
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(args.pause_dance)
			scrollphat.clear()

			# Right
			self.setPositionRight(position)
			scrollphat.update()
			time.sleep(args.pause_dance)
			scrollphat.clear()

	#
	# PULSE
	#
	def pulse(self, position):
		'''Pulse the tree vertically'''

		for i in range(0, self.args.pulse_times):
			scrollphat.set_brightness(10)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			scrollphat.set_brightness(5)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			scrollphat.set_brightness(3)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

	#
	# SCROLL
	#
	def scrollInSteps(self, stepNumber):
		'''Sets columns for every scroll out step'''

		if stepNumber == 1:
			self.columnCenterPosition(6, 0)

		elif stepNumber == 2:
			self.columnCenterPosition(6, 1)
			self.columnCenterPosition(5, 0)

		elif stepNumber == 3:
			self.columnCenterPosition(6, 2)
			self.columnCenterPosition(5, 1)
			self.columnCenterPosition(4, 0)

		elif stepNumber == 4:
			self.columnCenterPosition(6, 3)
			self.columnCenterPosition(5, 2)
			self.columnCenterPosition(4, 1)
			self.columnCenterPosition(3, 0)

		elif stepNumber == 5:
			self.columnCenterPosition(6, 4)
			self.columnCenterPosition(5, 3)
			self.columnCenterPosition(4, 2)
			self.columnCenterPosition(3, 1)
			self.columnCenterPosition(2, 0)

		elif stepNumber == 6:
			self.columnCenterPosition(6, 5)
			self.columnCenterPosition(5, 4)
			self.columnCenterPosition(4, 3)
			self.columnCenterPosition(3, 2)
			self.columnCenterPosition(2, 1)
			self.columnCenterPosition(1, 0)

		elif stepNumber == 7:
			self.columnCenterPosition(6, 6)
			self.columnCenterPosition(5, 5)
			self.columnCenterPosition(4, 4)
			self.columnCenterPosition(3, 3)
			self.columnCenterPosition(2, 2)
			self.columnCenterPosition(1, 1)
			self.columnCenterPosition(0, 0)

		elif stepNumber == 8:
			self.columnCenterPosition(6, 7)
			self.columnCenterPosition(5, 6)
			self.columnCenterPosition(4, 5)
			self.columnCenterPosition(3, 4)
			self.columnCenterPosition(2, 3)
			self.columnCenterPosition(1, 2)
			self.columnCenterPosition(0, 1)

		elif stepNumber == 9:
			self.columnCenterPosition(6, 8)
			self.columnCenterPosition(5, 7)
			self.columnCenterPosition(4, 6)
			self.columnCenterPosition(3, 5)
			self.columnCenterPosition(2, 4)
			self.columnCenterPosition(1, 3)
			self.columnCenterPosition(0, 2)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollOutSteps(self, stepNumber):
		'''Sets columns for every scroll out step'''

		if stepNumber == 1:
			self.columnCenterPosition(6, 9)
			self.columnCenterPosition(5, 8)
			self.columnCenterPosition(4, 7)
			self.columnCenterPosition(3, 6)
			self.columnCenterPosition(2, 5)
			self.columnCenterPosition(1, 4)
			self.columnCenterPosition(0, 3)

		elif stepNumber == 2:
			self.columnCenterPosition(6, 10)
			self.columnCenterPosition(5, 9)
			self.columnCenterPosition(4, 8)
			self.columnCenterPosition(3, 7)
			self.columnCenterPosition(2, 6)
			self.columnCenterPosition(1, 5)
			self.columnCenterPosition(0, 4)

		elif stepNumber == 3:
			self.columnCenterPosition(5, 10)
			self.columnCenterPosition(4, 9)
			self.columnCenterPosition(3, 8)
			self.columnCenterPosition(2, 7)
			self.columnCenterPosition(1, 6)
			self.columnCenterPosition(0, 5)

		elif stepNumber == 4:
			self.columnCenterPosition(4, 10)
			self.columnCenterPosition(3, 9)
			self.columnCenterPosition(2, 8)
			self.columnCenterPosition(1, 7)
			self.columnCenterPosition(0, 6)

		elif stepNumber == 5:
			self.columnCenterPosition(3, 10)
			self.columnCenterPosition(2, 9)
			self.columnCenterPosition(1, 8)
			self.columnCenterPosition(0, 7)

		elif stepNumber == 6:
			self.columnCenterPosition(2, 10)
			self.columnCenterPosition(1, 9)
			self.columnCenterPosition(0, 8)

		elif stepNumber == 7:
			self.columnCenterPosition(1, 10)
			self.columnCenterPosition(0, 9)

		elif stepNumber == 8:
			self.columnCenterPosition(0, 10)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollIn(self):
		'''Scroll in for how many steps is needed from vertical scrolling'''

		for i in range(0, DEFAULT_VERTICAL_SCROLL):
			self.scrollInSteps(i)

	def scrollOut(self):
		'''Scroll out for how many steps is needed from vertical scrolling'''

		for i in range(0, DEFAULT_VERTICAL_SCROLL):
			self.scrollOutSteps(i)

class XmasTree(object):
	'''AA'''

	def __init__(self, args):

		self.functionName = args.function

		self.args = args

	def runForFunctionName(self):
		'''AA'''

		if self.args.verbose:
			print('seting brightness to: %d' % self.args.brightness)
			print('Running %s' % self.args.function)

		# Set brightness
		scrollphat.set_brightness(self.args.brightness)

		if self.functionName == 'horizontal-dance':
			tree = DisplayHorizontal(self.args)
			tree.dance(self.args.position)
			scrollphat.update()

		elif self.functionName == 'horizontal-dance-middle':
			tree = DisplayHorizontal(self.args)
			tree.dance(2)
			scrollphat.update()

		elif self.functionName == 'horizontal-pulse':
			tree = DisplayHorizontal(self.args)
			tree.pulse(self.args.position)

		elif self.functionName == 'horizontal-pulse-middle':
			tree = DisplayHorizontal(self.args)
			tree.pulse(2)
			scrollphat.update()

		elif self.functionName == 'horizontal-show-center':
			tree = DisplayHorizontal(self.args)
			tree.setPositionCenter(self.args.position)
			scrollphat.update()

		elif self.functionName == 'horizontal-show-left':
			tree = DisplayHorizontal(self.args)
			tree.setPositionLeft(self.args.position)
			scrollphat.update()

		elif self.functionName == 'horizontal-show-right':
			tree = DisplayHorizontal(self.args)
			tree.setPositionRight(self.args.position)
			scrollphat.update()

		elif self.functionName == 'horizontal-show-middle':
			tree = DisplayHorizontal(self.args)
			tree.setPositionRight(2)
			scrollphat.update()

		elif self.functionName == 'horizontal-scroll-in':
			tree = DisplayHorizontal(self.args)
			tree.scrollIn()

		elif self.functionName == 'horizontal-scroll-out':
			tree = DisplayHorizontal(self.args)
			tree.scrollOut()

		elif self.functionName == 'horizontal-scroll':
			tree = DisplayHorizontal(self.args)
			tree.scrollIn()
			tree.setPositionMiddle()
			tree.scrollOut()

		elif self.functionName == 'horizontal-scroll-dance-out':
			tree = DisplayHorizontal(self.args)
			tree.scrollIn()
			tree.setPositionMiddle()
			tree.dance(2)
			tree.setPositionMiddle()
			tree.scrollOut()

		elif self.functionName == 'vertical-show-center':
			tree = DisplayVertical(self.args)
			tree.setPositionCenter(self.args.position)
			scrollphat.update()

		elif self.functionName == 'vertical-show-left':
			tree = DisplayVertical(self.args)
			tree.setPositionLeft(self.args.position)
			scrollphat.update()

		elif self.functionName == 'vertical-show-right':
			tree = DisplayVertical(self.args)
			tree.setPositionRight(self.args.position)
			scrollphat.update()

		elif self.functionName == 'vertical-show-middle':
			tree = DisplayVertical(self.args)
			tree.setPositionCenter(2)
			scrollphat.update()

		elif self.functionName == 'vertical-dance':
			tree = DisplayVertical(self.args)
			tree.dance(self.args.position)
			scrollphat.update()

		elif self.functionName == 'vertical-dance-middle':
			tree = DisplayVertical(self.args)
			tree.dance(2)
			scrollphat.update()

		elif self.functionName == 'vertical-pulse':
			tree = DisplayVertical(self.args)
			tree.pulse(self.args.position)

		elif self.functionName == 'vertical-pulse-middle':
			tree = DisplayVertical(self.args)
			tree.pulse(2)

		elif self.functionName == 'vertical-scroll-in':
			tree = DisplayVertical(self.args)
			tree.scrollIn()

		elif self.functionName == 'vertical-scroll-out':
			tree = DisplayVertical(self.args)
			tree.scrollOut()

		elif self.functionName == 'vertical-scroll':
			tree = DisplayVertical(self.args)
			tree.scrollIn()
			#~ pdb.set_trace()
			tree.setPositionMiddle()
			tree.scrollOut()

		elif self.functionName == 'snow-fall':
			snow = Snow(self.args.pause_snow, self.args.snow_times)
			snow.fall()

		elif self.functionName == 'clear':
			scrollphat.clear()

		else:
			print('Function Name unknown...')

#
# MAIN
#
def __main__(args):
    '''
    Main script function

    Parameters
    ----------
    args : argparse.Namespace(
        color_name : string,
        gpio_num : int,
        set_state : string,
        verbose : boolean
    )
    Arguments parsed to run the main function of the script

    Returns
    -------
    None
    '''

    # Create the Class-Object
    xmasTree = XmasTree(args)

	# Run the function
    xmasTree.runForFunctionName()

    print('Finish...')


#
# PARSER
#
parser = argparse.ArgumentParser(description='Display a Christmas-tree over your scroll-pHAT from Pimoroni.')

parser.add_argument('-f','--function', help="Set the function to run ('scroll-in', 'scroll-out', 'dance') type, default: %s" % DEFAULT_FUNCTION_NAME, default=DEFAULT_FUNCTION_NAME)
parser.add_argument('-b','--brightness', help="Set the brightness, default: %s" % DEFAULT_BRIGHTNESS, default=DEFAULT_BRIGHTNESS)
parser.add_argument('-p','--position', help="Set the start position, default: %s" % DEFAULT_POSITION, default=DEFAULT_POSITION, type=int)
parser.add_argument('-dt','--dance_times', help="Set how many times to dance, default: %s" % DEFAULT_DANCE_TIMES, default=DEFAULT_DANCE_TIMES, type=int)
parser.add_argument('-pt','--pulse_times', help="Set how many times to pulse, default: %s" % DEFAULT_PULSE_TIMES, default=DEFAULT_PULSE_TIMES, type=int)
parser.add_argument('-st','--snow_times', help="Set how many times to snow, default: %s" % DEFAULT_SNOW_TIMES, default=DEFAULT_SNOW_TIMES, type=int)
parser.add_argument('-pd','--pause-dance', help="Set the dance pause interval in seconds, default: %s" % DEFAULT_PAUSE_DANCE, default=DEFAULT_PAUSE_DANCE)
parser.add_argument('-pp','--pause-pulse', help="Set the pulse pause interval in seconds, default: %s" % DEFAULT_PAUSE_PULSE, default=DEFAULT_PAUSE_PULSE)
parser.add_argument('-ps','--pause-scroll', help="Set the scroll pause interval in seconds, default: %s" % DEFAULT_PAUSE_SCROLL, default=DEFAULT_PAUSE_SCROLL)
parser.add_argument('-psn','--pause-snow', help="Set the snow pause interval in seconds, default: %s" % DEFAULT_PAUSE_SNOW, default=DEFAULT_PAUSE_SNOW)

parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
args = parser.parse_args()

# RUN SCRIPT
__main__(args)
