"""
Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.
"""

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7

        powers = []
        nxt, base = 0, 1
        while nxt <= n:
            nxt = base ** x
            base += 1
            powers.append(nxt)
    
        dp = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD
        
        return dp[n]

"""
This code defines a solution to count the number of ways to express a given integer n as the sum of unique integers raised to the power of x.
The `numberOfWays` method first generates a list of powers of integers raised to x until the next power exceeds n. 
It then initializes a dynamic programming array `dp` where `dp[i]` represents the number of ways to express the integer i using the generated powers.
The method iterates through each power and updates the `dp` array in reverse order to ensure that each power is only used once in each combination. 
Finally, it returns the value of `dp[n]`, which contains the number of ways to express n as required, modulo 10^9 + 7.
The time complexity of this solution is O(n * k), where n is the target integer and k is the number of unique powers considered.
"""