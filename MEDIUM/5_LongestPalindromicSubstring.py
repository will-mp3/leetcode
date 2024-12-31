"""
Given a string s, return the longest palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # check odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]: # check if pointers are in bounds and contain a palindrome
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # check even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: # check if pointers are in bounds and contain a palindrome
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

"""
to solve this problem we make use of pointers to help identify palindromes in our string.
for each character in our string s we check for both even and odd palindromes (in reference to character count).
the formula for each is essentially the same, just note the difference in pointer position above.
the algorithm used checks to see if the left and right pointers are equal, denoting a palindrome, 
and continues to expand them until the condition fails.
the result itself and the results length are tracked, allowing for us to check and store our result when a new max length is found
this is done for every character in our list.
this solution runs in O(n^2) quadratic time.
"""