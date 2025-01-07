"""
You are given two positive integers n and k. 
A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
"""

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        x = 1

        while x <= n:
            if n % x == 0:
                factors.append(x)
            x += 1
        
        if len(factors) < k:
            return -1
        
        return factors[k - 1]

"""

"""