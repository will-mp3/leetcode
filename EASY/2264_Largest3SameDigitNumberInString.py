"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
"""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res, count = float("-inf"), 0
        prev = None

        for char in num:
            if char == prev:
                count += 1
            else:
                count = 1

            if count == 3:
                res = max(res, int(char))
            
            prev = char
        
        return str(res) * 3 if res != float("-inf") else ""

"""

"""