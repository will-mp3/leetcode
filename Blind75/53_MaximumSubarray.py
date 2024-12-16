"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

"""
begin by tracking the max subarray and the current sum, two variable we will be comparing.
iterate through the list, adding each variable and evaluating two things:
is the current sum (before n is added) negative? if so reset it to zero, the previous values add nothing.
next add n to the current sum and check: is the current sum more than the current max value? do this through the entire list.
this silution runs in O(n) linear time.
"""