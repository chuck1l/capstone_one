import numpy as np  
import pandas as pd 
from datetime import datetime 
import matplotlib.pyplot as plt 
import scipy.stats as stats


class SecurityCleaning:
    def __init__(self, name, data):
        self.name = name
        self.df = pd.read_csv(data)

    def remove_na_cols(self):
        self.df.dropna(axis='columns', inplace=True)

    def rename_columns(self):
        self.df.columns = self.df.columns.str.replace(' ', '_')
        self.df.columns = map(str.lower, self.df.columns)

        self.df.rename(columns={'time': 'date', 'plot.2': '200_ma', 
            'plot.3': '100_ma', 'plot.4': '20_ema'}, inplace=True)

    def date_format(self):
        self.df['date'] = pd.to_datetime(self.df['date'], unit = 's')

    # Saving my new dataframe to the data directory
    def write_to_csv(self, location):
        self.df.to_csv(location)

    def create_delta_column(self):
        self.df['prev_close'] = self.df['close'].shift(periods=1)
        self.df['prev_close'].fillna(self.df['close'], inplace=True)

        self.df['$_change'] = self.df['open'] - self.df['prev_close']
        self.df['%_change'] = self.df['$_change']/self.df['prev_close'] * 100

    

if __name__ == "__main__":
    spy = SecurityCleaning('SPY', '../data/spy_1d_data.csv')
    spy.remove_na_cols()
    spy.rename_columns()
    spy.date_format()
    
    spy.create_delta_column()

    print(spy.df.head())
   


    location = r'../data/joined_data.csv'
    spy.write_to_csv(location)