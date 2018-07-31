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
import csv
import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import fxcmpy
import importlib
from fxcmpy import fxcmpy_tick_data_reader as tdr

from Modules.Bin import *
from Modules.Tools import *
import Modules.config as config
CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH
BINS_FREQ = config.BINS_FREQ

if not os.path.exists(CURRENT_PATH+'/database/'):
	os.makedirs(CURRENT_PATH+'/database/')
'''===================================================================================================
File content:

==================================================================================================='''
@Timer
def rawtick_to_database(start, end):
	'''===================================================================================================

	==================================================================================================='''
	# Preparation Phrase
	con = fxcmpy.fxcmpy(config_file = 'fxcm.cfg', server='demo');
	if int((end-start).days/10) > 1:
		raise Exception('rawtick_to_database: illegal input');
	# Handling Phrase
	try :
		# instruments = tdr.get_available_symbols(); # old tick
		instruments  = con.get_instruments_for_candles();
		instruments = ['EUR/USD'];
		# start = dt.datetime(2018, 1, 1);
		# end = dt.datetime(2018, 1, 2);
		bins = {};
		for ins in instruments:
			for freq in BINS_FREQ:
				bins[freq] = [];
				if not os.path.exists(CURRENT_PATH+'/database/'+ins.replace('/', '')+'/'+freq):
					os.makedirs(CURRENT_PATH+'/database/'+ins.replace('/', '')+'/'+freq);
				df = con.get_candles(ins, period=freq, start=start, end=end); # the highest freq is m1
				(num_row, num_col) = df.shape;
				dtime = df.index;
				bidopen = df['bidopen'];
				bidclose = df['bidclose'];
				bidhigh = df['bidhigh'];
				bidlow = df['bidlow'];
				askopen = df['askopen'];
				askclose = df['askclose'];
				askhigh = df['askhigh'];
				asklow = df['asklow'];
				tickqty = df['tickqty'];
				for r in range(num_row):
					bin = Bin();
					bin.length = freq;
					if r == 0:
						if freq == 'm1':
							bin.open_time = dtime[0]-dt.timedelta(seconds=60)
						elif freq == 'H4':
							bin.open_time = dtime[0]-dt.timedelta(seconds=3600*4)
						elif freq == 'D1':
							bin.open_time = dtime[0]-dt.timedelta(days=1)
						else :
							pass
					else :
						bin.open_time = dtime[r-1];
					bin.close_time, bin.open_bid, bin.close_bid, bin.high_bid, bin.low_bid, bin.open_ask, bin.close_ask, bin.high_ask, bin.low_ask, bin.volume = dtime[r], bidopen[r], bidclose[r], bidhigh[r], bidlow[r], askopen[r], askclose[r], askhigh[r], asklow[r], tickqty[r];
					bins[freq].append(bin);

				with open('{}/{}/{}/{}/{}_{}.csv'.format(CURRENT_PATH, 'database', ins.replace('/', ''), freq, start.strftime('%Y%m%d'), end.strftime('%Y%m%d')), 'w', newline='') as file:
					writer = csv.writer(file);
					writer.writerow(('open time', 'close time', 'open bid', 'close bid', 'high bid', 'low bid', 'open ask', 'close ask', 'high ask', 'low ask', 'volume'))
					for r in range(num_row):
						bin = bins[freq][r]
						writer.writerow((bin.open_time, bin.close_time, bin.open_bid, bin.close_bid, bin.high_bid, bin.low_bid, bin.open_ask, bin.close_ask, bin.high_ask, bin.low_ask, bin.volume))
			# dr = tdr(ins, start, end, verbosity=True);
			# df = dr.get_data();
			# dt = df.index;
			# df = df.reset_index();
			# dt = df['Datetime'].values;
			# bid = df['Bid'].values;
			# ask = df['Ask'].values;
			# for freq in BINS_FREQ:
			# 	bins = [];
			# 	if not os.path.exists(CURRENT_PATH+'/database/'+ins+'/'+freq):
			# 		os.makedirs(CURRENT_PATH+'/database/'+ins+'/'+freq);
			# 	if freq == 'M1':
			# 		for r in range(num_row):
			# 			bin = Bin();
			# 			bin.length = 'M1';
			# 			bin.close_time, bin.open_bid, bin.close_bid, bin.high_bid, bin.low_bid, bin.ask_open, bin.ask_close, bin.ask_high, bin.ask_low, bin.volume = dt[r], openbid[r], closebid[r], highbid[r], lowbid[r], askopen[r], askclose[r], askhigh[r], asklow[r], tickqty[r];
			# 			bins.append(bin);
			# 	elif freq == 'H4':
			# 		rng = int((dt[-1]-dt[0]).seconds/3600/4);
			# 		for r in range(rng):
			# 			bin = Bin();
			# 			bin.length = 'H4';
			# 	elif freq == 'D1':
			# 		1
			# 	else :
			# 		pass

	except Exception as e :
		logging.error('rawtick_to_database|Error Message: {}'.format(e));
		con.close();

	# Checking Phrase
	con.close();
