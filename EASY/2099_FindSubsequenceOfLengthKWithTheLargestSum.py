"""
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing 
the order of the remaining elements.
"""

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = []

        # create list of number and their indexes
        idxs = [ [i, n] for i, n in enumerate(nums)]

        # sort these pairs by their number, not index
        sort = sorted(idxs, key = lambda x: x[1])

        # get the largest k value pairs
        resPairs = []
        for i in range(len(nums) - k, len(nums)):
            resPairs.append(sort[i])
        # sort the largest k pairs by index
        resPairs.sort()

        # gather values from sorted indices
        for pair in resPairs:
            res.append(pair[1])
        
        return res

"""

"""