

## Market state

* Has an extremal event occured?\
**Question:**\
How precise is Bollinger bands of 1.5, 2 or 2.5 sigma at detecting Extremal events?\
How precise is the 10%, 5% and 1% quantile of xyz-interval returns at detecting Extremal events?\
How precise is the 10%, 5% and 1% quantile of xyz-interval prices at detecting Extremal events?


* What is the current trend state?\
**Question:**\
How precise is the mean return functional at detecting the trend?\
How precise is the positive-negative functional at detecting the trend?\
How precise is the battery of statistical tests at detecting the trend?


* What is the current risk state?\
**Question:**\
What's the current volatility states?\
What's the current connectability in the market?\
What are the current probability states?



## Detect strategy

* If Up trend:\
*run long between 0-tangents, to minimize risk of loss*

1. Check for Extremal events \
   If Negative Extremal event occurs - Close trades, take loss. Halt trading\
   If Positive Extremal event occurs - Close trades, take profit. Gauge trading
2. Check for Divergence and weight of closed trades.\
   If open, high and low diverge over time.\
   Consider whether a high volatility period is ahead and how to benefit on buying low and selling high.\
   If the the weight of the closing trades are significant and a certain direction has been chosen.\
   Consider whether to play along the direction or to take profit before a direction change.
3. Check for moment and moment drift

* If Down trend:\
*run short between 0-tangets, to minimize risk of loss*

1. Check for Extremal events \
   If Negative Extremal event occurs - Close trades, take loss. Halt trading\
   If Positive Extremal event occurs - Close trades, take profit. Gauge trading
2. Check for Divergence and weight of closed trades.\
   If open, high and low diverge over time.\
   Consider whether a high volatility period is ahead and how to benefit on buying low and selling high.\
   If the the weight of the closing trades are significant and a certain direction has been chosen.\
   Consider whether to play along the direction or to take profit before a direction change.
3. Check for moment and moment drift

* If No/Flat trend:\
*run long between 0-tangents, to minimize risk of loss*\
*run short between 0-tangets, to minimize risk of loss*

1. Check for mean reversion indications\
   If the 6, 20 and 40 day moving averages cross\
   If the average directional index changes\
   If the trend indicators change\
   If the autocorrelation indicator increases
2. Check for Resistance levels
   If the Price reaches a previous resistance level - concrete price
   If the price reaches a fibonacci level - mythical & mystical price level
   If the price drops by x% from a previous max or min
3. Check for Breakthrough signals
   *Unsure how to check this at the moment*

* If unknown trend:\
*Wait till a clear trend manifests*



