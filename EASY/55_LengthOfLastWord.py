"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = ""

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and len(res) != 0:
                break
            if s[i] != " ":
                res = res + s[i]

        return len(res)

"""

"""