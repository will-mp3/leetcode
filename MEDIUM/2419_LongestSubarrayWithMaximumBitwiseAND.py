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
This code defines a solution to find the length of the longest subarray with the maximum bitwise AND.
The `longestSubarray` method first determines the maximum value in the input array, which represents the maximum possible bitwise AND (k).
It then iterates through the array to find the length of the longest contiguous subarray where all elements are equal to k.
The method maintains a count of the current length of such subarrays and updates the maximum length found so far.
Finally, it returns the maximum length of the subarray that meets the criteria.
The time complexity of this solution is O(n), where n is the length of the input array, as it requires a single pass to find the maximum value and another pass to determine the longest subarray.
"""