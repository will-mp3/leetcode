"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        freqs = {}

        for num in arr:
            freqs[num] = 1 + freqs.get(num, 0)
        
        for num in freqs.keys():
            if num == freqs[num]:
                res = max(res, num)

        return res

"""

"""