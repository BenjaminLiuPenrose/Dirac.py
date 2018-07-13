'''
Name: Beier (Benjamin) Liu
Date: 6/30/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib
Using cmd line py -3.6 -m pip install [package_name]
'''
import os, time, logging, sys
import copy, math
import functools, itertools
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
'''===================================================================================================
File content:
Bin Class
==================================================================================================='''

class Bin():
	'''==============================================================================================
	Members:
	open_time 	-- datetime object, open time of the bin
	close_time 	-- datetime object, close time of the bin
	open_bid 	-- double, open bid of the bin
	high_bid 	-- double, highest bid of the bin
	low_bid 	-- double, lowest bid of the bin
	close_bid 	-- double, close bid of the bin
	open_ask 	-- double, open ask of the bin
	high_ask 	-- double, high ask of the bin
	low_ask 	-- double, low ask of the bin
	close_ask 	-- double, close ask of the bin
	volume 	-- double, volume of the bin
	pnl 	-- double, pnl of the bin
	length 	-- deltatime/string, length of the bin


	Methods:
	=============================================================================================='''
	def __init__(self):
		self._open_time = 0;
		self._close_time = 0;

		self._open_bid = 0.0;
		self._high_bid = 0.0;
		self._low_bid = 0.0;
		self._close_bid = 0.0;

		self._open_ask = 0.0;
		self._high_ask = 0.0;
		self._low_ask = 0.0;
		self._close_ask = 0.0;

		self._volume = 0.0;

		self._pnl = 0.0;

		self._length = 0;

	@property
	def open_time(self):
		return self._open_time

	@open_time.setter
	def open_time(self, value):
		self._open_time = value

	@property
	def close_time(self):
		return self._close_time

	@close_time.setter
	def close_time(self, value):
		self._close_time = value

	@property
	def open_bid(self):
		return self._open_bid

	@open_bid.setter
	def open_bid(self, value):
		self._open_bid = value

	@property
	def close_bid(self):
		return self._close_bid

	@close_bid.setter
	def close_bid(self, value):
		self._close_bid = value

	@property
	def high_bid(self):
		return self._high_bid

	@high_bid.setter
	def high_bid(self, value):
		self._high_bid = value

	@property
	def low_bid(self):
		return self._low_bid

	@low_bid.setter
	def low_bid(self, value):
		self._low_bid = value

	@property
	def open_ask(self):
		return self._open_ask

	@open_ask.setter
	def open_ask(self, value):
		self._open_ask = value

	@property
	def close_ask(self):
		return self._close_ask

	@close_ask.setter
	def close_ask(self, value):
		self._close_ask = value

	@property
	def high_ask(self):
		return self._high_ask

	@high_ask.setter
	def high_ask(self, value):
		self._high_ask = value

	@property
	def low_ask(self):
		return self._low_ask

	@low_ask.setter
	def low_ask(self, value):
		self._low_ask = value

	@property
	def volume(self):
		return self._volume

	@volume.setter
	def volume(self, value):
		self._volume = value

	@property
	def pnl(self):
		return self._pnl

	@pnl.setter
	def pnl(self, value):
		self._pnl = value

	@property
	def length(self):
		return self._length

	@length.setter
	def length(self, value):
		self._length = value











