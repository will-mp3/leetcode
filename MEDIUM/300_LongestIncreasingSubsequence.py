"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

"""
for this problem we use a dynamic programming strategy starting at the last index of our array nums.
we know that at the last index, the largest subsequence is 1 since theres no values to come.
using this initial value and a simple formula we can work backwards through the array and find the LIS.
the way it works is as follows:
working backwards, check if the value to the right (j) is less than i, if so the LIS is 1 + LIS[j] (the previously stored LIS).
if the value is greater than, the LIS stays 1.
once the loop has fully iterated the cached LIS values will have compounded and one index will hold the maximum.
this solution runs in O(n^2) quadratic time.
"""