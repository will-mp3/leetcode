"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, zeros = 0, 0

        for num in nums:
            if num == 0:
                res += zeros + 1
                zeros += 1
            else:
                zeros = 0
        
        return res

"""

"""