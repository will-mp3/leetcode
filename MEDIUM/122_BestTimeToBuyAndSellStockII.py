"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        peak, valley = prices[0], prices[0]
        profit = 0
            
        while i < len(prices) - 1:
            # while the next day has a lower price, increment i
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            
            valley = prices[i]

            # while the next day has a higher price, increment i
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            
            peak = prices[i]

            profit += peak - valley
        
        return profit

"""
to solve this problem we make use of the peak valley strategy by tracking the low and high points as we go.
we start by initializing our peak, valley, and profit variables; peak and valley start at the first index and profit starts at 0.
we set up a loop that runs until i reaches the length threshhold of our prices array.
inside of this loop there are two nested loops that increment i.
the first one is to find our valley, i in incremented while the next day, i + 1, is less than the current i.
simply put, i is incremented until the chart goes positive and then valley is set to that minimum value.
this same logic is applied to find the peak, except we are incrementing while the chart is rising.
once the chart peaks and starts to dip we set our peak value and then calculate profit.
at this point our outer loop executes again, this time with our updated i values and continues the previous logic.
this executes until i moves out of bounds and then returns profit.
"""