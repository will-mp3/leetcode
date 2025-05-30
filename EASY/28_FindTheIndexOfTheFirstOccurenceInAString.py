"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        strlen = len(needle)
        l, r = 0, strlen - 1

        while r < len(haystack):
            word = haystack[l:r+1]
            if word == needle:
                return l
            l += 1
            r += 1

        return -1

"""

"""