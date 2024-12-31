"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. 

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum(): # check if character is alphanumerical
                newStr += c.lower()

        return newStr == newStr[::-1] # reversed string

"""
this solution is very simple.
our approach is to reformat the given string, removing all non alphanumerial values and making every character lowercase.
once done we simply check if our new string is equal to its reversed self.
"""