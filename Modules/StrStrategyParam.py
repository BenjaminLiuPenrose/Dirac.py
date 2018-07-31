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
StrStrategyParam Class
==================================================================================================='''
class StrStrategyParam():
	'''===================================================================================================

	==================================================================================================='''
	def __init__(self):
		self._params_indicators = {"R2": 72, "name": "range", "low": 0.013, "high": 0.019};
		self._params_entry = {"entry": 0.12, "R": 48};
		self._params_target = {"R": 48, "name": "range", "target": 0.32};
		self._params_stop = {"stop": 50*0.0001};
		"Indicators: R2=max_{}-min_{}, \nEntry condition: open_price-R*{}, R=max_{}-min_{}, \nProfit target: offer_price+R*{}, \nStop loss: {}*0.0001".format(self._params_indicators["R2"], params_indicators["R2"], params_entry["entry"], params_entry["R"], params_entry["R"], params_target["target"], params_stop["stop"])

	@property
	def params_indicators(self):
		return self._params_indicators

	@params_indicators.setter
	def params_indicators(self, value):
		self._params_indicators = value

	@property
	def params_entry(self):
		return self._params_entry

	@_params_entry.setter
	def params_entry(self, value):
		self._params_entry = value

	@property
	def params_target(self):
		return self._params_target

	@params_target.setter
	def params_target(self, value):
		self._params_taregt = value

	@property
	def params_stop(self):
		return self._params_stop

	@params_stop.setter(self, value):
	def params_stop(self):
		self._params_stop = value


	def to_string(self):
		logging.info('\nThe StrStrategyParam: \n')
