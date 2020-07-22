import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 16})
import scipy.stats as stats
import pandas as pd  
import numpy as np
from datetime import datetime 

class MiddleNinety(object):

    def __init__(self, name, data):
        self.name = name
        self.df = pd.read_csv(data)

    def create_new_cols(self):
        self.df.rename(columns={'%_change': 'ov_ni_%_change'}, inplace=True)
        open_p = self.df['open']
        close_p = self.df['close']
        hofd = self.df['high']
        lofd = self.df.loc[:, 'low']
        self.df['day_o_c_delta%'] = ((close_p - open_p) / open_p) * 100
        self.df['hofd_o_delta%'] = ((hofd - open_p) / open_p) * 100
        self.df['hofd_lofd_delta%'] = ((hofd - lofd) / lofd) * 100 


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

class HistogramMiddleNinety():
    def __init__(self, name, data):
        self.name = name
        self.df = data

    # Plotting the data to identify the upper and lower 5% of the data
    # What I'm considering the extremes
    # Including a toggle switch to plot the two %5 extremes without pdf
    def plot_data(self, col, title):
        minimum = min(self.df[col])
        maximum = max(self.df[col])
        mu = np.mean(self.df[col])
        std = np.std(self.df[col])

        fig, ax = plt.subplots(figsize=(12, 5))
        ax.hist(self.df[col], bins=50, density=True, color='green', alpha=0.5,
                label=f'% of Price Change With No Event')
        ax.set_title(title)
        ax.set_xlim(minimum, maximum)
        ax.set_xlabel('% Delta High of Day vs. Open')
        ax.set_ylabel(y_lab)

        
        percent_change_model = stats.norm(mu, std)

        t = np.linspace(minimum, maximum, num=200)
        ax.plot(t, percent_change_model.pdf(t), linewidth=2, color='black',
                label='Normal PDF with sample mean and std')

        time_025 = percent_change_model.ppf(0.025)
        time_975 = percent_change_model.ppf(0.975)
        ax.axvline(time_025, color='red', linestyle='--', linewidth=1,
            label=f'Lower 2.5%: {round(time_025, 2)}%')
        ax.axvline(time_975, color='red', linestyle='--', linewidth=1,
            label=f'Upper 2.5%: {round(time_975, 2)}%')
        ax.axvline(mu, color='black', linestyle='--', linewidth=1,
            label=f'Mean: {round(mu, 2)}%')
            

        ax.legend(loc='best')
        plt.tight_layout()
        #plt.savefig(f'../img/{self.name}.png')
        #plt.show()


if __name__ == "__main__":
    data = '../data/prev_data/spxl_clean.csv'
    spxl_mid_90 = MiddleNinety('spxl_mid_90', data)
    spxl_mid_90.create_new_cols()
    
    m_pos = spxl_mid_90.df['ov_ni_%_change'] <= 2
    m_neg = spxl_mid_90.df['ov_ni_%_change'] >= -2
    m_zero_pos = spxl_mid_90.df['ov_ni_%_change'] >= 0 
    m_zero_neg = spxl_mid_90.df['ov_ni_%_change'] <= 0

    mask_pos = m_zero_pos & m_pos
    mask_neg = m_neg & m_zero_neg

    data_reduced_pos_45 = spxl_mid_90.df[mask_pos]
    data_reduced_neg_45 = spxl_mid_90.df[mask_neg]

    print(len(data_reduced_pos_45))
    print(len(data_reduced_neg_45))
    
    location_pos = r'../data/spxl_mid_pos_45.csv'
    data_reduced_pos_45.to_csv(location_pos)

    location_neg = r'../data/spxl_mid_neg_45.csv'
    data_reduced_neg_45.to_csv(location_neg)

    