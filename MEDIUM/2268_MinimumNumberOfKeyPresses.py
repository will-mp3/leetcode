"""
You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters. 
You can choose which characters each button is matched to as long as:

All 26 lowercase English letters are mapped to.
Each character is mapped to by exactly 1 button.
Each button maps to at most 3 characters.
To type the first character matched to a button, you press the button once. 
To type the second character, you press the button twice, and so on.

Given a string s, return the minimum number of keypresses needed to type s using your keypad.

Note that the characters mapped to by each button, and the order they are mapped in cannot be changed.
"""

import collections

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = collections.Counter(s) # store the frequencies of each value
        frequencies = sorted(freq.values(), reverse=True) # sort value frequencies

        res, count = 0, 0
        # iterate through our ordered frequencies
        for i, j in enumerate(frequencies):
            if i % 9 == 0: # if we get to another multiple of 9 (0, 9, 18, ...) add 1 to counter
                count += 1
            res += j * count

        return res

"""

"""