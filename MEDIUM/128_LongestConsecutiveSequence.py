"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

"""
to solve this problem in O(n) time, we will make use of a set.
we turn our given array into a set and iterate through it from the first value, checking two things:
first, does the current value have a left neighbor (does 100 have 99), if no then this is the start of a sequence.
from here, check if it has the right neighbor, if it does then check if that right neighbor has a right neighbor etc etc.
continue through the list, creating new sequences when there is no left neighbor and continuing if not.
this solution runs in O(n) linear time and memory complexity O(n) because of the set.
"""