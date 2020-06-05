from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import pandas as pd

key='WWOYKJ31LZOV8QZF'

df = pd.read_csv('data/securities.csv')

ts = TimeSeries(key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
print(data)