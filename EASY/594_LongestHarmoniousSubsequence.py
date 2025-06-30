"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        # build hashmap
        numMap = {}
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)
        
        for num in nums:
            if num + 1 in numMap:
                res = max(res, numMap[num] + numMap[num + 1])

        return res

"""

"""