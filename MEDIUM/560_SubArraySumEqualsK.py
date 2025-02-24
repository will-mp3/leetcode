"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = { 0 : 1 }

        for n in nums:
            curSum += n
            diff = curSum - k

            # add the count of prefixes to result, add 0 if diff is not present
            res += prefixSums.get(diff, 0)
            
            # add the prefix or increment an existing prefix
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res

"""

"""