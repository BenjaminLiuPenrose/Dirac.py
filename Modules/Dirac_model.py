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
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

import Modules.config as config
from Modules.rawtick_to_database import *
from Modules.database_to_datarepo import *

CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH
BINS_FREQ = config.BINS_FREQ
INSTRUMENTS = config.INSTRUMENTS
'''===================================================================================================
File content:
Strategy Class
==================================================================================================='''

def Dirac_model():
	'''==============================================================================================


	=============================================================================================='''
	# Preparation Phrase
	start = dt.datetime(2018, 1, 1);
	end = dt.datetime(2018, 1, 20);
	datarepos = {};
	incre = dt.timedelta(9);
	e = start-de.timedelta(1);
	for x in range(math.ceil((end-start).days/10)):
		s = e+dt.timedelta(1);
		e = s+incre;
		if (end-e).days<0:
			e = end;
		rawtick_to_database(s, e);

	# Handling Phrase
	e = start-de.timedelta(1);
	for x in range(math.ceil((end-start).days/10)):
		s = e+dt.timedelta(1);
		e = s+incre;
		if (end-e).days<0:
			e = end;
		for ins in INSTRUMENTS:
			datarepos[ins] = database_to_datarepo(ins, s, e);

	# strategy = Strategy();

	# Checking Phrase
