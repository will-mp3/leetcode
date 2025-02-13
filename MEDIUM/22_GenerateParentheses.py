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
this solution makes use of a recursive function that traverses a decision tree.
to envision this, imagine that we have three rules to follow:
only add open parenthesis if open count < n
only add a closed parentheses if closed < open
only valid if open == closed == n
we must traverse our decision tree following these rules to discover each valid set of parentheses where open == closed == n.
this is also conveniently our base case.
we keep a stack to track our parentheses and start by calling our recursive function with the open and closed count equal to zero.
our base case is when the open count, closed count, and n are all equal; at that point join the stack and append to result.
if that is not the case we begin making recursive calls based on two conditions:
if the open count is less than n we add an open parenthesis to the stack and call our function with 1 added to the open count.
this branches off and continues until the base case is found, we add a line to pop the stack after so its clear for the next combination.
if the closed count is less than the open count we can add a closed parenthesis to the stack.
we call our function like before but this time adding one to the closed count.
when all is said and done we will have all of the valid combinations saved to result and can return it.
"""