"""
You are given an integer array nums and an integer k. You can perform the following operation any number of times:

Select an index i and replace nums[i] with nums[i] - 1.
Return the minimum number of operations required to make the sum of the array divisible by k.
"""

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k

"""
This solution calculates the sum of all elements in the input array nums and then computes the remainder when this sum is divided by k using the modulo operator (%). 
The result represents the minimum number of operations needed to make the sum divisible by k, as each operation reduces the sum by 1. 
The computed value is returned as the final result.
"""