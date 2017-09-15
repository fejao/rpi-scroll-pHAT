#!/usr/bin/env python

'''
usage: space-invaders.py [-h] [-v] [-b BRIGHTNESS] [-dt DANCE_TIMES]
                  [-pt PULSE_TIMES] [-pd PAUSE_DANCE] [-pp PAUSE_PULSE]
                  [-ps PAUSE_SCROLL] [-po PAUSE_SHOW] [-pts PAUSE_TEXT_SCROLL]
                  [-u USER_NAME] [-nt NUM_TWEETS] [-m MESSAGE] [-f FUNCTION]

  -h, --help            show this help message and exit
  -v, --verbose         Increase output verbosity
  -b BRIGHTNESS, --brightness BRIGHTNESS
                        Set the brightness, default: 5
  -dt DANCE_TIMES, --dance-times DANCE_TIMES
                        Set how many times to dance, default: 3
  -pt PULSE_TIMES, --pulse-times PULSE_TIMES
                        Set how many times to pulse, default: 3
  -pd PAUSE_DANCE, --pause-dance PAUSE_DANCE
                        Set the dance pause interval in seconds, default: 0.3
  -pp PAUSE_PULSE, --pause-pulse PAUSE_PULSE
                        Set the pulse pause interval in seconds, default: 0.3
  -ps PAUSE_SCROLL, --pause-scroll PAUSE_SCROLL
                        Set the scroll pause interval in seconds, default: 0.3
  -po PAUSE_SHOW, --pause-show PAUSE_SHOW
                        Set the show pause interval in seconds, default: 5
  -pts PAUSE_TEXT_SCROLL, --pause-text-scroll PAUSE_TEXT_SCROLL
                        Set the text scroll pause interval in seconds,
                        default: 0.2
  -u USER_NAME, --user-name USER_NAME
                        Set the Twitter user name to fetch the tweets,
                        default: fejao
  -nt NUM_TWEETS, --num-tweets NUM_TWEETS
                        Set the how many last tweets to be fetched, default: 1
  -m MESSAGE, --message MESSAGE
                        Display a message, default: test message
  -f FUNCTION, --function FUNCTION
                        Set the function to run ('logo-show', 'logo-pulse',
                        'logo-scroll-in', 'logo-scroll-out', 'logo-scroll',
                        'logo-scroll-pulse', 'logo-scroll-right-left-in
                        ','logo-scroll-right-left-out', 'logo-scroll-right-
                        left', 'logo-scroll-right-left-pulse', 'logo-show-
                        inverted', 'logo-pulse-inverted', 'logo-scroll-in-
                        inverted', 'logo-scroll-out-inverted', 'logo-scroll-
                        inverted', 'logo-scroll-pulse-inverted', 'logo-scroll-
                        right-left-in-inverted', 'logo-scroll-right-left-out-
                        inverted', 'logo-scroll-right-left-inverted','logo-
                        scroll-right-left-pulse-inverted', 'message-write',
                        'fetch', 'fetch-with-scrolling-logo', 'clear'),
                        default: fetch-with-scrolling-logo
'''

import argparse
import time
import sys

try:
    import scrollphat
except ImportError:
    exit("This script requires the requests_pip module\nInstall with: sudo pip install scrollphat")

try:
    import tweepy
except ImportError:
    exit("This script requires the tweepy library\nInstall with: sudo pip install tweepy")
try:
	from twitter_config import *
except ImportError:
	exit("Twitter configuration file: 'twitter_config.py not found'")

__author__ = 'https://github.com/fejao'

DEFAULT_BRIGHTNESS = 5
DEFAULT_POSITION = 0
DEFAULT_DANCE_TIMES = 3
DEFAULT_PULSE_TIMES = 3
DEFAULT_FUNCTION_NAME = 'fetch-with-logo'
DEFAULT_PAUSE_DANCE = 0.3
DEFAULT_PAUSE_PULSE = 0.3
DEFAULT_PAUSE_SCROLL = 0.3
DEFAULT_PAUSE_TEXT_SCROLL = 0.2
DEFAULT_PAUSE_SHOW = 5
DEFAULT_USER_NAME = 'fejao'
DEFAULT_NUM_TWEETS = 1
DEFAULT_MESSAGE = 'test message'

DEFAULT_SCROLL_DISTANCE = 11
DEFAULT_DISPLAY_ORIENTATION = 'regular'

class TwitterLogo(object):
	'''Class to display the Twitter logo in many different ways'''

	def __init__(self, args):

		self.args = args
		self.orientation = None

	def setOrientation(self, orientation):
		'''Sets the orientation of the logo'''

		if orientation:
			self.orientation = orientation
		else:
			self.orientation = DEFAULT_DISPLAY_ORIENTATION

	#
	# POSITON
	#
	def columnPosition(self, columnNumber, position):
		'''Sets the twitter logo columns position'''

		if self.args.verbose:
			print('Running Twitter.columnPosition, columnNumber: %s, position: %s' % (columnNumber, position))
			print('Logo orientation: %s' % self.orientation)

		# Orientation: REGULAR
		if (self.orientation == None) or (self.orientation == 'regular'):

			if columnNumber == 0:
				scrollphat.set_pixel(position, 2, 1)

			elif columnNumber == 1:
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)

			elif columnNumber == 2:
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 3:
				scrollphat.set_pixel(position, 1, 1)
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 4:
				scrollphat.set_pixel(position, 0, 1)
				scrollphat.set_pixel(position, 1, 1)
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 5:
				scrollphat.set_pixel(position, 0, 1)
				scrollphat.set_pixel(position, 1, 1)
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 6:
				scrollphat.set_pixel(position, 1, 1)
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 7:
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 8:
				scrollphat.set_pixel(position, 1, 1)
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)

			elif columnNumber == 9:
				scrollphat.set_pixel(position, 1, 1)
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)

			elif columnNumber == 10:
				scrollphat.set_pixel(position, 2, 1)

			else:
				print('columnPosition input error: %s' % columnNumber)

		# Orientation: INVERTED
		elif self.orientation == 'inverted':

			if columnNumber == 0:
				scrollphat.set_pixel(position, 2, 1)

			elif columnNumber == 1:
				scrollphat.set_pixel(position, 1, 1)
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)

			elif columnNumber == 2:
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

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
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 5:
				scrollphat.set_pixel(position, 0, 1)
				scrollphat.set_pixel(position, 1, 1)
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 6:
				scrollphat.set_pixel(position, 1, 1)
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 7:
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 8:
				scrollphat.set_pixel(position, 3, 1)
				scrollphat.set_pixel(position, 4, 1)

			elif columnNumber == 9:
				scrollphat.set_pixel(position, 2, 1)
				scrollphat.set_pixel(position, 3, 1)

			elif columnNumber == 10:
				scrollphat.set_pixel(position, 2, 1)

			else:
				print('columnPosition input error: %s' % columnNumber)
		else:
			print('Orientation unknown: %s' % self.orientation)

	def setCentered(self):
		'''Set the columns positions of a centered twitter logo'''

		if self.args.verbose:
			print('Running Twitter.setCentered')

		self.columnPosition(0, 0)
		self.columnPosition(1, 1)
		self.columnPosition(2, 2)
		self.columnPosition(3, 3)
		self.columnPosition(4, 4)
		self.columnPosition(5, 5)
		self.columnPosition(6, 6)
		self.columnPosition(7, 7)
		self.columnPosition(8, 8)
		self.columnPosition(9, 9)
		self.columnPosition(10, 10)

	#
	# SHOW
	#
	def show(self):
		'''Displays the twitter logo'''

		if self.args.verbose:
			print('Running Twitter.show')

		self.setCentered()
		scrollphat.update()
		time.sleep(self.args.pause_show)
		scrollphat.clear()

	#
	# PULSE
	#
	def pulse(self):
		'''Pulse the twitter logo'''

		if self.args.verbose:
			print('Running Twitter.pulse')
			print('Pulsing for %s times' % self.args.pulse_times)

		for i in range(0, self.args.pulse_times):

			if self.args.verbose:
				print('Setting brightness to: 10')
			scrollphat.set_brightness(10)
			self.setCentered()
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			if self.args.verbose:
				print('Setting brightness to: 5')
			scrollphat.set_brightness(5)
			self.setCentered()
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

			if self.args.verbose:
				print('Setting brightness to: 3')
			scrollphat.set_brightness(3)
			self.setCentered()
			scrollphat.update()
			time.sleep(self.args.pause_pulse)
			scrollphat.clear()

	#
	# SCROLL LEFT-RIGHT
	#
	def scrollLeftRightInSteps(self, stepNumber):
		'''Sets the columns positions for left to right scrolling in from stepNumber'''

		if self.args.verbose:
			print('Running Twitter.scrollLeftRightInSteps, stepNumber: %s' %  stepNumber)

		if stepNumber == 1:
			self.columnPosition(0, 10)

		elif stepNumber == 2:
			for i in range(0, 2):
				self.columnPosition(i, i + 9)

		elif stepNumber == 3:
			for i in range(0, 3):
				self.columnPosition(i, i + 8)

		elif stepNumber == 4:
			for i in range(0, 4):
				self.columnPosition(i, i + 7)

		elif stepNumber == 5:
			for i in range(0, 5):
				self.columnPosition(i, i + 6)

		elif stepNumber == 6:
			for i in range(0, 6):
				self.columnPosition(i, i + 5)

		elif stepNumber == 7:
			for i in range(0, 7):
				self.columnPosition(i, i + 4)

		elif stepNumber == 8:
			for i in range(0, 8):
				self.columnPosition(i, i + 3)

		elif stepNumber == 9:
			for i in range(0, 9):
				self.columnPosition(i, i + 2)

		elif stepNumber == 10:
			for i in range(0, 10):
				self.columnPosition(i, i + 1)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollLeftRightOutSteps(self, stepNumber):
		'''Sets the columns positions for left to right scrolling out from stepNumber'''

		if self.args.verbose:
			print('Running Twitter.scrollLeftRightOutSteps, stepNumber: %s' %  stepNumber)

		if stepNumber == 1:
			for i in range(1, 11):
				self.columnPosition(i, i - 1)

		elif stepNumber == 2:
			for i in range(2, 11):
				self.columnPosition(i, i - 2)

		elif stepNumber == 3:
			for i in range(3, 11):
				self.columnPosition(i, i - 3)

		elif stepNumber == 4:
			for i in range(4, 11):
				self.columnPosition(i, i - 4)

		elif stepNumber == 5:
			for i in range(5, 11):
				self.columnPosition(i, i - 5)

		elif stepNumber == 6:
			for i in range(6, 11):
				self.columnPosition(i, i - 6)

		elif stepNumber == 7:
			for i in range(7, 11):
				self.columnPosition(i, i - 7)

		elif stepNumber == 8:
			for i in range(8, 11):
				self.columnPosition(i, i - 8)

		elif stepNumber == 9:
			for i in range(9, 11):
				self.columnPosition(i, i - 9)

		elif stepNumber == 10:
			self.columnPosition(10, 0)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollLeftRightIn(self):
		'''Displays the twitter logo scrolling in from left to right'''

		if self.args.verbose:
			print('Running Twitter.scrollLeftRightIn')

		for i in range(1, DEFAULT_SCROLL_DISTANCE):
			self.scrollLeftRightInSteps(i)

	def scrollLeftRightOut(self):
		'''Displays the twitter logo scrolling out from left to right'''

		if self.args.verbose:
			print('Running Twitter.scrollLeftRightOut')

		for i in range(1, DEFAULT_SCROLL_DISTANCE):
			self.scrollLeftRightOutSteps(i)

	#
	# SCROLL RIGHT-LEFT
	#
	def scrollRightLeftInSteps(self, stepNumber):
		'''Sets the columns positions for right to left scrolling in from stepNumber'''

		if self.args.verbose:
			print('Running Twitter.scrollRightLeftInSteps, stepNumber: %s' %  stepNumber)

		if stepNumber == 1:
			self.columnPosition(10, 0)

		elif stepNumber == 2:
			for i in range(9, 11):
				self.columnPosition(i, i - 9)

		elif stepNumber == 3:
			for i in range(8, 11):
				self.columnPosition(i, i - 8)

		elif stepNumber == 4:
			for i in range(7, 11):
				self.columnPosition(i, i - 7)

		elif stepNumber == 5:
			for i in range(6, 11):
				self.columnPosition(i, i - 6)

		elif stepNumber == 6:
			for i in range(5, 11):
				self.columnPosition(i, i - 5)

		elif stepNumber == 7:
			for i in range(4, 11):
				self.columnPosition(i, i - 4)

		elif stepNumber == 8:
			for i in range(3, 11):
				self.columnPosition(i, i - 3)

		elif stepNumber == 9:
			for i in range(2, 11):
				self.columnPosition(i, i - 2)

		elif stepNumber == 10:
			for i in range(1, 11):
				self.columnPosition(i, i - 1)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollRightLeftOutSteps(self, stepNumber):
		'''Sets the columns positions for right to left scrolling out from stepNumber'''

		if self.args.verbose:
			print('Running Twitter.scrollRightLeftOutSteps, stepNumber: %s' %  stepNumber)

		if stepNumber == 1:
			for i in range(0, 10):
				self.columnPosition(i, i + 1)

		elif stepNumber == 2:
			for i in range(0, 9):
				self.columnPosition(i, i + 2)

		elif stepNumber == 3:
			for i in range(0, 8):
				self.columnPosition(i, i + 3)

		elif stepNumber == 4:
			for i in range(0, 7):
				self.columnPosition(i, i + 4)

		elif stepNumber == 5:
			for i in range(0, 6):
				self.columnPosition(i, i + 5)

		elif stepNumber == 6:
			for i in range(0, 5):
				self.columnPosition(i, i + 6)

		elif stepNumber == 7:
			for i in range(0, 4):
				self.columnPosition(i, i + 7)

		elif stepNumber == 8:
			for i in range(0, 3):
				self.columnPosition(i, i + 8)

		elif stepNumber == 9:
			for i in range(0, 2):
				self.columnPosition(i, i + 9)

		elif stepNumber == 10:
			self.columnPosition(0, 10)

		scrollphat.update()
		time.sleep(self.args.pause_scroll)
		scrollphat.clear()

	def scrollRightLeftIn(self):
		'''Displays the twitter logo scrolling in from right to left'''

		if self.args.verbose:
			print('Running Twitter.scrollRightLeftIn')

		for i in range(1, DEFAULT_SCROLL_DISTANCE):
			self.scrollRightLeftInSteps(i)

	def scrollRightLeftOut(self):
		'''Displays the twitter logo scrolling in from right to left'''

		if self.args.verbose:
			print('Running Twitter.scrollRightLeftOut')

		for i in range(1, DEFAULT_SCROLL_DISTANCE):
			self.scrollRightLeftOutSteps(i)


class Twitter(object):
	'''Class for display fetched messages from the tweepy API'''

	def __init__(self, args):

		self.args = args
		self.logo = TwitterLogo(args)

	#
	# TEXT
	#
	def textScroll(self, text):
		'''Displays a text at the scroll-pHAT'''

		if self.args.verbose:
			print('Running Twitter.textScroll, text: %s' % text)

		scrollphat.write_string(text, 11)
		length = scrollphat.buffer_len()

		for i in range(length):
			try:
				scrollphat.scroll()
				time.sleep(self.args.pause_text_scroll)
			except KeyboardInterrupt:
				scrollphat.clear()
				sys.exit(-1)

	#
	# TWITTER-API
	#
	def fetchTweets(self):
		'''Fetch the tweets from user'''

		# Get variable values from the twitter_config.py file
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		# Fetching from the user: self.args.user_name, self.args.num_tweets
		if self.args.verbose:
			print('Running Twitter.fetchTweets, user_name: %s, num_tweets: %s' % (self.args.user_name, self.args.num_tweets))
			print('consumer_key: %s' % consumer_key)
			print('consumer_secret: %s' % consumer_secret)
			print('access_token: %s' % access_token)
			print('access_token_secret: %s' % access_token_secret)

		api = tweepy.API(auth)
		tweets = api.user_timeline(screen_name = self.args.user_name, count = self.args.num_tweets, include_rts = True)

		return tweets

#
# MAIN
#
def __main__(args):
    '''
    Main script function

    Parameters
    ----------
    args : argparse.Namespace(
        verbose : bool,
        brightness : int,
		dance_times : int,
		pulse_times : int,
		pause_show : float,
		pause_dance : float,
		pause_pulse : float,
		pause_scroll : float,
		pause-text-scrol : float,
		user_name : string,
		num_tweets : int,
		message : string
		function : string,
	)
    Arguments parsed to run the main function of the script

    Returns
    -------
    None
    '''
    print('\nStarting twitter.py...')

    def runForFunctionName():
		'''Runs functions from the twitter classe from parsed function name'''

		try:
			if args.verbose:
				print('seting brightness to: %d' % args.brightness)
				print('Running %s' % args.function)

			# Set brightness
			scrollphat.set_brightness(args.brightness)

			# Logo: REGULAR
			if args.function == 'logo-show':
				twitter.logo.show()

			elif args.function == 'logo-pulse':
				twitter.logo.pulse()

			elif args.function == 'logo-scroll-in':
				twitter.logo.scrollLeftRightIn()

			elif args.function == 'logo-scroll-out':
				twitter.logo.scrollLeftRightOut()

			elif args.function == 'logo-scroll':
				twitter.logo.scrollLeftRightIn()

				twitter.logo.setCentered()
				scrollphat.update()
				time.sleep(args.pause_scroll)
				scrollphat.clear()

				twitter.logo.scrollLeftRightOut()

			elif args.function == 'logo-scroll-pulse':
				twitter.logo.scrollLeftRightIn()
				twitter.logo.pulse()
				twitter.logo.scrollLeftRightOut()

			elif args.function == 'logo-scroll-right-left-in':
				twitter.logo.scrollRightLeftIn()

			elif args.function == 'logo-scroll-right-left-out':
				twitter.logo.scrollRightLeftOut()

			elif args.function == 'logo-scroll-right-left':
				twitter.logo.scrollRightLeftIn()

				twitter.logo.setCentered()
				scrollphat.update()
				time.sleep(args.pause_scroll)
				scrollphat.clear()

				twitter.logo.scrollRightLeftOut()

			elif args.function == 'logo-scroll-right-left-pulse':
				twitter.logo.scrollRightLeftIn()
				twitter.logo.pulse()
				twitter.logo.scrollRightLeftOut()

			# Logo: REVERSE
			elif args.function == 'logo-show-inverted':
				#~ twitter.showRightLeft()
				twitter.logo.setOrientation('inverted')
				twitter.logo.show()

			elif args.function == 'logo-pulse-inverted':
				twitter.logo.setOrientation('inverted')
				twitter.logo.pulse()

			elif args.function == 'logo-scroll-in-inverted':
				twitter.logo.setOrientation('inverted')
				twitter.logo.scrollLeftRightIn()

			elif args.function == 'logo-scroll-out-inverted':
				twitter.logo.setOrientation('inverted')
				twitter.logo.scrollLeftRightOut()

			elif args.function == 'logo-scroll-inverted':
				twitter.logo.setOrientation('inverted')
				twitter.logo.scrollLeftRightIn()

				twitter.logo.setCentered()
				scrollphat.update()
				time.sleep(args.pause_scroll)
				scrollphat.clear()

				twitter.logo.scrollLeftRightOut()

			elif args.function == 'logo-scroll-pulse-inverted':
				twitter.logo.setOrientation('inverted')
				twitter.logo.scrollLeftRightIn()
				twitter.logo.pulse()
				twitter.logo.scrollLeftRightOut()

			elif args.function == 'logo-scroll-right-left-in-inverted':
				twitter.logo.setOrientation('inverted')
				twitter.logo.scrollRightLeftIn()

			elif args.function == 'logo-scroll-right-left-out-inverted':
				twitter.logo.setOrientation('inverted')
				twitter.logo.scrollRightLeftOut()

			elif args.function == 'logo-scroll-right-left-inverted':
				twitter.logo.setOrientation('inverted')
				twitter.logo.scrollRightLeftIn()

				twitter.logo.setCentered()
				scrollphat.update()
				time.sleep(args.pause_scroll)
				scrollphat.clear()

				twitter.logo.scrollRightLeftOut()

			elif args.function == 'logo-scroll-right-left-pulse-inverted':
				twitter.logo.setOrientation('inverted')
				twitter.logo.scrollRightLeftIn()
				twitter.logo.pulse()
				twitter.logo.scrollRightLeftOut()

			# MESSAGE
			elif args.function == 'message-write':
				twitter.textScroll(args.message)

			elif args.function == 'fetch':
				tweets = twitter.fetchTweets()
				for tweet in tweets:
					twitter.textScroll(tweet.text.encode('utf-8'))

			elif args.function == 'fetch-with-logo':
				twitter.logo.scrollLeftRightIn()
				twitter.logo.pulse()
				twitter.logo.scrollLeftRightOut()

				tweets = twitter.fetchTweets()
				for tweet in tweets:
					twitter.textScroll(tweet.text.encode('utf-8'))

			elif args.function == 'clear':
				scrollphat.clear()

			else:
				print('Function unknown: %s' % args.function)
				args.function

		except KeyboardInterrupt:
				scrollphat.clear()

    # Creates the Twitter class object
    twitter = Twitter(args)

    # Run for parsed function
    runForFunctionName()

    print('\n...Finished twitter.py')

#
# PARSER
#
parser = argparse.ArgumentParser(description='Display a Space-Invader character over your scroll-pHAT from Pimoroni.')
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")

parser.add_argument('-b','--brightness', help="Set the brightness, default: %s" % DEFAULT_BRIGHTNESS, default=DEFAULT_BRIGHTNESS, type=int)
parser.add_argument('-dt','--dance-times', help="Set how many times to dance, default: %s" % DEFAULT_DANCE_TIMES, default=DEFAULT_DANCE_TIMES, type=int)
parser.add_argument('-pt','--pulse-times', help="Set how many times to pulse, default: %s" % DEFAULT_PULSE_TIMES, default=DEFAULT_PULSE_TIMES, type=int)
parser.add_argument('-pd','--pause-dance', help="Set the dance pause interval in seconds, default: %s" % DEFAULT_PAUSE_DANCE, default=DEFAULT_PAUSE_DANCE, type=float)
parser.add_argument('-pp','--pause-pulse', help="Set the pulse pause interval in seconds, default: %s" % DEFAULT_PAUSE_PULSE, default=DEFAULT_PAUSE_PULSE, type=float)
parser.add_argument('-ps','--pause-scroll', help="Set the scroll pause interval in seconds, default: %s" % DEFAULT_PAUSE_SCROLL, default=DEFAULT_PAUSE_SCROLL, type=float)
parser.add_argument('-po','--pause-show', help="Set the show pause interval in seconds, default: %s" % DEFAULT_PAUSE_SHOW, default=DEFAULT_PAUSE_SHOW, type=float)
parser.add_argument('-pts','--pause-text-scroll', help="Set the text scroll pause interval in seconds, default: %s" % DEFAULT_PAUSE_TEXT_SCROLL, default=DEFAULT_PAUSE_TEXT_SCROLL, type=float)
parser.add_argument('-u','--user-name', help="Set the Twitter user name to fetch the tweets, default: %s" % DEFAULT_USER_NAME, default=DEFAULT_USER_NAME, type=str)
parser.add_argument('-nt','--num-tweets', help="Set the how many last tweets to be fetched, default: %s" % DEFAULT_NUM_TWEETS, default=DEFAULT_NUM_TWEETS, type=int)
parser.add_argument('-m','--message', help="Display a message, default: %s" % DEFAULT_MESSAGE, default=DEFAULT_MESSAGE, type=str)
parser.add_argument('-f','--function', help="Set the function to run ('logo-show', 'logo-pulse', 'logo-scroll-in', 'logo-scroll-out', 'logo-scroll', 'logo-scroll-pulse', \
'logo-scroll-right-left-in','logo-scroll-right-left-out', 'logo-scroll-right-left', 'logo-scroll-right-left-pulse', 'logo-show-inverted', 'logo-pulse-inverted', 'logo-scroll-in-inverted', \
'logo-scroll-out-inverted', 'logo-scroll-inverted', 'logo-scroll-pulse-inverted', 'logo-scroll-right-left-in-inverted', 'logo-scroll-right-left-out-inverted', \
'logo-scroll-right-left-inverted','logo-scroll-right-left-pulse-inverted', 'message-write', 'fetch', 'fetch-with-logo', 'clear')\
, default: %s" % DEFAULT_FUNCTION_NAME, default=DEFAULT_FUNCTION_NAME, type=str)

args = parser.parse_args()

# RUN SCRIPT
__main__(args)
