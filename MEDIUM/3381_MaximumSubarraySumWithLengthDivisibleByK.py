"""
You are given an array of integers nums and an integer k.

Return the maximum sum of a subarray of nums, such that the size of the subarray is divisible by k.
"""

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = 0
        maxSum = -sys.maxsize
        kSum = [sys.maxsize // 2] * k
        kSum[k - 1] = 0
        for i in range(n):
            prefixSum += nums[i]
            maxSum = max(maxSum, prefixSum - kSum[i % k])
            kSum[i % k] = min(kSum[i % k], prefixSum)
        return maxSum

"""
This solution uses a prefix sum approach combined with modular arithmetic to efficiently find the maximum subarray sum whose length is divisible by k. 
It maintains a running total of the prefix sum and an array kSum to store the minimum prefix sums for each possible remainder when divided by k. 
As it iterates through the array, it updates the maximum sum found by checking the difference between the current prefix sum and the minimum prefix sum corresponding to the same remainder class. 
Finally, it returns the maximum sum found.
"""