"""
You are given an integer array nums of length n.

A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:

Left subarray contains indices [0, i].
Right subarray contains indices [i + 1, n - 1].
Return the number of partitions where the difference between the sum of the left and right subarrays is even.
"""

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 1):
            if (sum(nums[:i + 1]) - sum(nums[i + 1:])) % 2 == 0:
                res += 1
        return res

"""

"""