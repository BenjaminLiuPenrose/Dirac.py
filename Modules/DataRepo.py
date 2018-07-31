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
DataRepo Class
==================================================================================================='''
class Singleton(type):  # type
	_instances = {}
	def __call__(cls, *args, **kargs):
		if cls not in cls._instances:
			cls._instances[cls]=super(Singleton, cls).__call__(*args, **kargs)
		return cls._instances[cls]


class DataRepo(metaclass=Singleton):
	'''==============================================================================================
	Members:
	bins_D1 	-- list of bin objects, bin.length == D1
	bins_H4 	-- list of bin objects, bin.length == H4
	bins_M1 	-- list of bin objects, bin.length == M1


	Methods:
	=============================================================================================='''
	def __init__(self):
		self._instrument = "";
		self._bins_D1 = [];
		self._bins_H4 = [];
		self._bins_m1 = [];

	@property
	def bins_D1(self):
		return self._bins_D1

	@property
	def bins_H4(self):
		return self._bins_H4

	@property
	def bins_m1(self):
		return self._bins_m1

	@property
	def instrument(self):
		return self._instrument

	@instrument.setter
	def instrument(self, value):
		self._instrument = value

	def add_bins_D1(self, value):
		self._bins_D1.append(value)

	def add_bins_H4(self, value):
		self._bins_H4.append(value)

	def add_bins_m1(self, value):
		self._bins_m1.append(value)

	def to_string(self):
		logging.debug('\nThe datarepo is: \nbins_D1: {}\nbins_H4: {}\nbins_m1: {}'.format(self.bins_D1[:5], self.bins_H4[:5], self.bins_m1[:5]));
