"""
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. 
Since the answer may be too large, return it modulo 10**9 + 7.
"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)

        l, r = 0, n - 1
        res = 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + (2 ** (r - l))) % mod
                l += 1
            else:
                r -= 1
            
        return res

"""

"""