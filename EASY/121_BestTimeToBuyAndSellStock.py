"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left and right pointers
        maxP = 0 # max profit

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        
        return maxP

"""
to solve this problem we wanted to make use of two pointers and a variable tracking our max profit.
iterate through the list, first checking if the left pointer is less than the right pointer (profitable).
if so: calculate the profit from the current buy and sell points (left and right) and compare it to the current max profit.
if left is greater than right, reset the pointers to equal eachother.
finish the loop incrementing the right pointer by 1.
this solution runs in O(n) linear time.
"""