"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]: # check if pointers are in bounds and contain a palindrome
                res += 1
                l -= 1
                r += 1
            
            # check even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: # check if pointers are in bounds and contain a palindrome
                res += 1
                l -= 1
                r += 1

        return res

"""

"""