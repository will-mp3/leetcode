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
This code defines a solution to check if a given integer n is a power of four.
The `isPowerOfFour` method initializes a variable `cur` to 1 and a variable `power` to 1. It then enters a loop where it checks if `cur` is equal to n. 
If they are equal, it returns True, indicating that n is a power of four.
If `cur` is less than n, it calculates the next power of four by raising 4 to the current value of `power`, increments `power`, and continues the loop. 
If the loop exits without finding a match, it returns False, indicating that n is not a power of four.
The time complexity of this solution is O(log n) since it iteratively checks powers of four until it exceeds n.
"""