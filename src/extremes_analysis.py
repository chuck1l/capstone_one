import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 16})
import scipy.stats as stats
import pandas as pd  
import numpy as np
from datetime import datetime 

class ThreeDayEvents(object):

    def __init__(self, name, data):
        self.name = name
        self.df = pd.read_csv(data)

    def create_new_cols(self):
        self.df.rename(columns={'%_change': 'ov_ni_%_change'}, inplace=True)
        open_p = self.df['open']
        close_p = self.df['close']
        hofd = self.df['high']
        self.df['day_o_c_delta%'] = (close_p - open_p) / open_p
        self.df['hofd_o_delta%'] = (hofd - open_p) / open_p


    def remove_extra_cols(self):
        drop_cols = ['open', 'high', 'low', 'close', '200_ma', '100_ma', 
            '20_ema', 'volume_ma', 'atr', 'prev_close', '$_change', 'volume']
        self.df.drop(drop_cols, axis=1, inplace=True)

    def shift_rows_add_cols(self):
        # Add yesterday's information on same row
        self.df['y_rsi'] = self.df['rsi'].shift(periods=-1)
        self.df['y_rel_vol'] = self.df['relative_vol'].shift(periods=-1)
        self.df['y_o_c_delta%'] = self.df['day_o_c_delta%'].shift(periods=-1)
        self.df['y_hofd_o_delta%'] = self.df['hofd_o_delta%'].shift(periods=-1)

        # Add tomorrow's information on same row
        self.df['tm_rsi'] = self.df['rsi'].shift(periods=1)
        self.df['tm_rel_vol'] = self.df['relative_vol'].shift(periods=1)
        self.df['tm_o_c_delta%'] = self.df['day_o_c_delta%'].shift(periods=1)
        self.df['tm_hofd_o_delta%'] = self.df['hofd_o_delta%'].shift(periods=1)


if __name__ == "__main__":

    data = '../data/prev_data/spxl_clean.csv'
    spxl = ThreeDayEvents('spxl', data)
    spxl.create_new_cols()
    spxl.remove_extra_cols()
    spxl.shift_rows_add_cols()
    
    spxl_high = 3.64
    spxl_low = -3.43

    spxl_mask_pos = spxl.df['ov_ni_%_change'] >= spxl_high
    spxl_mask_neg = spxl.df['ov_ni_%_change'] <= spxl_low
    
    df_events_pos = spxl.df[spxl_mask_pos]
    df_events_neg = spxl.df[spxl_mask_neg]

    location = r'../data/df_gt_3.64.csv'
    df_events_pos.to_csv(location)

    location = r'../data/df_lt_n3.43.csv'
    df_events_neg.to_csv(location)

    
    
