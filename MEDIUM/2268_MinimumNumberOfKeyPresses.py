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
this problem relies on understanding what is being asked.
we know that our keypad has 9 characters, and we can arrange it however we would like.
the logical decision is to map the first 9 characters to unique keys, then the second 9 characters, and so on for even distribution.
this is simple enough, but for larger strings, we may need to be more strategic in which keys get mapped where so as to reduce presses.
for example, we wouldnt want a character that appears 10 times mapped to the second or third layer of our key.
to account for this, we start by storing the frequency of each character in a hashmap called freq (using the collections import).
we store this as an array of digits, frequencies, in reverse ascending order (largest to smallest).
we initialize result and count to zero for tracking and then iterate over frequencies.
we check if the index is divisible by 9, since each index represents a new unique character.
if its divisible by 9 we increment count by 1, what this is doing is representing each layer of the keypad.
the first 9 digits have count equal to 1, the next 9 ocunt equals 2, and so on.
as we are doing this we are incrementing result by the amount of said digit multiplied by its layer.
if our digit appears 3 times (frequencies[i] = j = 3) and count is at 1 (first layer) we know that we add 3 presses.
if our digit appears 3 times and count is 2 then we need 6, hence the need for count and its multiplication.
once the loop finishes we return res.
"""