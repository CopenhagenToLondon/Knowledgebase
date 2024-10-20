# There will be significant changes in the coming months

Over the coming months I will change the layout and structure of this repository.
At the moment, the repository has been structured after subject and resources.
But I will gradually change it to a walk-through of each significant topic.

I will be starting with quantitative finance, specifically walking through work
and examples on quantitative portfolio management, as this has recently become 
desired by others.

## If you want to contribute

If you've found yourself wanting to contribute either with some content or with
a donation. Please feel free to reach out to me on Email: mark@brezina.dk or [Mark Brezina - Linkedin](https://www.linkedin.com/in/markdbrezina/)


**Acknowledgment**\
Author: [Mark Brezina](https://github.com/CopenhagenToLondon)\
Contributors: [Aksel Fristrup](https://github.com/afristrup)


**Note to self, need own pictures**

1. [Trading](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/Introduction.md#trading)
2. [Portfolio management](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/Introduction.md#portfolio-management)
3. [Risk management](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/Introduction.md#risk-management)
4. [Pricing](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/Introduction.md#pricing)



# Trading

In quantitative finance trading, refers to the practice of buying or selling an asset, such as Stocks, Bonds, Options, Futures, Currency(crypto or otherwise) and more.

**Interday = Between days.**\
**Intraday = Inside one day.**\
**Bid = What price is being bid for a buy or sell order.**\
**Ask = What price is being asked for a buy or sell order.**\
**Bid-ask spread = The distance between the Bid and Ask on orders.**\
**Brokerage fee = The fee paid to a brokerage upon performing a trade.**\
**Signal = An indication in the market to buy or sell an asset.**\
**Long = Refers to buying. This also mean buying with borrowed money.**\
**Short = Refers to selling. This also means selling borrowed assets.**


## HFT - High frequency trading - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/HFT/Introduction.md) 
High frequency trading refers to trading done on the intraday time interval. Meaning within one day.
This is not to be confused with the practice of market making, which may implement High frequency trading.
But High frequency trading isn't exclusively market making.


* To perform high frequency trading successfully, one has to be subject to negligable Brokerage fees.
* To perform high frequency trading successfully, one has to be able to obtain live or intraday data at less than 2 hour intervals.
* To perform high frequency trading successfully, one has to be able to perform trading operations on intraday time intervals.

### Concepts
Here is a list of trading strategies for High frequency trading

**Market making** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/HFT/Market%20making.md) \
This strategy utilizes the distance in a bid-ask spread, along with the opportunity to obtain brokerage fee.
As the name indicates, this will be a strategy performed in running markets. 

**Arbitrage strategies** -  [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/HFT/Arbitrage.md) \
Arbitrage strategies, utilizes methods to determine incorrectly priced assets.
* Statistical arbitrage, utilizes statistics to determine arbitrage opportunities.
* Deterministic arbitrage, utilizes deterministic methods to determine arbitrage opportunities. - A simple example is the arbitrage opportunity between two exchanges with a time-delay between them.

**Momentum strategies** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/HFT/Momentum.md) \
Momentum strategies utilizes momentum in price changes for assets.\
With no or negligable brokerage fees, miniscule changes in the price of an asset can amount to large profits.


### Books, Notes, Websites
https://www.deutsche-boerse.com/resource/blob/69642/6bbb6205e6651101288c2a0bfc668c45/data/high-frequency-trading_en.pdf
https://www.quantifiedstrategies.com/trading-strategies/
https://tradinginvestment.weebly.com/blog/-dont-confuse-statistical-arbitrage-with-deterministic-arbitrage

### Code



## LFT - Low frequency trading - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/LFT/Introduction.md) 

Low frequency trading refers to trading done on the interday time interval. Meaning on intervals larger than a single day.
This is not to be confused with the practice of daytrading, which is Low frequency trading, but algorithmic trading also falls into this category. Mean reversion trading is a popular strategy implemented by both algorithmic low frequency trading and day traders.

* To perform low frequency trading successfully, one has to optimize trading returns against brokerage fees.
* To perform low frequency trading successfully, one has to be able to obtain the necessary data to run the selected strategy.
* To perform low frequency trading successfully, one has to be able to perform trading operations.

### Concepts

Here is a list of trading strategies for low frequency trading

**Mean reversion** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/LFT/1.%20Mean%20reversion.md) \
These strategies focus on the general market property of mean reversion.
![Mean Reversion](https://www.tradinformed.com/wp-content/uploads/2019/01/Mean-Reversion.jpg)



**Trend following** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/LFT/2.%20Trend%20following.md) \
These strategies focus on the occasions where markets or assets trend upwards or downwards.
![Trend trading](https://centerpointsecurities.com/wp-content/uploads/2021/07/Momentum-Trading.jpg)

**Pairs trading** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/LFT/3.%20Pairs%20Trading.md) \
These strategies focus on the occasions where two strongly correlated markets or assets diverge.
![Pairs trading](https://www.quantifiedstrategies.com/wp-content/uploads/2023/10/image-61.png)

**Momentum** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/LFT/4.%20Momentum.md) \
These strategies focus on the occasions where markets or assets gain momentum in an upwards or downwards direction.
![Momentum trading](https://centerpointsecurities.com/wp-content/uploads/2021/07/Momentum-Trading.jpg)

**Breakout** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/LFT/5.%20Breakout.md) \
These strategies focus on the occasions where assets breakout of a previous limit. Such as a previous market cap.

**Market-neutral** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/HFT/Market%20making.md) \
These strategies focus on ...

**Sentiment trading** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/LFT/6.%20Sentiment.md) \
These strategies focus on the occasions where the market sentiment changes- or affects the momentum of an asset.
![Sentiment trading](https://vladimirribakov.com/wp-content/uploads/sentiment-trading.jpg)

**Events** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/LFT/7.%20Events.md) \
These strategies focus on the occasions where unique events changes the price- or affects the momentum of an asset.

**Mathematical patterns** - [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/LFT/8.%20Mathematical%20patterns.md) \
These strategies focus on mathematical patterns to detect buy or sell opportunities.


### Books, Notes, Websites

### Code





# Portfolio Management

### Concepts

### Books, Notes, Websites

### Code

# Risk Management

### Concepts

### Books, Notes, Websites

### Code

# Pricing

### Concepts

### Books, Notes, Websites

### Code
