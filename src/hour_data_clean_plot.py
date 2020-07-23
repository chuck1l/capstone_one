import numpy as np  
import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 16})
import scipy.stats as stats
plt.style.use('ggplot')

class HourDataCleaning:
    def __init__(self, name, data):
        self.name = name
        self.df = pd.read_csv(data)

    # Removing the multiple columns pulled in with all-null values
    def remove_na_cols(self):
        self.df.drop(columns=['MA', '52 Week High', '52 Week Low', 'Plot', 
                'Plot.1', 'Plot.2', 'Plot.3', 'Plot.4', 'Plot.5', 'Plot.6', 
                'Plot.7', 'EMA Divergence', '-Min', '-Max',
                'Min', 'Max'], inplace=True)
       

    # Cleaning the columns by removing the blank space, and lowercasing
    # Changing column names to be more clear representation
    def rename_columns(self):
        self.df.columns = self.df.columns.str.replace(' ', '_')
        self.df.columns = map(str.lower, self.df.columns)

        self.df.rename(columns={'time': 'date'}, inplace=True)

    # Changing the date column from unix time base to datetime
    def date_format(self):
        self.df['date'] = pd.to_datetime(self.df['date'], unit = 's')

    def new_date_col(self):
        self.df['date2'] = self.df['date'].astype(str).str.slice(0, 10)
        self.df['time_of_day'] = self.df['date'].astype(str).str.slice(11, 13)
        self.df['time_of_day'] = self.df['time_of_day'].astype(float)   
        self.df['time_of_day'] = self.df['time_of_day'].sub(4.5)


    # Saving my new dataframe to the data directory
    def write_to_csv(self, location):
        self.df.to_csv(location)

class HistogramHourData(object):
    def __init__(self, name, data):
        self.name = name
        self.df = data

    def plot_data(self, title, col):
        minimum = min(self.df[col])
        maximum = max(self.df[col])
        mu = np.mean(self.df[col])
        std = np.std(self.df[col])

        fig, ax = plt.subplots(figsize=(12, 5))
        ax.hist(self.df[col], bins=7, density=True, color='red', alpha=0.70,
                label=f'Times, Low of Day')
        ax.set_title(title)
        ax.set_xlim(minimum, maximum)
        ax.set_xlabel('Time of Day')
        ax.set_ylabel('Density')


        ax.legend(loc='best')
        plt.tight_layout()
        plt.savefig(f'../img/{self.name}.png')
        plt.show()



if __name__ == "__main__":

    day_of_events = pd.read_csv('../data/spxl_eventdays_1h.csv')
    events_scat_matr.scatter_matrices()

    mask_event_max = day_of_events.groupby(['date2'])['high'].idxmax()
    mask_event_min = day_of_events.groupby(['date2'])['low'].idxmin()

    day_of_events_max = day_of_events.loc[mask_event_max]
    day_of_events_min = day_of_events.loc[mask_event_min]

    all_days = pd.read_csv('../data/spxl_alldays_1h.csv')
    mask_all_max = all_days.groupby(['date2'])['high'].idxmax()
    mask_all_min = all_days.groupby(['date2'])['low'].idxmin()

    all_days_max = all_days.loc[mask_all_max]
    all_days_min = all_days.loc[mask_all_min]

    graph_events_min = HistogramHourData('graph_events_min_time', day_of_events_min)
    title = 'Time That Low of Day Occurs, During Event'
    col = 'time_of_day'

    graph_events_min.plot_data(title, col)

    data = pd.read_csv('../data/df_gt_3.64.csv')
    spxl_data_1h = HourDataCleaning('spxl_1h', '../data/spxl_1h_raw.csv')

    date_lst = []
    for row in data['date']:
        date_lst.append(row[:10])

    spxl_data_1h.remove_na_cols()
    spxl_data_1h.rename_columns()
    spxl_data_1h.date_format()
    spxl_data_1h.new_date_col()
    spxl_data_1h.df = spxl_data_1h.df[19:]

    mask = spxl_data_1h.df['date2'].isin(date_lst)

    spxl_eventdays_1h = spxl_data_1h.df[mask]
    #print(spxl_eventdays_1h.info())

    location = r'../data/spxl_eventdays_1h.csv'
    spxl_eventdays_1h.to_csv(location)