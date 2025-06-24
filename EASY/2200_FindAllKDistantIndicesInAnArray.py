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
this solution is not the more optimized but I believe its the most intuitive.
we get here by breaking down the problem a little bit more, theres two parts to understand.
we need to find the elements in our array nums which are equal to our key and save their index.
with these indices, we are computing a difference equation with respect to k.
the range of values we need in our result is j - k through j + k for all in-bound indices j whose value equals key.
to do this simply we iterate through our list once more and for each index i, if the absolute value j is less than or equal to k, ass to res.
we make result a set to avoid potential duplicates, though I dont know if its necesary for this algorithm.
this solutions runs in O(n) linear time.
"""