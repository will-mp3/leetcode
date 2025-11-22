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
This solution iterates through each number in the input array nums. For each number, it checks the remainder when divided by 3. 
If the remainder is not zero, it calculates the minimum operations needed to make that number divisible by 3, 
which is either adding or subtracting the remainder or subtracting the remainder from 3. 
The total operations are accumulated in the variable res, which is returned at the end.
"""