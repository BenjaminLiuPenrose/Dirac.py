# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 6/1/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy
Using cmd line py -3.6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
import datetime

'''===================================================================================================
File content:
global variables of the whole program
==================================================================================================='''

CURRENT_PATH = os.getcwd();
CURRENT_TIME = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
FREQ_CONVERSION = {
	"daily": (1, 252),
	"weekly": (5, 50),
	"monthly": (20, 12),
	"quaterly": (60, 4),
	"semiannually": (120, 2),
	"yearly": (252, 1),
	"annually": (252, 1)
	}
BINS_FREQ =['m1', 'H4', 'D1'];
INSTRUMENTS = ['AUD/CAD', 'AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/USD', \
 'CAD/CHF', 'CAD/JPY', 'CHF/JPY', 'TRY/JPY', 'ZAR/JPY', \
 'EUR/CAD', 'EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'EUR/NOK', 'EUR/NZD', 'EUR/SEK', 'EUR/TRY', 'EUR/USD', 'EUR/AUD', \
 'GBP/AUD', 'GBP/CAD', 'GBP/CHF', 'GBP/JPY', 'GBP/NZD', 'GBP/USD', \
 'NZD/CAD', 'NZD/CHF', 'NZD/JPY', 'NZD/USD', \
 'USD/CAD', 'USD/CHF', 'USD/CNH', 'USD/HKD', 'USD/JPY', 'USD/MXN', 'USD/NOK', 'USD/SEK', 'USD/TRY', 'USD/ZAR', \
 'AUS200', 'CHN50', 'ESP35', 'EUSTX50', 'FRA40', 'GER30', 'HKG33', 'JPN225', 'NAS100', 'US30', 'SPX500',  'UK100', \
 'USDOLLAR', 'USOil', 'UKOil', 'NGAS', 'XAG/USD', 'XAU/USD', 'Copper', 'SOYF', 'Bund']



