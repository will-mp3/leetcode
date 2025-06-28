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
this solution is optimized so its a little less intuitive.
the tricky part with this problem is retaining the original order of the values.
we can sort the list and pick the k largest which will give us our sum, but we also need to retain their order.
to do this we make a new list that includes the string indices.
with this list we sort by the value just as mentioned before using a lambda function in our sorted key.
this function basically says sort by index 1 instead of index 0 in each pair.
we then grab the k largest like before and put them into a result pair list.
we sort this list like normal, which sorts it by the index by default.
with our now ordered list all thats left to do is return the value in the index value pair in a result list.
"""