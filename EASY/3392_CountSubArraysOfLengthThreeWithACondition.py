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
this solution is a super simple pass through with a clever trick.
since we are dealing with subarrays, 
we can almost mirror a sliding window by starting at index 1, ending at index n - 1, and checking adjacent values.
we go through the array starting at index 1, each time check if its neighbors summed and doubled equals its value.
if so increment result by 1 and return result once the loop ends.
this solution runs in O(n) linear time.
"""