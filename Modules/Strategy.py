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

from Modules.Trade import *
from Modules.Tools import *
'''==================================================================================================-=
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
	def __init__(self, datarepos, strats):
		#### 18, 12, 0.013, 0.019, 0.12, 0.32,
		self._params = {};
		self._instrument = strats['instrument'];
		self._cashs = [strats['cash']]*18;
		self._direction = strats.get("direction", "Long");
		self._commission_rate = strats.get("commission rate", 0.0);
		self._datarepo = datarepos[self._instrument];

	@Timer
	def run_simulation(self, strats={}):
		# Preparation Phrase
		res = {}
		instrument = self._instrument;
		direction = self._direction;
		datetimes = [];
		trades = [];
		trades_live = [];
		profits = [];
		cashs = self._cashs;
		cum_profit_final = 0;
		sharpe = 0;
		high_48 = float("-inf")
		low_48 = float("inf")
		high_72 = float("-inf")
		low_72 = float("inf")
		R = high_48-low_48;
		R2 = high_72-low_72;

		# Handling Phrase
		cnt=18;
		for _ in range(1):
			for bin in self._datarepo.bins_H4[18:]:
				high_48 = max(i.high_price for i in self._datarepo.bins_H4[cnt-12: cnt])
				low_48 = min(i.low_price for i in self._datarepo.bins_H4[cnt-12: cnt])
				high_72 = max(i.high_price for i in self._datarepo.bins_H4[cnt-18: cnt])
				low_72 = min(i.low_price for i in self._datarepo.bins_H4[cnt-18: cnt])
				R = high_48-low_48;
				R2 = high_72-low_72;
				cash = cashs[cnt-1]
				logging.debug('0.013<=R2<=0.019 is {}, low_price<open_price-R*0.12 is {}'.format((R2>=0.013 and R2<=0.019), bin.low_price<bin.open_price-R*0.12))
				cnt += 1

				if (R2>=0.013 and R2<=0.019 and bin.low_price<bin.open_price-R*0.12 and cash>0):
					offer_price = bin.open_price-R*0.12
					order = {
						"uuid": bin.close_time.strftime("%Y%m%d%H%M%S"),
						"instrument": instrument,
						"entry price": offer_price,
						"entry time": bin.close_time,
						"quantity": 100,
						"commission rate": 0.0,
						"direction": direction,
						# "stop loss price": offer_price-50*0.0001,
						"stop loss price": offer_price-50*0.000,
						"profit target price": offer_price+R*0.32
					}
					trade = Trade();
					trade.open(order);
					trades_live.append(trade)
					cash = cash - trade.init_cost
					logging.info('make a entry trade')
				for my_trade in trades_live:
					if my_trade.direction != "Neutural":
						if (bin.low_price<my_trade.stop_loss_price or bin.high_price>my_trade.profit_target_price):
							order = {
								"exit price": bin.close_ask,
								"exit time": bin.close_time
							};
							my_trade.close(order);
							profits.append(my_trade.profit)
							trades.append(my_trade)
							cash = cash + my_trade.profit
							logging.info('make a exit trade')
							logging.info("profit is {}".format(my_trade.profit))
				cashs.append(cash)

		# Checking Phrase
		logging.info('The profits are {}'.format([round(i, 6) for i in profits]))
		res['instrument']=instrument;
		res['trades']=trades;
		res['datetimes']=datetimes;
		res['cashs ts']=np.array(cashs);
		res["profits ts"] = np.array(profits);
		res["cum profits ts"] = np.cumsum(res.get("profits ts", [0, 1]));
		res["cum profit final"] = round(res.get("cum profits ts", [0, 1])[-1], 4);
		res["sharpe"]= res.get("profits ts", [0, 1]).mean()/res.get("profits ts", [0, 1]).var();
		return res

	def run_realtime(self):
		pass

	def cost_function(self):
		pass

	def compute_cost_function(self):
		pass

	def compute_perf_metrics(self):
		pass

	def trades(self):
		pass #map

	def to_string(self):
		logging.debug('\nThe Strategy is ')
