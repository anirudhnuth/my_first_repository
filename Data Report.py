# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:04:14 2017

@author: Anirudh
"""

from IPython.display import display, Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats


index = ['']
columns = ["2007","2008","2009","2010","2011","2012","2013",'2014','2015','2016']
demand = pd.DataFrame(index=index, columns=columns)
supply = pd.DataFrame(index = index, columns = columns)

s1 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Mine_Supply.csv')

s2 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Supply_Scrap.csv')

s3 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Producer_Hedge.csv')

d1 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Jewelry_Demand.csv')

d2 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Technology_Demand.csv')

d3 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Bar_Demand.csv')

d4 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Coin_Demand.csv')

d5 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Reserve_Changes.csv')

d6 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\ETF_Holdings.csv')

d7 = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Demand_Medallion.csv')

price = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Prices.csv')

gdp = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\World_GDP.csv')

stock = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\S&P_Prices.csv')

usd = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Currency_USD.csv')

inflation = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Inflation.csv')

ir = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Interest_Rates.csv')

volatility = pd.read_csv('C:\Data_Bootcamp\Bootcamp_CSV_files\Volatility.csv')
#accessing data sheets.Calling all the sources of information that I need for 
#my analysis. Most of my data came from a Thomson Reuters Gold Survey document 
#with embedded tables, therefore it was not possible to use tabula. Therefore, 
#I was forced to create my own excel documents. The rest of the documents come 
#from other sources in excel or csv format, which I will include the links for 
#in my data report.
