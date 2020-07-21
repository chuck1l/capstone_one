import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 16})
import scipy.stats as stats
import pandas as pd  
import numpy as np

class HistogramPlot:
    def __init__(self, name, data):
        self.name = name
        self.df = data

    # Plotting the data to identify the upper and lower 5% of the data
    # What I'm considering the extremes
    # Including a toggle switch to plot the two %5 extremes without pdf
    def plot_data(self, col, title, toggle=1):
        minimum = min(self.df[col])
        maximum = max(self.df[col])
        mu = np.mean(self.df[col])
        std = np.std(self.df[col])

        if toggle == 1:
            binsize = 75
            dens=True
            y_lab = 'Density'
            size = 5
           
        else:
            binsize = 25
            dens =False
            y_lab = 'Frequency'
            size = 2.5


        fig, ax = plt.subplots(figsize=(12, size))
        ax.hist(self.df[col], bins=binsize, density=dens, color='green', alpha=0.5,
                label=f'Histogram of Percent Change')
        ax.set_title(title)
        ax.set_xlim(minimum, maximum)
        ax.set_xlabel('Percent Change From Previous Day')
        ax.set_ylabel(y_lab)

        if toggle == 1:
            percent_change_model = stats.norm(mu, std)

            t = np.linspace(minimum, maximum, num=200)
            ax.plot(t, percent_change_model.pdf(t), linewidth=2, color='black',
                    label='Normal PDF with sample mean and std')

            time_05 = percent_change_model.ppf(0.05)
            time_95 = percent_change_model.ppf(0.95)
            ax.axvline(time_05, color='red', linestyle='--', linewidth=1,
                label=f'Lower 5%: {round(time_05, 2)}%')
            ax.axvline(time_95, color='red', linestyle='--', linewidth=1,
                label=f'Upper 5%: {round(time_95, 2)}%')
            

        ax.legend(loc='best')
        plt.tight_layout()
        #plt.savefig(f'../img/{self.name}.png')
        #plt.show()

        
        


if __name__ == '__main__':

    # initial = pd.read_csv('../data/joined_data.csv')
    # initial_graph = HistogramPlot('full_data', initial)
    # initial_graph.plot_data('%_change', 'Distribution for The Daily Percent of Change, All Samples', 1)
    
    # high = 1.31
    # low = -1.38

    # m_pos = initial['%_change'] >= high
    # m_neg = initial['%_change'] <= low 
    
    # df_pos = initial[m_pos]
    # two_plus = HistogramPlot('great_than_975', df_pos)
    # two_plus.plot_data('%_change', 'Distribution for The Percent of Change, Greater Than 2%', 0)
    
    # df_neg = initial[m_neg]
    # less_two = HistogramPlot('less_than_025', df_neg)
    # less_two.plot_data('%_change', 'Distribution for The Percent of Change, Less Than -2%', 0)
    

    # spxl = pd.read_csv('../data/spxl_clean.csv')
    # spxl_initial = HistogramPlot('full_spxl', spxl)
    # spxl_initial.plot_data('%_change', "SPXL Distribution Daily Percent of Change, All Samples", 1)

    # spxl_high = 3.64
    # spxl_low = -3.43

    # mask_pos = spxl['%_change'] >= spxl_high
    # mask_neg = spxl['%_change'] <= spxl_low

    # spxl_pos = spxl[mask_pos]
    # spxl_neg = spxl[mask_neg]
    # spxl_g95 = HistogramPlot('spxl_gt_3.64%', spxl_pos)
    # spxl_g95.plot_data('%_change', 'Distribution For The Percent of Change, Greater Than 3.64%', 0)

    # spxl_l05 = HistogramPlot('spxl_lt_n3.43%', spxl_neg)
    # spxl_l05.plot_data('%_change', 'Distribution For The Percent of Change, Less Than -3.43%', 0)

    