import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime

# I have four data sets with all of the data that I wanted
# Bring the data in, view, and collect into one df

df1 = pd.read_csv('../data/SPY_1d_2020_2014.csv')
df2 = pd.read_csv('../data/SPY_1D_201312_200705.csv')
df3 = pd.read_csv('../data/SPY_1D_200705_200009.csv')
df4 = pd.read_csv('../data/SPY_1D_200009_199407.csv')

# renaming columns 

df1.rename(columns={'time': 'date', 'VWAP': 'vwap', '200 MA': '200_ma', 
    '100 MA': '100_ma', '20 EMA': '20_ema', 'Volume': 'volume', 
    'Volume MA': 'volume_ma', 'RSI': 'rsi'}, inplace=True)

df2.rename(columns={'time': 'date', 'VWAP': 'vwap', 'Plot.2': '200_ma', 
    'Plot.3': '100_ma', 'Plot.4': '20_ema', 'Volume': 'volume', 
    'Volume MA': 'volume_ma', 'RSI': 'rsi'}, inplace=True)

df3.rename(columns={'time': 'date', 'VWAP': 'vwap', 'Plot.2': '200_ma', 
    'Plot.3': '100_ma', 'Plot.4': '20_ema', 'Volume': 'volume', 
    'Volume MA': 'volume_ma', 'RSI': 'rsi'}, inplace=True)

df4.rename(columns={'time': 'date', 'VWAP': 'vwap', 'Plot.2': '200_ma', 
    'Plot.3': '100_ma', 'Plot.4': '20_ema', 'Volume': 'volume', 
    'Volume MA': 'volume_ma', 'RSI': 'rsi'}, inplace=True)

# converting the unix time to readable date in my df's 

df1['date'] = pd.to_datetime(df1['date'], unit = 's')
df2['date'] = pd.to_datetime(df2['date'], unit = 's')
df3['date'] = pd.to_datetime(df3['date'], unit = 's')
df4['date'] = pd.to_datetime(df4['date'], unit = 's')

# concatenate all columns from all df's into one, order by date

frames = [df4, df3, df2, df1]
df = pd.concat(frames)

df.to_csv(r'/Users/chucks_apple/Documents/galvanize/capstone/capstone_one/data/joined_data.csv')

