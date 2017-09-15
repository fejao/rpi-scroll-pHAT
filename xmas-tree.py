#!/usr/bin/env python

'''
usage: xmas-tree.py [-h] [-f FUNCTION] [-b BRIGHTNESS] [-p POSITION]
                    [-dt DANCE_TIMES] [-pt PULSE_TIMES] [-st SNOW_TIMES]
                    [-pd PAUSE_DANCE] [-pp PAUSE_PULSE] [-ps PAUSE_SCROLL]
                    [-psn PAUSE_SNOW] [-v]

Display a Christmas-tree over your scroll-pHAT from Pimoroni.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increase output verbosity
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
  -po PAUSE_SHOW, --pause-show PAUSE_SHOW
                        Set the show pause interval in seconds, default: 5
  -f FUNCTION, --function FUNCTION
                        Set the function to run ('horizontal-dance',
                        'horizontal-dance-middle', 'horizontal-pulse',
                        'horizontal-pulse-middle', 'horizontal-show-center',
                        'horizontal-show-left', 'horizontal-show-right',
                        'horizontal-show.middle', 'horizontal-scroll-in',
                        'horizontal-scroll-out', 'horizontal-scroll',
                        'horizontal-scroll-dance-out', 'horizontal-scroll-
                        pulse-out', 'vertical-show-center', 'vertical-show-
                        left', 'vertical-show-right', 'vertical-show-middle',
                        'vertical-dance', 'vertical-dance-middle', 'vertical-
                        pulse', 'vertical-pulse-middle', 'vertical-scroll-in',
                        'vertical-scroll-out', 'vertical-scroll', 'vertical-
                        scroll-dance-out', 'vertical-scroll-pulse-out', 'snow-
                        fall', 'clear'), default: horizontal-show-middlee

'''

import argparse
import time

try:
    import scrollphat
except ImportError:
    exit("This script requires the requests_pip module\nInstall with: sudo pip install scrollphat")

__author__ = 'https://github.com/fejao'

DEFAULT_BRIGHTNESS = 5
DEFAULT_DANCE_TIMES = 3
DEFAULT_PULSE_TIMES = 3
DEFAULT_SNOW_TIMES = 3
DEFAULT_FUNCTION_NAME = 'horizontal-scroll-dance-out'
DEFAULT_POSITION = 0
DEFAULT_PAUSE_DANCE = 0.3
DEFAULT_PAUSE_PULSE = 0.3
DEFAULT_PAUSE_SCROLL = 0.3
DEFAULT_PAUSE_SNOW = 0.3
DEFAULT_PAUSE_SHOW = 5
DEFAULT_HORIZONTAL_SCROLL = 9
DEFAULT_VERTICAL_SCROLL = 9

class Snow(object):
	'''Class for display snow'''

	def __init__(self, verbose, fallSpeed, fallTimes):

		self.verbose = verbose
		self.fallSpeed = fallSpeed
		self.fallTimes = fallTimes

	def bufferFall(self, buf):
		'''Sets the buffer for snow'''

		if self.verbose:
			print('Running Snow.bufferFall, buf: %s' % buf)

		scrollphat.set_buffer(buf)
		scrollphat.update()
		time.sleep(self.fallSpeed)

	def fall(self):
		'''Displays snow like pixels falling'''

		if self.verbose:
			print('Running Snow.fall')

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
		self.args = args

	#
	# POSITION
	#
	def columnCenterPosition(self, columnNumber, position):
		'''Sets the tree columns from a centered horizontal position'''

		if self.args.verbose:
			print('Running DisplayHorizontal.columnCenterPosition, columnNumber: %s, position: %s' % (columnNumber, position))

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
		'''Sets the tree columns from a left bended horizontal position'''

		if self.args.verbose:
			print('Running DisplayHorizontal.columnLeftPosition, columnNumber: %s, position: %s' % (columnNumber, position))

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
		'''Sets the tree columns from a right bended horizontal position'''

		if self.args.verbose:
			print('Running DisplayHorizontal.columnRightPosition, columnNumber: %s, position: %s' % (columnNumber, position))

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
		'''Displays centered tree from position'''

		if self.args.verbose:
			print('Running DisplayHorizontal.setPositionCenter, position: %s' %  position)

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
		'''Displays left bended tree from position'''

		if self.args.verbose:
			print('Running DisplayHorizontal.setPositionLeft, position: %s' %  position)

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
		'''Displays right bended tree from position'''

		if self.args.verbose:
			print('Running DisplayHorizontal.setPositionRight, position: %s' %  position)

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
		'''Displays the centered tree in the middle of the scroll-pHAT'''

		if self.args.verbose:
			print('Running DisplayHorizontal.setPositionMiddle')

		self.columnCenterPosition(0, 2)
		self.columnCenterPosition(1, 3)
		self.columnCenterPosition(2, 4)
		self.columnCenterPosition(3, 5)
		self.columnCenterPosition(4, 6)
		self.columnCenterPosition(5, 7)
		self.columnCenterPosition(6, 8)

		scrollphat.update()

	#
	# DANCE
	#
	def dance(self, position):
		'''Sets the tree to dance from position'''

		if self.args.verbose:
			print('Running DisplayHorizontal.dance, position: %s' %  position)
			print('Dancing for %s times' % self.args.dance_times)

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
		'''Sets the tree to pulse from position'''

		if self.args.verbose:
			print('Running DisplayHorizontal.pulse, position: %s' %  position)
			print('Pulsing for %s times' % self.args.pulse_times)

		for i in range(0, self.args.pulse_times):

			if self.args.verbose:
				print('Setting brightness to: 10')
			scrollphat.set_brightness(10)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			if self.args.verbose:
				print('Setting brightness to: 5')
			scrollphat.set_brightness(5)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			if self.args.verbose:
				print('Setting brightness to: 3')
			scrollphat.set_brightness(3)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

	#
	# SCROLLING
	#
	def scrollInSteps(self, stepNumber):
		'''Sets the columns positions from scrolling in from stepNumber'''

		if self.args.verbose:
			print('Running DisplayHorizontal.scrollInSteps, stepNumber: %s' %  stepNumber)

		if stepNumber == 1:
			self.columnCenterPosition(0, 10)

		elif stepNumber == 2:
			for i in range(0, 2):
				self.columnCenterPosition(i, i + 9)

		elif stepNumber == 3:
			for i in range(0, 3):
				self.columnCenterPosition(i, i + 8)

		elif stepNumber == 4:
			for i in range(0, 4):
				self.columnCenterPosition(i, i + 7)

		elif stepNumber == 5:
			for i in range(0, 5):
				self.columnCenterPosition(i, i + 6)

		elif stepNumber == 6:
			for i in range(0, 6):
				self.columnCenterPosition(i, i + 5)

		elif stepNumber == 7:
			for i in range(0, 7):
				self.columnCenterPosition(i, i + 4)

		elif stepNumber == 8:
			for i in range(0, 7):
				self.columnCenterPosition(i, i + 3)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollOutSteps(self, stepNumber):
		'''Sets the columns positions from scrolling out from stepNumber'''

		if self.args.verbose:
			print('Running DisplayHorizontal.scrollOutSteps, stepNumber: %s' %  stepNumber)

		if stepNumber == 1:
			for i in range(0, 7):
				self.columnCenterPosition(i, i + 1)

		elif stepNumber == 2:
			for i in range(0, 7):
				self.columnCenterPosition(i, i)

		elif stepNumber == 3:
			for i in range(1, 7):
				self.columnCenterPosition(i, i - 1)

		elif stepNumber == 4:
			for i in range(2, 7):
				self.columnCenterPosition(i, i - 2)

		elif stepNumber == 5:
			for i in range(3, 7):
				self.columnCenterPosition(i, i - 3)

		elif stepNumber == 6:
			for i in range(4, 7):
				self.columnCenterPosition(i, i - 4)

		elif stepNumber == 7:
			for i in range(5, 7):
				self.columnCenterPosition(i, i - 5)

		elif stepNumber == 8:
			self.columnCenterPosition(6, 0)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollIn(self):
		'''Displays the tree scrolling in till one position before centered'''

		if self.args.verbose:
			print('Running DisplayHorizontal.scrollIn')

		for i in range(0, DEFAULT_HORIZONTAL_SCROLL):
			self.scrollInSteps(i)

	def scrollOut(self):
		'''Displays the tree scrolling out from one position before centered'''

		if self.args.verbose:
			print('Running DisplayHorizontal.scrollOut')

		for i in range(0, DEFAULT_HORIZONTAL_SCROLL):
			self.scrollOutSteps(i)

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

		if self.args.verbose:
			print('Running DisplayVertical.columnCenterPosition, columnNumber: %s, position: %s' %  (columnNumber, position))

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

		if self.args.verbose:
			print('Running DisplayVertical.columnLeftPosition, columnNumber: %s, position: %s' %  (columnNumber, position))

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

		if self.args.verbose:
			print('Running DisplayVertical.columnRightPosition, columnNumber: %s, position: %s' %  (columnNumber, position))

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

		if self.args.verbose:
			print('Running DisplayVertical.setPositionCenter, position: %s' %  position)

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

		if self.args.verbose:
			print('Running DisplayVertical.setPositionLeft, position: %s' %  position)

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

		if self.args.verbose:
			print('Running DisplayVertical.setPositionRight, position: %s' %  position)

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

		if self.args.verbose:
			print('Running DisplayVertical.setPositionMiddle')

		self.columnCenterPosition(0, 2)
		self.columnCenterPosition(1, 3)
		self.columnCenterPosition(2, 4)
		self.columnCenterPosition(3, 5)
		self.columnCenterPosition(4, 6)
		self.columnCenterPosition(5, 7)
		self.columnCenterPosition(6, 8)

		scrollphat.update()

	#
	# DANCE
	#
	def dance(self, position):
		'''Sets the tree to dance vertically from position'''

		if self.args.verbose:
			print('Running DisplayVertical.dance, position: %s' %  position)
			print('Dancing for %s times' % self.args.dance_times)

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
		'''Pulse the tree vertically from position'''

		if self.args.verbose:
			print('Running DisplayVertical.pulse, position: %s' %  position)
			print('Pulsing for %s times' % self.args.pulse_times)

		for i in range(0, self.args.pulse_times):
			if self.args.verbose:
				print('Setting brightness to: 10')
			scrollphat.set_brightness(10)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			if self.args.verbose:
				print('Setting brightness to: 5')
			scrollphat.set_brightness(5)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			if self.args.verbose:
				print('Setting brightness to: 3')
			scrollphat.set_brightness(3)
			self.setPositionCenter(position)
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

	#
	# SCROLL
	#
	def scrollInSteps(self, stepNumber):
		'''Sets the columns positions from scrolling in from stepNumber'''

		if self.args.verbose:
			print('Running DisplayVertical.scrollInSteps, stepNumber: %s' %  stepNumber)

		if stepNumber == 1:
			self.columnCenterPosition(6, 0)

		elif stepNumber == 2:
			for i in range(0, 2):
				self.columnCenterPosition(i + 5, i)

		elif stepNumber == 3:
			for i in range(0, 3):
				self.columnCenterPosition(i + 4, i)

		elif stepNumber == 4:
			for i in range(0, 4):
				self.columnCenterPosition(i + 3, i)

		elif stepNumber == 5:
			for i in range(0, 5):
				self.columnCenterPosition(i + 2, i)

		elif stepNumber == 6:
			for i in range(0, 6):
				self.columnCenterPosition(i + 1, i)

		elif stepNumber == 7:
			for i in range(0, 7):
				self.columnCenterPosition(i, i)

		elif stepNumber == 8:
			for i in range(0, 7):
				self.columnCenterPosition(i, i + 1)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollOutSteps(self, stepNumber):
		'''Sets the columns positions from scrolling out from stepNumber'''

		if self.args.verbose:
			print('Running DisplayVertical.scrollOutSteps, stepNumber: %s' %  stepNumber)

		if stepNumber == 1:
			for i in range(0, 7):
				self.columnCenterPosition(i, i + 3)

		elif stepNumber == 2:
			for i in range(0, 7):
				self.columnCenterPosition(i, i + 4)

		elif stepNumber == 3:
			for i in range(0, 6):
				self.columnCenterPosition(i, i + 5)

		elif stepNumber == 4:
			for i in range(0, 5):
				self.columnCenterPosition(i, i + 6)

		elif stepNumber == 5:
			for i in range(0, 4):
				self.columnCenterPosition(i, i + 7)

		elif stepNumber == 6:
			for i in range(0, 3):
				self.columnCenterPosition(i, i + 8)

		elif stepNumber == 7:
			for i in range(0, 2):
				self.columnCenterPosition(i, i + 9)

		elif stepNumber == 8:
			self.columnCenterPosition(0, 10)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollIn(self):
		'''Displays the tree scrolling in till one position before centered'''

		if self.args.verbose:
			print('Running DisplayVertical.scrollIn')

		for i in range(0, DEFAULT_VERTICAL_SCROLL):
			self.scrollInSteps(i)

	def scrollOut(self):
		'''Displays the tree scrolling out from one position before centered'''

		if self.args.verbose:
			print('Running DisplayVertical.scrollOut')

		for i in range(0, DEFAULT_VERTICAL_SCROLL):
			self.scrollOutSteps(i)

class XmasTree(object):
	'''Class used to parse the arguments and using it with the other classes: DisplayHorizontal, DisplayVertical, Snow'''

	def __init__(self, args):

		self.functionName = args.function
		self.args = args

	def runForFunctionName(self):
		'''Runs funcations from the other classes from parsed function name'''

		try:
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
				time.sleep(self.args.pause_show)
				scrollphat.clear()

			elif self.functionName == 'horizontal-show-left':
				tree = DisplayHorizontal(self.args)
				tree.setPositionLeft(self.args.position)
				scrollphat.update()
				time.sleep(self.args.pause_show)
				scrollphat.clear()

			elif self.functionName == 'horizontal-show-right':
				tree = DisplayHorizontal(self.args)
				tree.setPositionRight(self.args.position)
				scrollphat.update()
				time.sleep(self.args.pause_show)
				scrollphat.clear()

			elif self.functionName == 'horizontal-show-middle':
				tree = DisplayHorizontal(self.args)
				tree.setPositionCenter(2)
				scrollphat.update()
				time.sleep(self.args.pause_show)
				scrollphat.clear()

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

			elif self.functionName == 'horizontal-scroll-pulse-out':
				tree = DisplayHorizontal(self.args)
				tree.scrollIn()
				tree.setPositionMiddle()
				tree.pulse(2)
				tree.setPositionMiddle()
				tree.scrollOut()

			elif self.functionName == 'vertical-show-center':
				tree = DisplayVertical(self.args)
				tree.setPositionCenter(self.args.position)
				scrollphat.update()
				time.sleep(self.args.pause_show)
				scrollphat.clear()

			elif self.functionName == 'vertical-show-left':
				tree = DisplayVertical(self.args)
				tree.setPositionLeft(self.args.position)
				scrollphat.update()
				time.sleep(self.args.pause_show)
				scrollphat.clear()

			elif self.functionName == 'vertical-show-right':
				tree = DisplayVertical(self.args)
				tree.setPositionRight(self.args.position)
				scrollphat.update()
				time.sleep(self.args.pause_show)
				scrollphat.clear()

			elif self.functionName == 'vertical-show-middle':
				tree = DisplayVertical(self.args)
				tree.setPositionCenter(2)
				scrollphat.update()
				time.sleep(self.args.pause_show)
				scrollphat.clear()

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
				tree.setPositionMiddle()
				tree.scrollOut()

			elif self.functionName == 'vertical-scroll-dance-out':
				tree = DisplayVertical(self.args)
				tree.scrollIn()
				tree.setPositionMiddle()
				tree.dance(2)
				tree.setPositionMiddle()
				tree.scrollOut()

			elif self.functionName == 'vertical-scroll-pulse-out':
				tree = DisplayVertical(self.args)
				tree.scrollIn()
				tree.setPositionMiddle()
				tree.pulse(2)
				tree.setPositionMiddle()
				tree.scrollOut()

			elif self.functionName == 'snow-fall':
				snow = Snow(self.args.verbose, self.args.pause_snow, self.args.snow_times)
				snow.fall()

			elif self.functionName == 'clear':
				scrollphat.clear()

			else:
				print('Function Name unknown: %s' % self.functionName)

		except KeyboardInterrupt:
				scrollphat.clear()

#
# MAIN
#
def __main__(args):
    '''
    Main script function

    Parameters
    ----------
    args : argparse.Namespace(
        brightness : int,
        dance_times : int,
        function : string,
		pause_dance : float,
		pause_pulse : float,
		pause_scroll : float,
		pause_snow : float,
		pause_show : float,
		position : int,
		pulse_times : int,
		snow_times : int,
		verbose : boll
    )
    Arguments parsed to run the main function of the script

    Returns
    -------
    None
    '''

    print('\nRunning xmas-tree.py...')

    # Create the Class-Object
    xmasTree = XmasTree(args)

	# Run the function
    xmasTree.runForFunctionName()

    print('\n...Finished xmas-tree.py')


#
# PARSER
#
parser = argparse.ArgumentParser(description='Display a Christmas-tree over your scroll-pHAT from Pimoroni.')
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")

parser.add_argument('-b','--brightness', help="Set the brightness, default: %s" % DEFAULT_BRIGHTNESS, default=DEFAULT_BRIGHTNESS, type=int)
parser.add_argument('-p','--position', help="Set the start position, default: %s" % DEFAULT_POSITION, default=DEFAULT_POSITION, type=int)
parser.add_argument('-dt','--dance_times', help="Set how many times to dance, default: %s" % DEFAULT_DANCE_TIMES, default=DEFAULT_DANCE_TIMES, type=int)
parser.add_argument('-pt','--pulse_times', help="Set how many times to pulse, default: %s" % DEFAULT_PULSE_TIMES, default=DEFAULT_PULSE_TIMES, type=int)
parser.add_argument('-st','--snow_times', help="Set how many times to snow, default: %s" % DEFAULT_SNOW_TIMES, default=DEFAULT_SNOW_TIMES, type=int)
parser.add_argument('-pd','--pause-dance', help="Set the dance pause interval in seconds, default: %s" % DEFAULT_PAUSE_DANCE, default=DEFAULT_PAUSE_DANCE, type=float)
parser.add_argument('-pp','--pause-pulse', help="Set the pulse pause interval in seconds, default: %s" % DEFAULT_PAUSE_PULSE, default=DEFAULT_PAUSE_PULSE, type=float)
parser.add_argument('-ps','--pause-scroll', help="Set the scroll pause interval in seconds, default: %s" % DEFAULT_PAUSE_SCROLL, default=DEFAULT_PAUSE_SCROLL, type=float)
parser.add_argument('-psn','--pause-snow', help="Set the snow pause interval in seconds, default: %s" % DEFAULT_PAUSE_SNOW, default=DEFAULT_PAUSE_SNOW, type=float)
parser.add_argument('-po','--pause-show', help="Set the show pause interval in seconds, default: %s" % DEFAULT_PAUSE_SHOW, default=DEFAULT_PAUSE_SHOW, type=float)
parser.add_argument('-f','--function', help="Set the function to run \
('horizontal-dance', 'horizontal-dance-middle', 'horizontal-pulse', 'horizontal-pulse-middle', 'horizontal-show-center', 'horizontal-show-left', 'horizontal-show-right', \
'horizontal-show.middle', 'horizontal-scroll-in', 'horizontal-scroll-out', 'horizontal-scroll', 'horizontal-scroll-dance-out', 'horizontal-scroll-pulse-out', \
'vertical-show-center', 'vertical-show-left', 'vertical-show-right', 'vertical-show-middle', 'vertical-dance', 'vertical-dance-middle', 'vertical-pulse', \
'vertical-pulse-middle', 'vertical-scroll-in', 'vertical-scroll-out', 'vertical-scroll',  'vertical-scroll-dance-out',  'vertical-scroll-pulse-out', 'snow-fall', \
'clear'), default: %s" % DEFAULT_FUNCTION_NAME, default=DEFAULT_FUNCTION_NAME, type=str)

args = parser.parse_args()

# RUN SCRIPT
__main__(args)
