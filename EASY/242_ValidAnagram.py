"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 2, O(1) space complexity assuming sorting algorithms are considered negligible
        return sorted(s) == sorted(t)

        # solution 3, kinda cheating
        return Counter(s) == Counter(t)

        # solution 1, what you would typically submit
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        # build hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # iterate through hashmaps
        for c in countS:
            if countS[c] != countT.get(c, 0): # use get function to avoid key error if c dosent exist in countC
                return False
        return True

"""

"""