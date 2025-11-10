"""
You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.

In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.

Return the minimum number of operations required to make all elements in the array 0.
"""

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stack = []
        res = 0
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            if n == 0:
                continue
            if not stack or stack[-1] < n:
                res += 1
                stack.append(n)
        return res

"""
This solution uses a stack to keep track of the distinct non-zero integers in the array as we iterate through it. 
Each time we encounter a new minimum integer that is greater than the last one in the stack, we increment our operation count. 
If we find an integer smaller than the last one in the stack, we pop elements from the stack until we find a suitable position for the new integer. 
This ensures that we only count necessary operations to convert all elements to zero.  
"""