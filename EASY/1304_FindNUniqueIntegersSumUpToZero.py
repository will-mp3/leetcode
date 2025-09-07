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
This code defines a solution to generate an array of `n` unique integers that sum up to zero. The function `sumZero` takes an integer `n` as input and returns a list of integers.
The method first checks if `n` is odd or even. If `n` is odd, it initializes the result list `res` with a single element `0`, since the sum of
zero is necessary to achieve a total sum of zero with an odd count of numbers. If `n` is even, it initializes `res` as an empty list.
Next, the method uses a loop that iterates from `1` to `n // 2`. In each iteration, it appends both `i` and `-i` to the result list `res`. This ensures that for every positive integer added, its negative counterpart is also added, maintaining the sum of zero.
Finally, the method returns the list `res`, which contains `n` unique integers that sum to zero.
The time complexity of this solution is O(n), as it involves a single loop that runs `n // 2` times. The space complexity is also O(n), since the result list `res` contains `n` integers.
"""