"""
You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.
"""

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])
        return res

"""
this solution uses dynamic programming.
we create a 2D array dp where dp[i][j] represents the length of the longest valid subsequence ending with the i-th and j-th elements.
we iterate through each number in nums, and for each number, we update the dp array based on the previous values.
we keep track of the maximum length found across all pairs of indices and return it as the result.
this solution runs in O(n * k^2) time, where n is the length of the input array and k is the given integer.
"""