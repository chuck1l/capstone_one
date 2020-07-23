import numpy as np  
import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 16})
import scipy.stats as stats
plt.style.use('ggplot')

class SevenDayEvents(object):

    def __init__(self, name, data):
        self.name = name
        self.df = pd.read_csv(data)

    # def create_avg_price(self):
    #     self.df['avg_price'] = self.df.apply(lambda row: (row.open + row.close   
    #             + row.high + row.low)/4, axis=1)

    def remove_extra_cols(self):
        
        self.df['date'] = pd.to_datetime(self.df['date'], format='%Y-%m-%d').dt.date
        self.df['date2'] = self.df['date'].astype(str)
        cols = ['date', 'date2', 'volume', '%_change', 'high']
        self.df = self.df[cols]
    
    

    def graph_7d_data(self, title, x_label, y1_label, y2_label):
        fig, ax1 = plt.subplots(figsize=(12, 5))
        
        ax1.set_xlabel('Dates Around Event')
        ax1.set_ylabel(y1_label, color='green')
        ax1.plot(self.df['date2'][2669:2680], self.df['high'][2669:2680], label=y1_label,
                color='green', alpha=.7)
        ax1.tick_params(axis='y', labelcolor='green')
        ax1.axvline(x=5, label='Day of Event')

        ax2 = ax1.twinx() # Instantiate a second axes that shares x-axis

        ax2.set_ylabel(y2_label, color='blue')
        ax2.plot(self.df['date2'][2669:2680], self.df['volume'][2669:2680], label=y2_label, 
                color='blue', alpha=.7)
        ax2.tick_params(axis='y', labelcolor='blue')

        ax1.set_title(title)
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')
      
        plt.tight_layout()
        plt.savefig(f'../img/ten_day_chars/graph2020-04-07.png')
        plt.show()
    
if __name__ == '__main__':
    spxl_data = '../data/prev_data/spxl_clean.csv'

    d7_events_spxl = SevenDayEvents('d7_events_spxl', spxl_data)
    mask = d7_events_spxl.df['%_change'] >= 3.64
    d7_events_spxl.remove_extra_cols()

    event_days = d7_events_spxl.df[mask]
 
    d7_events_spxl.graph_7d_data('Comparing Volume to Price 10 Days Around an Event',
             'Dates', 'Price', 'Volume')