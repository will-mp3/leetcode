"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] if n % 2 == 1 else []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        return res

"""

"""