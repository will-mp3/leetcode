"""
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.
"""

class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd, minEven = 0, float('inf')
        map = {}

        for char in s:
            map[char] = 1 + map.get(char, 0)
        
        for val in map.values():
            if val % 2 == 0:
                minEven = min(minEven, val)
            else:
                maxOdd = max(maxOdd, val)

        return maxOdd - minEven

"""

"""