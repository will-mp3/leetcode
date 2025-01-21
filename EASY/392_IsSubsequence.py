"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0 # left pointer for s, right for t

        while l < len(s) and r < len(t):
            if s[l] == t[r]: # match found
                l += 1
            r += 1

        return l == len(s) # if left pointer equals the length of s, we know we have found all chars

"""
so solve this problem I make use of the two pointer method, however this does not utilize any sliding window techniques.
we have our left and right pointers, however these names are slightly misleading.
left is assigned to our source string s, and right is assigned to our target string t.
while both of our pointers are in bounds, we iterate through our two strings.
we check to see if our pointers indicate a match, that is s[l] == t[r].
if a match is found we can shift our left pointer, regardless of this we mshift our right pointer.
at some point this loop will break, either pointer will go out of bounds or perhaps both will.
if the left pointer has gone our of bounds we know that we have found a match for all characters in our source string.
we return the boolean value of this condition.
this solution runs in O(n) linear time.
"""