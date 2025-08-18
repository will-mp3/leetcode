"""
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. 
You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.
"""

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    for val in candidates:
                        if dfs(next_nums + [val]):
                            return True
            return False

        return dfs([float(x) for x in cards])

"""
This code defines a solution to determine if it is possible to arrange four given integers (cards) using basic arithmetic operations to evaluate to 24.
The `judgePoint24` method uses a depth-first search (DFS) approach to explore all possible combinations of the numbers and operations. 
It defines a helper function `dfs` that takes a list of numbers and recursively checks if any combination can yield 24.
The function checks all pairs of numbers, applies the four basic operations (addition, subtraction, multiplication, and division), and recursively calls itself with the new list of numbers after applying the operation. 
It uses a small epsilon value (EPS) to handle floating-point precision issues when comparing to 24.
If it finds a valid combination that evaluates to 24, it returns True; otherwise, it returns False.
The time complexity of this solution is exponential in nature due to the recursive exploration of combinations.
"""