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

## _**Selecting The Days of Interest:**_ 

I first created three new columns in my dataframe. The prior day's closing price, change in U.S. dollars (next day open minus prior day close), and finally the percent of change for the two sequential days.  I began this analysis with an assumption that a plus or minus 3% gap, from prior day close to next day open, would be the earmark threshold for my definition of a precipitous change. Upon further analysis I discovered that 90% of the data lies within two points; lower: -3.43% upper: 3.64%. I want to focus my EDA on the extremes that I now consider to the left of -3.43% and to the right of 3.64%, totaling 171 events over the almost 11 years. Ongoing analysis will include 10 minute intervals for the trade-day leading up to each event through the close of the trade-day following.

![Graph full spxl data](https://github.com/chuck1l/capstone_one/blob/master/img/full_spxl.png)

#### _**The Initial View of These Two Data Sets**_

We don't gain much insight from this view, just noticing the frequency of events outside of the threshold.

![Graph Less Than -3.43%](https://github.com/chuck1l/capstone_one/blob/master/img/spxl_lt_n3.43%25.png)
![Graph Greater Than 3.64%](https://github.com/chuck1l/capstone_one/blob/master/img/spxl_gt_3.64%25.png)

As human nature tends to lead us, we focus on the positive events first.  Those days that had a catalyzing event leading to greater than or equal to a **3.64% overnight gap** (due to after hours and futures trading).

At first glance, we looked at the percent of change from the open mark versus the closing - for 3 days. The day before the event, day of the event, and then the day after the event. 

**($Close - $Open) / $Open x 100** 

![Graph $close vs $open](https://github.com/chuck1l/capstone_one/blob/master/img/graph_%25_op_clo.png)

This graph tells me very important information. Remembering that I am looking to be right more than 50% of the time, there is another caveat, the move must be substantial enough for decent profit on that correctness. Learning: If I hold a position from open to close.
* The day before has an average of negative price change.
    * That's okay, we can't see the future.
    * Seeing an almost even split between positive and negative action suggests people acting on impending catalysts evenly.
    * Some are right, some are wrong
* Holding the day of the event would produce a win on average.
    * Between 0.7% and 13.6% gain over half of the time.
    * Acceptable, but I hypothesize that we can do better
    * With a mean of 0.7% we are very close to 0% gain or loss, stop losses are paramount
* The day after seems to pull back over 50% of the time.
    * Risking a -1.3% to -13.15% loss!
    * Holding the day after comes with great risk

The name of the game is **intraday** money movement, why focus on open and close when there is potentially greater opportunity throughout the day? Let us take a closer look by focusing on the **High of Day** mark versus the open price for the same three days around the event. Still looking at the **3.64% overnight gap** referred to as an event. 

**($High of Day - $Open) / $Open x 100**

![Graph $High of Day vs $open](https://github.com/chuck1l/capstone_one/blob/master/img/graph_%25_hi_open.png)

Very interesting. Every scenario can provide a meaningful return averaging around 3% from just the open price to the high of day. Putting this into a perspective of earnings potential:

Minimum account size for a day trader, using a broker based in the United States, is $25,000 to satisfy the SEC Pattern Day Trading rule. The SEC Pattern Day Trading rule states that a trader must maintain a minimum of $25,000 account size if he/she plans to execute greater than 3 day trades in any given five-day period (weekends and holidays don't count) using a margin account. You have greater buying power with a margin account but let's say you only trade the $25,000 balance: Current market value of $SPXL = $48.00
* $25,000 @ $48/share = ~ 520 shares of $SPXL
* 3% increase is $1.44 / share
* $1.44 x 520 shares = $749 profit for the day  
* Identifying 2 or 3 trades per week could return $80,000 to $120,000 yearly if you average the 3% mark
* Maximize profits, don't stop at 3% if the momentum is still in your favor
* Minimize losses when the trade doesn't go as planned
* Remember that is minimum account size, 3% was only the average, could be much larger
* Double or triple conservatively

The EDA up to this point has raised new questions to further analyze:
* What does daily action look like when not impacted with a catalyzing event?
* What would the return look like **High of Day** versus **Low of Day**?
* Can we identify a repeatable method of entering a position closer to the **Low of Day**?
* Does the **Low of Day** and **High of Day** repeat at a certain time of the day?
* Could volume metrics preceed price movement to forecast the future action?

## _**The Answers:**_

### _**Daily Action Without A Catalyst Driving Volatility**_

The original graph from this presentation illustrates the fact that we are searching for elevated volatility in a day following an extreme condition from the previous day. Now, this is the case because the SEC strongly suggests that news is released outside of normal market hours. Thus, post-market and futures activity create an overnight gap. Our trigger for attention. Through the EDA colored lens, the next two illustrations offer more insight into that concept.

![mid-90 $close vs $open](https://github.com/chuck1l/capstone_one/blob/master/img/graph_pos_45_op_cl.png)

We can see that even when overnight action is positive, but less than or equal to 2%, our potential profit for holding throughout the day is restrained. Perhaps intuitively 90% of the data lies within less than 3%, centered greatly around zero, and has an equal likelihood of turning negative. Very difficult to forecast the direction of price action, and minimal ROI if you can't capture the entire move.  

![mid-90 $hofd vs $open](https://github.com/chuck1l/capstone_one/blob/master/img/graph_pos_45_hofd_op.png)

A more concerning concept is that you would really have to capture the high of day point to create acceptable profit. The high of day versus open price mean difference is only 1.21% with a much lower probability of realizing a move greater than 3%.

### _**What Would The Return Look Like High of Day Versus Low of Day**_

![hofd vs lofd non-cat](https://github.com/chuck1l/capstone_one/blob/master/img/graph_pos_45_hofd_lofd.png)
![hofd vs lofd w/ cat](https://github.com/chuck1l/capstone_one/blob/master/img/graph_%25_hiofd_lowofd.png)

These illustrations scream potential, even on the days that don't follow an extreme condition from the day before. The trick will be identifying metrics to lockdown a near low of day entry and taking profits toward the high of day. The main focus should still be centered on days that follow a precipitous gapper, but considerable opportunity for scalping on slower days exists.