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
        self.df['lofd_o_delta%'] = ((lofd - open_p) / open_p) * 100
        self.df['hofd_lofd_delta%'] = ((hofd - lofd) / lofd) * 100 


    def remove_extra_cols(self):
        drop_cols = ['open', 'high', 'low', 'close', '200_ma', '100_ma', 
            '20_ema', 'volume_ma', 'atr', 'prev_close', '$_change', 'volume']
        self.df.drop(drop_cols, axis=1, inplace=True)

class HistogramMiddleNinety():
    def __init__(self, name, data):
        self.name = name
        self.df = data

    # Plotting the data to identify the upper and lower 5% of the data
    # What I'm considering the extremes
    # Including a toggle switch to plot the two %5 extremes without pdf
    def plot_data(self, title, col):
        minimum = min(self.df[col])
        maximum = max(self.df[col])
        mu = np.mean(self.df[col])
        std = np.std(self.df[col])

        fig, ax = plt.subplots(figsize=(12, 5))
        ax.hist(self.df[col], bins=50, density=True, color='green', alpha=0.5,
                label=f'% of Price Change')
        ax.set_title(title)
        ax.set_xlim(minimum, maximum)
        ax.set_xlabel('% Delta High of Day vs. Low of Day')
        ax.set_ylabel('Density')

        
        percent_change_model = stats.norm(mu, std)

        # t = np.linspace(minimum, maximum, num=200)
        # ax.plot(t, percent_change_model.pdf(t), linewidth=2, color='black',
        #         label='Normal PDF')

        time_05 = percent_change_model.ppf(0.05)
        time_95 = percent_change_model.ppf(0.95)
        # ax.axvline(time_05, color='red', linestyle='--', linewidth=1,
        #     label=f'Lower 5%: {round(time_05, 2)}%')
        ax.axvline(time_95, color='red', linestyle='--', linewidth=1,
            label=f'Upper 5%: {round(time_95, 2)}%')
        ax.axvline(mu, color='black', linestyle='--', linewidth=1,
            label=f'Mean: {round(mu, 2)}%')
            

        ax.legend(loc='upper right')
        plt.tight_layout()
        plt.savefig(f'../img/{self.name}.png')
        #dplt.show()


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

    graph_pos_45 = HistogramMiddleNinety('graph_pos_45_hofd_lofd', data_reduced_pos_45)

    title = 'Comparing Price Change High of Day vs. Low of Day For Non-Catalyst Days'
    col_pos = 'hofd_lofd_delta%'

    graph_pos_45.plot_data(title, col_pos)




    

    