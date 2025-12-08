"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)

"""
This solution calculates the number of odd integers in the inclusive range [low, high] by leveraging integer division. 
It computes the count of odd numbers from 0 to high and subtracts the count of odd numbers from 0 to low - 1. 
The formula (high + 1) // 2 gives the count of odd numbers up to high, 
while (low // 2) gives the count of odd numbers up to low - 1. 
The difference between these two values yields the total count of odd numbers in the specified range.
"""