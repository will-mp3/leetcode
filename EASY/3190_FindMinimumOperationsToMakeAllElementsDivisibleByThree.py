"""
You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

Return the minimum number of operations to make all elements of nums divisible by 3.
"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
          if num % 3:
            res += min(num % 3, 3 - (num % 3))
        return res

"""

"""