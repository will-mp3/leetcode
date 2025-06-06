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
this problem is broken up into three logic segments.
we want to use a stack for this problem but also track the smallest character remaining inb our original string s.
the basic logic is for every character in s we push it to the stack and then check if that character is the smaller than the smallest in s.
if the top of the stack is the smallest we can append it to result, otherwise move to the next character.
at the end we append the remainder of the stack and return the string.
more in depth, we use Counter to create an array of frequencys for each characater in s.
this sorted frequency array is how we will track the smallest characters left in s.
our helper function min_char turns numbers 1 - 26 into their respective lowercase letters and returns the first letter present in freq.
with that set up we loop through every character in s, each time pushing to the stack, decrementing its freq value and checking:
if the stack is not empty and the top value of the stack is less than the smallest in s.
while this is true we pop and append the stack.
once this loop completes we append the remaining stack and return the result.
"""