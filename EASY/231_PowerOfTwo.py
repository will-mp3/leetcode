"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and str(bin(n)).count('1') == 1

"""
This code defines a solution to check if a given integer n is a power of two.
The `isPowerOfTwo` method uses a simple condition to determine if n is greater than zero and if the binary representation of n contains exactly one '1'. 
This is because a power of two in binary form has only one bit set to '1' (e.g., 1 is 2^0, 10 is 2^1, 100 is 2^2, etc.). 
The time complexity of this solution is O(log n) due to the conversion of the integer to its binary representation, and the space complexity is O(1) since it uses a constant amount of space for the result.
"""