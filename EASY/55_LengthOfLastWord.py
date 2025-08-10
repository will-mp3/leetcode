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
This solution iterates through the string from the end to the beginning, collecting characters of the last word until it encounters a space after having collected some characters. 
The length of the last word is then returned.
The time complexity is O(n), where n is the length of the string, as we may need to traverse the entire string in the worst case. 
The space complexity is O(1) if we consider the output length as part of the return value, otherwise it is O(m) where m is the length of the last word.
"""