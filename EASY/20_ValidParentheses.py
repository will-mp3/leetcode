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

"""