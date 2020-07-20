import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 16})
import scipy.stats as stats
import pandas as pd  
import numpy as np

class HistogramPlot:
    def __init__(self, name, data):
        self.name = name
        self.df = data

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

            time_025 = percent_change_model.ppf(0.025)
            time_975 = percent_change_model.ppf(0.975)
            ax.axvline(time_025, color='red', linestyle='--', linewidth=1,
                label=f'Lower 2.5%: {round(time_025, 2)}%')
            ax.axvline(time_975, color='red', linestyle='--', linewidth=1,
                label=f'Upper 2.5%: {round(time_975, 2)}%')
            

        ax.legend(loc='best')
        plt.tight_layout()
        plt.savefig(f'../img/{self.name}')
        
        


if __name__ == '__main__':

    initial = pd.read_csv('../data/joined_data.csv')
    initial_graph = HistogramPlot('full_data', initial)
    initial_graph.plot_data('%_change', 'Distribution for The Daily Percent of Change, All Samples', 1)
    
    high = 1.31
    low = -1.38

    m_pos = initial['%_change'] >= high
    m_neg = initial['%_change'] <= low 
    
    df_pos = initial[m_pos]
    two_plus = HistogramPlot('great_than_975', df_pos)
    two_plus.plot_data('%_change', 'Distribution for The Percent of Change, Greater Than 2%', 0)
    
    df_neg = initial[m_neg]
    less_two = HistogramPlot('less_than_025', df_neg)
    less_two.plot_data('%_change', 'Distribution for The Percent of Change, Less Than -2%', 0)
    

    