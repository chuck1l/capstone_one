# <div align="center">_**Can we improve a trader's win-ratio through EDA?**_</div>
## <div align="center">_**Lawrence C. Williams - Capston Project I - July 24, 2020**_</div>

![header image](https://github.com/chuck1l/capstone_one/blob/master/img/header.png)

## _**Introduction:**_

An effective trading strategy is essential in attempting to sustain a living as a retail trader. It is without a doubt challenging, but exciting at the same time. The most consistent way to avoid becoming an all too familiar statistical loser in the stock market includes a necessary combination of advanced strategy, risk management, discipline, money management, emotional intelligence and the proper computational tools. In the end, the trader's success depends on the proven, straight forward strategy that is flexible enough to be effective for any security that meets your criteria.

No matter which strategy is chosen, the success or failure truly depends on three main components that can't be ignored:

* **Volume -** The volume informs us as to how much the instrument has been traded in the focal period. Elevated volume speaks to the significant change in interest for the asset or security. Usually (EDA focus), an increase in this metric will educate the informed trader that an impending price jump is approaching, price movement up or down doesn't matter, we can capitalize.

* **Volatility -** You can forecast the potential profit range based on historical volatility. Assuming that that price movement will recur in a manner consitent with past events - following support and resistance points, and trend lines can help predict the action.  However, elevated volatility will not only impact your profit potential, the traders risk potential is greater at the same time.  Whiplash or reversals can eat away profits very fast in a volatile market.

and last, but certianly not least:

* **Liquidity -** Liquidity enables the quick movement in and out of a position.  A trader's edge often depends on small price deltas, a lot of that can be lost if a large spread exists between the bid and ask.  This happens from a lack of liquidity (The Law of Supply and Demand). Profits erode quickly if an asset or security is illiquid, preventing the trader from executing at the target price.  Settling for the much lower bid, or much higher ask!

Before we submerge ourselves in the complexity that is the world of highly technical indicators, our EDA will focus on the basics. Often people think the basics aren't enough to improve upon the current win-ratio. I am here to argue that we will accomplish just that with a focused incorporation and analysis of invaluable elements. We will let exploratory data analysis and automated processes do the heavy lifting in the technicals, allowing more time to focus on discipline and emotional intelligence for the win.

## _**The Data:**_ 

My initial data has been sourced from the TradingView platform. Their organization is a social platform for traders and investors interested in improving investing skills and maximizing profits.  Providing top-of-the-line charting software, trade ideas, and live quotes. They have free services but in my case paid for to achieve the best real-time, accurate data. TradingView offers the added benefit of being able to export data for the paying customers. The initial analysis is looking at the historical action of an Exchange Traded Fund (ETF) that closely follows the S&P 500 market index. Direxion Daily S&P 500 Bull ($SPXL). It is a very good instrument for traders looking to hold their positions on a short leash, too high of an expense ratio for long-term durations. I chose this ETF because that is the driving force in my strategy, therefore looking to better understand the short-term indication via exploratory data analysis.

Initially viewing daily market conditions including the following: 

- **Time** (August 21, 2009 - July 20, 2020)
- **n** = 2,745 rows (after cleaning NaN values)
- **Security** (Direxion Daily S&P 500 Bull ETF (SPXL))
- **Technical Metrics**
    * Date
    * Open Price
    * Closing Price
    * High of Day Price
    * Low of Day Price
    * Volume Weighted Average Price (VWAP)
    * 200 Day Moving Average (simple)
    * 100 Day Moving Average (simple)
    * 20 Day Moving Average (Exponential)
    * Volume Moving Average
    * Relative Strength Index
    * Relative Volume

[**TradingView - market data provided by ICE Data Services**](https://www.tradingview.com/)

## _**Selecting The Days of Interest**_ 

I first created three new columns in my dataframe. The prior day's closing price, change in U.S. dollars (next day open minus prior day close), and finally the percent of change for the two sequential days.  I began this analysis with an assumption that a plus or minus 3% gap, from prior day close to next day open, would be the earmark threshold for my definition of a precipitous change. Upon further analysis I discovered that 90% of the data lies within two points; lower: -3.43% upper: 3.64%. I want to focus my EDA on the extremes I now consider to the left of -3.43% and to the right of 3.64%, totaling 171 events over the almost 11 years. I will be looking at the day leading up to each event and the day following.

![Graph full spxl data](https://github.com/chuck1l/capstone_one/blob/master/img/full_spxl.png)