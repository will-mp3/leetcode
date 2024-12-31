"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[" , "}" : "{" }

        for c in s:
            if c in closeToOpen: # checks if c is a closing parenthesis
                if stack and stack[-1] == closeToOpen[c]: # check that stack is not empty and value at the top of stack is a matching open parenthesis
                    stack.pop()
                else:
                    return False
            else: # we got an open parenthesis
                stack.append(c) # can add as many open parentheses as we want consecutively

        return True if not stack else False

"""
to solve this problem we make use of a stack data structure (just like the problem from CS241...).
the reason we can utilize a stack here is because of the paired nature of parentheses.
with our stack we are able to continually take in open parentheses and then pop these as matching closed parentheses come in.
for example we could receive "( { [ (" as our first four values, as the next four come we can check if they match and pop the top value.
the next four would be ") ] } )" and instead of adding them we pop the top value: ( and so on.
if our stack is empty by the end then we know we have a valid string of parentheses, else its invalid.
this solution runs in O(n) linear time.
"""