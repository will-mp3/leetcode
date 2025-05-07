"""
Given an integer array nums, return the number of subarrays of length 3 
such that the sum of the first and third numbers equals exactly half of the second number.
"""

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                res += 1
        return res

"""

"""