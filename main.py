# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date:

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, pandas, scipy, datetime, matplotlib, pyqt5
Using cmd line py -3.6 -m pip install [package_name]
these words are used interchangeablle:
(variance, vol)
(assets, assets pool, tickers)
'''
import os, time, logging, sys
import copy, math
import functools, itertools
import numpy
import datetime
import pandas
import matplotlib.pyplot
import scipy.optimize
import Modules.config as config
from Modules.Dirac_model import *
CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH

if not os.path.exists(CURRENT_PATH+'/log/'):
	os.makedirs(CURRENT_PATH+'/log/')
if not os.path.exists(CURRENT_PATH+'/plt/'):
	os.makedirs(CURRENT_PATH+'/plt/')
if not os.path.exists(CURRENT_PATH+'/database/'):
	os.makedirs(CURRENT_PATH+'/database/')
# if not os.path.exists(CURRENT_PATH+'/backtest/'+CURRENT_TIME):
# 	os.makedirs(CURRENT_PATH+'/backtest/'+CURRENT_TIME)

logger = logging.getLogger();
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr = logging.FileHandler(CURRENT_PATH+'/log/{}.log'.format(CURRENT_TIME));
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)

console=logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)
logger.setLevel(logging.INFO)

'''===================================================================================================
File content:
main program
==================================================================================================='''

def main():
	'''==============================================================================================
	Arguments:

	Returns:

	=============================================================================================='''
	Dirac_model();
	# Preparation Phrase
	# Handling Phrase
	# Checking Phrase

if __name__=='__main__':
	main()
