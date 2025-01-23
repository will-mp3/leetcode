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

            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            
            valley = prices[i]

            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            
            peak = prices[i]

            profit += peak - valley
        
        return profit

"""

"""