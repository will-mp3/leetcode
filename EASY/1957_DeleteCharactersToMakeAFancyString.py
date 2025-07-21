"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        newStr = ""

        count = 0
        prev = None
        for char in s:
            if char == prev:
                count += 1
            else:
                count = 1

            if count > 2:
                continue
            
            newStr = newStr + char
            prev = char

        return newStr

"""

"""