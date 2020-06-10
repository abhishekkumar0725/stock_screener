from alpha_vantage.sectorperformance import SectorPerformances
import pandas as pd

key='WWOYKJ31LZOV8QZF'

def getSectorData():
    sp = SectorPerformances(key, output_format='pandas')
    data, _ =  sp.get_sector()
    data = data.sort_values(by=[data.columns[0]])
    return data

def findBestSector(numSectors=3, metric=0):
    data = getSectorData()
    data = data.sort_values(by=[data.columns[metric]]).iloc[:numSectors]
    return data, list(data.index.values)

def getTickers(sector=''):
    df = pd.read_csv('data/bySector.csv')
    df = df.where(df['Sector']==sector).dropna()
    return list(df['Ticker'])

def getCompanies(sector=''):
    df = pd.read_csv('data/bySector.csv')
    df = df.where(df['Sector']==sector).dropna()
    return list(df['Companies'])