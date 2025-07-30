"""
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0 # An empty array has no non-empty subarrays

        # Step 1: Find the maximum possible bitwise AND (k)
        k = 0
        for num in nums:
            if num > k:
                k = num

        # Step 2: Find the length of the longest subarray where all elements are equal to k
        max_length = 0
        current_length = 0

        for num in nums:
            if num == k:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 0
        
        # After the loop, account for the case where the longest subarray ends at the end of `nums`
        max_length = max(max_length, current_length)

        return max_length

"""

"""