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
the solution to this problem is nearly identical to that of problem 5.
the way we handle palindromes is through pointers that expand from a middle value.
note we have handling for both odd and even palindromes, though the logic is practically identical.
we go through each charcater in s, setting our left and right pointers to that character (if targetting odd) 
or to the character and its neighbor (if targetting even).
once our pointers are set we check if their inbounds and equal each other.
if both conditions are true then we have found a palindrome, increment result and shift the pointers outward.
note that single characters are considered palindromes.
this solution runs in O(n^2) quadratic time.
"""