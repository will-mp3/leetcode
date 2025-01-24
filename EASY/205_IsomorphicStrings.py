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
for this solution we make use of a multiple dicitonary mapping technique and the zip function in python.
we want to map the characters in both strings as we come across them and compare accordingly as we go.
to do this we initiate t to s and s to t dictionaries and iterate through the characters in s and t.
to do this we use the zip function, which allows us to combine iterables into a tuple-like form and traverse them side by side.
we go through the characters in s and t and check two cases.
the first being if the characters are not mapped in BOTH dictionaries, if this is the case we map them to both dicts.
the second case is when a mapping dosent exist or dosent map.
we check to see if the value mapped to key c1 equals c2 and vise verse.
if this ever executes false is immediately returned, we found uneven or incorrect mapping.
if the entire traversal runs we return True.
"""