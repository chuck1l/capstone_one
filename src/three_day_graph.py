import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 16})
import scipy.stats as stats
import pandas as pd  
import numpy as np

class ThreeGraphPlot:
    def __init__(self, name, data):
        self.name = name
        self.df = data

    def plot_data(self, col1, col2, col3, title):
        minimum1, maximum1 = min(self.df[col1]), max(self.df[col1])
        minimum2, maximum2 = min(self.df[col2]), max(self.df[col2])
        minimum3, maximum3 = min(self.df[col3]), max(self.df[col3])
        if minimum1 < minimum2 and minimum1 < minimum3:
            minimum = minimum1
        elif minimum2 < minimum1 and minimum2 < minimum3:
            minimum = minimum2
        else:
            minimum = minimum3

        if maximum1 > maximum2 and maximum1 > maximum3:
            maximum = maximum1
        elif maximum2 > maximum1 and maximum2 > maximum3:
            maximum = maximum2
        else:
            maximum = maximum3

        mu1 = np.mean(self.df[col1])
        mu2 = np.mean(self.df[col2])
        mu3 = np.mean(self.df[col3])

        fig, ax = plt.subplots(3, 1, figsize=(15, 7))

        # Plot the day before the event
        ax[1].hist(self.df[col1], bins=20, density=True, color='green', alpha=.70,
                label=f'% of Price Change Day of Event')
        ax[1].axvline(mu1, color='black', linestyle='--', linewidth=1,
                label=f'Avg: {round(mu1, 2)}%')
        ax[1].set_xlim(minimum, maximum)
        ax[1].set_ylabel('Density')
        ax[1].legend(loc='upper left')

        # Plot the day of the event
        ax[0].hist(self.df[col2], bins=20, density=True, color='green', alpha=.70,
                label=f'% of Price Change Before Event')
        ax[0].axvline(mu2, color='black', linestyle='--', linewidth=1,
                label=f'Avg: {round(mu2, 2)}%')
        ax[0].set_title(title)
        ax[0].set_xlim(minimum, maximum)
        ax[0].set_ylabel('Density')
        ax[0].legend(loc='upper left')

        # Plot the day after the event
        ax[2].hist(self.df[col3], bins=20, density=True, color='green', alpha=.70,
                label=f'% of Price Change After Event')
        ax[2].axvline(mu3, color='black', linestyle='--', linewidth=1,
                label=f'Avg: {round(mu3, 2)}%')
        ax[2].set_xlim(minimum, maximum)
        ax[2].set_xlabel('% Delta Close vs. Open')
        ax[2].set_ylabel('Density')
        ax[2].legend(loc='upper left')

        
        fig.tight_layout()
        #plt.show()
        plt.savefig(f'../img/{self.name}.png')


if __name__ == "__main__":   

    data_pos = pd.read_csv('../data/df_gt_3.64.csv')
    pos_data = ThreeGraphPlot('graph_%_op_clo', data_pos)

    day_of_price = 'day_o_c_delta%'
    day_bf_price = 'y_o_c_delta%'
    day_af_price = 'tm_o_c_delta%'

    title = 'Comparing Price Change Close vs. Open For 3 days Around Event'

    pos_data.plot_data(day_of_price, day_bf_price, day_af_price, title)

    # pos_data = ThreeGraphPlot('graph_%_hi_open', data_pos)

    # day_of_price = 'hofd_o_delta%'
    # day_bf_price = 'y_hofd_o_delta%'
    # day_af_price = 'tm_hofd_o_delta%'

    # title = 'Comparing Price Change High of Day vs. Open For 3 days Around Event'
    # pos_data.plot_data(day_of_price, day_bf_price, day_af_price, title)


    



