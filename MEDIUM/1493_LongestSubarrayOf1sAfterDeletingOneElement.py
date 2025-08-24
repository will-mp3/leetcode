"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        counts = defaultdict(int)

        left = 0
        for i in range(len(nums)):
            counts[nums[i]] += 1

            while counts[0] > 1:
                counts[nums[left]] -= 1
                left += 1
            
            res = max(res, counts[1] + counts[0] - 1)
        
        return res

"""
This code defines a solution to find the size of the longest subarray containing only 1's after deleting one element from a given binary array nums.
The `longestSubarray` method uses a sliding window approach with two pointers. It maintains a count of 0's and 1's within the current window using a dictionary `counts`.
It iterates through the array with the right pointer `i`, updating the counts of 0's and 1's as it goes. If the count of 0's exceeds 1, it moves the left pointer `left` to the right until there is at most one 0 in the window.
At each step, it calculates the potential size of the longest subarray of 1's by adding the count of 1's and the count of 0's (which is at most 1) and subtracting 1 (to account for the deletion of one element).
Finally, it returns the maximum size found.
The time complexity of this solution is O(n), where n is the length of the nums array, as each element is processed at most twice (once by the right pointer and once by the left pointer).
"""