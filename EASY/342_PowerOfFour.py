"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cur, power = 1, 1
        while cur <= n:
            if cur == n:
                return True
            cur = 4 ** power
            power += 1
        return False

"""

"""