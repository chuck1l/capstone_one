# <div align="center">_**Can we improve a trader's win-ratio through EDA?**_</div>
## <div align="center">_**Lawrence C. Williams - Capstone Project I - July 24, 2020**_</div>

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

I first created three new columns in my dataframe. The prior day's closing price, change in U.S. dollars (next day open minus prior day close), and finally the percent of change for the two sequential days.  I began this analysis with an assumption that a plus or minus 3% gap, from prior day close to next day open, would be the earmark threshold for my definition of a precipitous change. Upon further analysis I discovered that 90% of the data lies within two points; lower: -3.43% upper: 3.64%. I want to focus my EDA on the extremes that I now consider to the left of -3.43% and to the right of 3.64%, totaling 171 events over the almost 11 years. Ongoing analysis will include 10 minute intervals for the trade-day leading up to each event through the close of the trade-day following.

![Graph full spxl data](https://github.com/chuck1l/capstone_one/blob/master/img/full_spxl.png)

#### _**The Initial View of These Two Data Sets**_

We don't gain much insight from this view, just noticing the frequency of events outside of the threshold.

![Graph Less Than -3.43%](https://github.com/chuck1l/capstone_one/blob/master/img/spxl_lt_n3.43%25.png)
![Graph Greater Than 3.64%](https://github.com/chuck1l/capstone_one/blob/master/img/spxl_gt_3.64%25.png)

As human nature tends to lead us, lets focus on the positive events first.  Those days that had a catalyzing event leading to greater than or equal to a **3.64% overnight gap** (due to after hours and futures trading).

At first glance, we looked at the percent of change from the open mark versus the closing - for 3 days. The day before the event, day of the event, and then the day after the event. **($ close - $ open) / $ open** 

![Graph $close vs $open](https://github.com/chuck1l/capstone_one/blob/master/img/graph_%25_op_clo.png)

This graph tells me very important information. Remembering that I am looking to be right more than 50% of the time, there is another caveat, the move must be substantial enough for decent profit on that correctnes. Learning: If I hold a position from open to close.
1. The day before has an average of negative price change.
    * Thats okay, we can't see the future.
    * Seeing an almost even split between positive and negative action suggests people acting on impending catalyst evenly.
    * Some are right, some are wrong
2. Holding the day of would produce a win on average.
    * Between 0.7% and 13.6% gain over half of the time.
    * Acceptable, but we can do better
    * With a mean of 0.7% we are very close to 0% gain or loss, stop losses are paramount
3. The day after seems to pull back over 50% of the time.
    * Risking a -1.3% to -13.15% loss!
    * Holding the day after comes with great risk