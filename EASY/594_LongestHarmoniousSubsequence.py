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
this problem is tricky as the description is very misleading.
on first glance our task is to find the longest subsequence (retaining order) where the largest and smallest values have a difference of 1.
this idea of retaining order is misleading because its really a counting problem.
it dosent matter what the first and last values are, and if you wanted to you could sort the list as well.
my approach is to find the count of each number in the list and save it to a hasmap.
with this i would go through each number again and if num + 1 is present, update the result with their two counts.
order dosent matter, just how many there are.
"""