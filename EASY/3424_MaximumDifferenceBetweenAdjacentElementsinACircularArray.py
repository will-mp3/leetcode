"""
Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.
"""

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDif = abs(nums[0] - nums[-1]) # check circular case
        for i in range(len(nums) - 1):
            maxDif = max(maxDif, abs(nums[i] - nums[i + 1]))
        return maxDif

"""

"""