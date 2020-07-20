import numpy as np  
import pandas as pd 
from datetime import datetime  


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


if __name__ == "__main__":
    spy = SecurityCleaning('SPY', '../data/spy_1d_data.csv')
    spy.remove_na_cols()
    spy.rename_columns()
    spy.date_format()
    print(spy.name)
    print(spy.df.head())

    location = r'../data/joined_data.csv'
    spy.write_to_csv(location)