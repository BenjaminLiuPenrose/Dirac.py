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
import csv
import pandas as pd

from Modules.Bin import *
from Modules.DataRepo import *
from Modules.Tools import *
import Modules.config as config

CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH
INSTRUMENTS = config.INSTRUMENTS
BINS_FREQ = config.BINS_FREQ
'''===================================================================================================
File content:

==================================================================================================='''
@Timer
def database_to_datarepo(instrument, start, end):
	'''===================================================================================================

	==================================================================================================='''
	# Preparation Phrase
	ins = instrument
	datarepo = DataRepo();
	datarepo.instrument = ins;

	# Handling Phrase
	for freq in BINS_FREQ:
		with open('{0}/database/{1}/{2}/{3}_{4}.csv'.format(CURRENT_PATH, ins.replace('/', ''), freq, start.strftime('%Y%m%d'), end.strftime('%Y%m%d')), 'r') as file:
			reader = csv.reader(file, delimiter=',');
			first_line_bool = True
			for row in reader:
				if first_line_bool == True:
					first_line_bool = False;
					continue;
				bin = Bin();
				bin.open_time, bin.close_time, bin.open_bid, bin.close_bid, bin.high_bid, bin.low_bid, bin.open_ask, bin.close_ask, bin.high_ask, bin.low_ask, bin.volume = row;
				bin.calc();
				if freq == 'm1':
					datarepo.add_bins_m1(bin);
				elif freq == 'H4':
					datarepo.add_bins_H4(bin);
				elif freq == 'D1':
					datarepo.add_bins_D1(bin);
				else :
					pass
	logging.debug(datarepo.to_string())

	# Checking Phrase
	return datarepo
