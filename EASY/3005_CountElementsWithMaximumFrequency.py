"""
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        maxC = 0

        for num in nums:
            counts[num] += 1
            maxC = max(maxC, counts[num])
        
        res = 0
        for count in counts.values():
            if count == maxC:
                res += count

        return res

"""

"""