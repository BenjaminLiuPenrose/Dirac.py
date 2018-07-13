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
		self._params = [];
		self._indicators = [];

	def add_indicators(self, params, indicators):
		self._params.append(params);
		self._indicators.append(indicators);
