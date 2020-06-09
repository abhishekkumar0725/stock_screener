from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import pandas as pd
#from talib import *

key='WWOYKJ31LZOV8QZF'
securities = pd.read_csv('data/securities.csv')

def getSectorData():
    sp = SectorPerformances(key, output_format='pandas')
    data, _ =  sp.get_sector()
    data = data.sort_values(by=[data.columns[0]])
    return data

def findBestSector(numSectors=3, metric=0):
    data = getSectorData()
    data = data.sort_values(by=[data.columns[metric]])
    return data.iloc[:numSectors]