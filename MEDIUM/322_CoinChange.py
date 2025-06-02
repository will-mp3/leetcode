"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # zero to amount
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1 # amount + 1 is the default value from the start


"""
to solve this problem we will make use of bottom up dynamic programming.
by calculating the amount of coins necesary to get to every value up to the total and saving those values to memory
we are able to calculate the amount of coins we need total.
if we consider 0 our base case, the amount of money needed to get to the goal amount, we can begin counting backwards.
take the coin array [1, 3, 4, 5] and goal amount 7 as an example.
our dynamic programming array dp can keep track of the coins needed to reach each value up to 7:
dp[0] = 0, dp[1] = 1, dp[2] = 2, dp[3] = 1, dp[4] = 1, dp[5] = 1, dp[6] = 2 (simply the amount of coins to reach that value).
using this, we can calculate the minimum amount of coins for each coin value to reach the amount:
for 1, we see we already need 1 coin to get to that value but we need 6 more total.
we see 6 takes 2 coins, so we comput 1 + dp[6] = 3.
repeat this process for every coin value and take the minimum (2).
this solution runs in O(n) linear time.
"""