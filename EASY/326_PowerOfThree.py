"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        cur, power = 1, 1
        while cur <= n:
            if cur == n:
                return True
            cur = 3 ** power
            power += 1
        return False

"""

"""