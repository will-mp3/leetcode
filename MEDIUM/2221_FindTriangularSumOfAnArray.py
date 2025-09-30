"""
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.
"""

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            copy = []
            for i in range(len(nums) - 1):
                copy.append((nums[i] + nums[i + 1]) % 10)
            nums = copy

        return nums[0]

"""
This code defines a solution to compute the triangular sum of an array of digits. The function `triangularSum` takes a list of integers `nums`, where each integer is a digit between 0 and 9, and returns the triangular sum as described in the problem statement. The approach used in this solution can be broken down into the following steps:
1. Use a while loop to repeatedly process the array until it contains only one element.
2. Inside the loop, create a new list `copy` to store the results of the current iteration.
3. Iterate through the array `nums` using a for loop, calculating the sum of each pair of adjacent elements, taking the result modulo 10, and appending it to the `copy` list.
4. After processing all pairs, replace the original `nums` array with the `copy` list.
5. Once the loop exits (when `nums` has only one element), return that element as the triangular sum.
The time complexity of this solution is O(n^2) in the worst case, where n is the length of the input array, due to the nested loops (the while loop runs n times and the for loop runs up to n times in each iteration). The space complexity is O(n) for storing the intermediate results in the `copy` list.
"""