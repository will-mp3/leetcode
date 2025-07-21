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
this code defines a solution to the problem of making a string fancy by ensuring that no three consecutive characters are equal.
The `makeFancyString` method iterates through the input string `s`, keeping track of the current character and its count of consecutive occurrences. 
If a character appears more than twice in a row, it is skipped. The resulting string is built up in `newStr`, which is returned as the final output. 
This approach ensures that the final string meets the criteria for being fancy, while maintaining the order of characters from the original string.
The time complexity of this solution is O(n), where n is the length of the input string s, as it processes each character exactly once.
"""