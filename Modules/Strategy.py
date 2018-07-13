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
Strategy Class
==================================================================================================='''

class Strategy():
	'''==============================================================================================
	Members:
	params_1
	params_2
	params_3


	Methods:
	run_simulation 		-- run the simulation
	run_realtime		-- run the realtime
	cost_function 		-- cost function
	compute_cost_fucntion 	-- compute the cost function
	trades 			--
	=============================================================================================='''
	def __init__(self):
		self._params_1 = 0.0;
		self._params_2 = 0.0;
		self._params_3 = 0.0;

	def run_simulation(self):
		pass

	def run_realtime(self):
		pass

	def cost_function(self):
		pass

	def compute_cost_function(self):
		pass

	def trades(self):
		pass #map
