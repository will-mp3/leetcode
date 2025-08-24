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

"""