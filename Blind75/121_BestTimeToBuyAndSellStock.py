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