"""
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.
"""

class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                res += 1
        return res

"""
this solution is a one pass function that checks to see if a character has been repeated.
to accomplish this, we iterate through the string and check if the current character is the same as the previous character.
if it is, we increment the result by 1.
notice that we start the loop at index 1 since we are checking the previous character.
the time complexity is O(n) where n is the length of the string.
the space complexity is O(1) since we are only using a few variables.
"""