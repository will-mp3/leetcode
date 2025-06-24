"""
You are given a 0-indexed integer array nums and two integers key and k. 
A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.
"""

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idxs = []
        res = set()

        for i in range(len(nums)):
            if nums[i] == key:
                idxs.append(i)

        for i in range(len(nums)):
            for j in idxs:
                if abs(i - j) <= k:
                    res.add(i)

        return list(res)

"""

"""