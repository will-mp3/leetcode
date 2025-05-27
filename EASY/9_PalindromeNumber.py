"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string  = str(x)

        if string == string[::-1]:
            return True
        else:
            return False

"""
to solve this problem we use basic string manipulation to reverse our input number.
we first must turn our integer into a string.
once done we can use python syntax [::-1] to reverse this string and check if they are equal.
"""