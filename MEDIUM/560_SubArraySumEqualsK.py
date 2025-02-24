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
this solution takes a greedy approach aimed at minimizing repeated work.
the backbone of the algorithm is the tracking of prefixes as we go along the given list of nums.
essentially, we are keeping track of prefix values and how many times they appear.
we use a hashmap called prefixSums to track the prefix value and the amount of times it appears.
for instance, if we see the prefix 1 appear twice it will be mapped as {1 : 2}.
this could be the case in an array such as [1, -1, 1].
using this idea we will traverse the entirety of our list of numbers, each time calculating the current sum and the diff between that and k.
our result is an integer so we will use the value stored in our prefixSums hashmap as the incrementer for result.
if we find a diff value that exists in our hashmap, meaning if our difference is equal to a previously saved prefix, we add its count.
if the diff/prefix hasnt been found we add zero.
we save our curSum as a prefix in our hashmap at the end of this logic and either increment it by 1 or add it with a count of 1.
once the loop completes we return result.
this solution runs in O(n) linear time.
"""