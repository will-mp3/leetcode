"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        only add open parenthesis if open count < n
        only add a closed parentheses if closed < open
        only valid if open == closed == n
        """

        stack = []
        res = []

        def backtrack(openN, closedN): # nested recursive function
            # base case
            if openN == closedN == n:
                res.append("".join(stack)) # taking the values in our stack and joining them
                return

            # the following two conditionals effectively check every valid branch in the decision tree
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # every time we're done with backtracking we pop the just added character

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

"""

"""