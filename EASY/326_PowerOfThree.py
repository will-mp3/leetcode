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
This code defines a solution to check if a given integer n is a power of three.
The `isPowerOfThree` method initializes a variable `cur` to 1 and a variable `power` to 1. It then enters a loop where it checks if `cur` is equal to n. 
If they are equal, it returns True, indicating that n is a power of three. 
If `cur` is less than n, it calculates the next power of three by raising 3 to the current value of `power`, increments `power`, and continues the loop. 
If the loop exits without finding a match, it returns False, indicating that n is not a power of three.
The time complexity of this solution is O(log n) since it iteratively checks powers of three until it exceeds n.
"""