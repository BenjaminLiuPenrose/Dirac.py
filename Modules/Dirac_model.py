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
import matplotlib.backends.backend_pdf
import scipy.optimize as opt
import seaborn as sns

import Modules.config as config
from Modules.rawtick_to_database import *
from Modules.database_to_datarepo import *
from Modules.Strategy import *

CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH
BINS_FREQ = config.BINS_FREQ
INSTRUMENTS = config.INSTRUMENTS
'''===================================================================================================
File content:
Dirac model
### learn from XQW_model.py
==================================================================================================='''

def Dirac_model():
	'''==============================================================================================


	=============================================================================================='''
	# Preparation Phrase
	start = dt.datetime(2010, 1, 1);
	end = dt.datetime(2010, 4, 30);
	datarepos = {};
	incre = dt.timedelta(9);
	ins_trail = "AUD/USD"
	process_num = 1;
	bool_test_mode = True;
	# e = start-de.timedelta(1);
	# for x in range(math.ceil((end-start).days/10)):
	# 	s = e+dt.timedelta(1);
	# 	e = s+incre;
	# 	if (end-e).days<0:
	# 		e = end;
	# 	rawtick_to_database(s, e);

	# Handling Phrase
	e = start-dt.timedelta(1);
	for x in range(math.ceil((end-start).days/10)):
		s = e+dt.timedelta(1);
		e = s+incre;
		for ins in INSTRUMENTS:
			if ins != ins_trail:
				continue;
			datarepos[ins] = database_to_datarepo(ins, s, e);

	strats = {
		"instrument": ins_trail,
		"cash": 10000,
		"direction": "Long",
		"commission rate": 0.0
	};

	strats_ls = []
	for i in range(process_num):
		if bool_test_mode and i != process_num-1:
			continue
		tmp = strats.copy();
		# tmp['deltaS'] = round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4);
		strats_ls.append(tmp)

	res = []
	for i in range(process_num):
		if bool_test_mode and i!= 0:
			break
		strategy = Strategy(datarepos, strats);
		res.append( strategy.run_simulation(strats_ls[i]) )

	# strategy = Strategy(datarepos, strats);
	# res = strategy.run_simulation(strats);
	# res = strategy.run_simulation(strats);
	# res = multiProcess(process_num, Strategy(datarepos, strats).run_simulation, strats_ls)
	logging.info(res)
	logging.info(len(res))


	#size = len(datarepos[ins_trail].bins_H4)
	# Xs_dt = [datarepos[ins_trail].bins_D1[i].close_time for i in range(size)]
	#Xs_dt = [datarepos[ins_trail].bins_H4[i].close_time for i in range(size)]
	# Ys_ps = [datarepos[ins_trail].bins_D1[i].close_price for i in range(size)]
	# Ys_bids = [datarepos[ins_trail].bins_D1[i].close_bid for i in range(size)]
	# Ys_asks = [datarepos[ins_trail].bins_D1[i].close_ask for i in range(size)]
	#Ys_cash = strategy._cash
	# Ys_profits_acc = np.cumsum(strategy._profit)
	# Xs = [i for i in range(len(Ys_profits_acc))]
	# plt.plot(Xs_dt, Ys_ps, 'r-')
	# plt.plot(Xs_dt, Ys_asks, 'g-')
	# plt.plot(Xs_dt, Ys_bids, 'b-')
	# plt.plot(Xs, Ys_profits_acc)
	#plt.plot(Xs_dt, Ys_cash)
	#plt.show()
	ins = ins_trail.replace('/', '')
	Ys_profits = []; Ys_cum_profits = []; trades = [];
	cum_profit_final_ls = []; sharpe_ls = [];
	for i in range(process_num):
		if bool_test_mode and  i != 0:
			break
		Ys_profits.append( res[i]['profits ts'] );
		Ys_cum_profits.append( res[i]['cum profits ts'] );
		cum_profit_final_ls.append( res[i]['cum profit final'] );
		sharpe_ls.append( res[i]['sharpe'] );
		trades.append( res[i]['trades'] )
	# Xs_dt = res[0]['datetimes'];
	Xs_dt = [i for i in range(len(res[0]['profits ts']))]

	str_path = "{}/output/{}/{}.pdf".format(CURRENT_PATH, CURRENT_TIME, ins)
	with matplotlib.backends.backend_pdf.PdfPages(str_path) as pdf:
		# cum returns graph
		fig = plt.figure(figsize=(16, 12))
		for i in range(process_num):
			if bool_test_mode and i!= 0:
				break
			# plt.plot(Xs_dt, Ys_profits[i], label=str(strats_ls[i]['deltaS']));
			plt.plot(Xs_dt, Ys_cum_profits[i], label=str(strats_ls[i]['instrument']));
		plt.legend(loc="upper left", ncol=int(process_num/10)+1)
		plt.title("Cumulative Returns")
		plt.xlabel("Days")
		plt.ylabel("Cumulative Returns")
		pdf.savefig(fig)
		# plt.show()

		# returns graph
		fig = plt.figure(figsize=(16, 12))
		for i in range(process_num):
			if bool_test_mode and i!= 0:
				break
			plt.plot(Xs_dt, Ys_profits[i], label=str(strats_ls[i]['instrument']));
		plt.legend(loc="upper left", ncol=int(process_num/10)+1)
		plt.title("Daily PnL")
		plt.xlabel("Days")
		plt.ylabel("Daily PnL")
		pdf.savefig(fig)
		# plt.show()

		if not bool_test_mode:
			with open("{}/output/{}/{}_cumProfits.csv".format(CURRENT_PATH, CURRENT_TIME, ins), "w", newline='') as file:
				writer = csv.writer(file);
				# writer.writerow(tuple(round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4) for i in range(process_num)))
				for j in range(len(Ys_cum_profits[0])):
					writer.writerow(tuple(Ys_cum_profits[i][j] for i in range(process_num)))

		if not bool_test_mode:
			with open("{}/output/{}/{}_profits.csv".format(CURRENT_PATH, CURRENT_TIME, ins), "w", newline='') as file:
				writer = csv.writer(file);
				# writer.writerow(tuple(round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4) for i in range(process_num)))
				for j in range(len(Ys_cum_profits[0])):
					writer.writerow(tuple(Ys_profits[i][j] for i in range(process_num)))

		if not bool_test_mode:
			# training final_profits as cost function
			fig = plt.figure(figsize=(16, 12))
			# plt.plot([round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4) for i in range(process_num)], cum_profit_final_ls, 'b--')
			plt.title("Training")
			plt.xlabel("deltaS")
			plt.ylabel("Final Profits")
			pdf.savefig(fig)
			# plt.show()

			# training  sharpe as cost function
			fig = plt.figure(figsize=(16, 12))
			# plt.plot([round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4) for i in range(process_num)], sharpe_ls, 'r--')
			plt.title("Training")
			plt.xlabel("deltaS")
			plt.ylabel("Sharpe Ratio")
			pdf.savefig(fig)
			# plt.show()
			with open("{}/output/{}/{}_trainingDeltaS.csv".format(CURRENT_PATH, CURRENT_TIME, ins), "w", newline='') as file:
				writer = csv.writer(file);
				writer.writerow(('deltaS', 'cum profit final', 'sharpe'))
				for i in range(process_num):
					writer.writerow((deltaS_ls[i], cum_profit_final_ls[i], sharpe_ls[i]))


	# Checking Phrase

