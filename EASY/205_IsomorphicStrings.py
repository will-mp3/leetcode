"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # define dictionaries to map characters in t to s and characters in s to t
        maps2t = {}
        mapt2s = {}

        for c1, c2 in zip(s, t):
            # case 1: check if characters are mapped already, if not map them into both dicts
            if c1 not in maps2t and c2 not in mapt2s:
                maps2t[c1] = c2
                mapt2s[c2] = c1
            
            # case 2: mapping dosent exist or mapping dosent match
            elif maps2t.get(c1) != c2 or mapt2s.get(c2) != c1:
                return False
            
        return True

"""

"""