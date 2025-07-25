"""
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.
"""

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = []
        for num in nums:
            if num not in seen:
                seen.append(num)
        seen.sort()
        if len(seen) == 1:
            return seen[0]
        else:
            res = sum(seen)
            for i in range(len(seen) - 1):
                if res - seen[i] > res:
                    res -= seen[i]
        return res

"""

"""