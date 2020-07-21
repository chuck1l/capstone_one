import numpy as np  
import pandas as pd 
from datetime import datetime 

class SecurityCleaning:
    def __init__(self, name, data):
        self.name = name
        self.df = pd.read_csv(data)

    # Removing the multiple columns pulled in with all-null values
    def remove_na_cols(self):
        self.df.dropna(axis='columns', inplace=True)
       

    # Cleaning the columns by removing the blank space, and lowercasing
    # Changing column names to be more clear representation
    def rename_columns(self):
        self.df.columns = self.df.columns.str.replace(' ', '_')
        self.df.columns = map(str.lower, self.df.columns)

        self.df.rename(columns={'time': 'date', 'ma.1': '200_ma', 
            'ma.3': '100_ma', 'ma.2': '20_ema', 'plot': 'relative_vol'}, inplace=True)

    # Changing the date column from unix time base to datetime
    def date_format(self):
        self.df['date'] = pd.to_datetime(self.df['date'], unit = 's')

    # Saving my new dataframe to the data directory
    def write_to_csv(self, location):
        self.df.to_csv(location)

    # Creating two columns for further analysis
    def create_delta_column(self):
        self.df['prev_close'] = self.df['close'].shift(periods=1)
        self.df['prev_close'].fillna(self.df['close'], inplace=True)

        self.df['$_change'] = self.df['open'] - self.df['prev_close']
        self.df['%_change'] = self.df['$_change']/self.df['prev_close'] * 100

    

if __name__ == "__main__":
    # spy = SecurityCleaning('SPY', '../data/spy_1d_data.csv')
    # spy.remove_na_cols()
    # spy.rename_columns()
    # spy.date_format()
    
    # spy.create_delta_column()
   
    # location = r'../data/joined_data.csv'
    # spy.write_to_csv(location)

    # spxl = SecurityCleaning('spxl', '../data/spxl_raw.csv')
    # spxl.rename_columns()
    # spxl.df = spxl.df[199:]
    # spxl.remove_na_cols()
    # spxl.date_format()
    # spxl.create_delta_column()
    
    # location = r'../data/spxl_clean.csv'
    # spxl.write_to_csv(location)