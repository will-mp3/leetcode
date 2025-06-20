"""
You are given an integer array nums and an integer k. 
You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence 
is at most k.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without 
changing the order of the remaining elements.
"""

class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = 1
        first = nums[0]
        for num in nums:
            if abs(num - first) > k:
                first = num
                res += 1
        return res

"""
to solve this problem we use a greedy approach.
we can sort our array nums in increasing order to give us an easier way of working with its values.
when the values are sorted we can traverse them in order, tracking the first value and denoting when an element is too large for a partition.
the way this works in code is by tracking a first value to represent the first and smallest value of a current partition.
we go through each number in nums, and if the difference between the number and our first value is greater than k we do the following.
first we save our current nmber as our new first value, then we increment our partition count to signify a new partition.
we let this loop run and return the result.
this solution runs in O(n) linear time.
"""