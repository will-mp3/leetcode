"""
You are given a string s and a robot that currently holds an empty string t. 
Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.
"""

class Solution:
    def robotWithString(self, s: str) -> str:
        stack, res = [], []
        # list of characters and their frequencys in string s
        freq = Counter(s)

        def min_char(freq):
            for i in range(26):
                char = chr(ord('a') + i) # find the lowercase equivalent of i (ord(a) = unicode of a)
                if freq[char] > 0: # return first present character in sorted frequency array
                    return char
            return 'a'

        for char in s:
            stack.append(char)
            freq[char] -= 1
            while stack and stack[-1] <= min_char(freq): # while our stack has values and the top value <= min char in s
                res.append(stack.pop())

        # empty remaining stack
        while stack:
            res.append(stack.pop())

        return ''.join(res)

"""

"""