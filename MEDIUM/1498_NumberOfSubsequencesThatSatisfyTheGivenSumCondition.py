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
this solution is very intuitive but relys on the underlying formula to find the amount of subsequences.
for a sequence of length n, there are 2^n valid subsequences, this is vital to understanding our solution.
intuitively we want to check all frames of our list, we frame our list using left and right pointers starting at 0 and len - 1.
the first thing we want to do is sort our list, this allows us to know the max and min of a certain subsequence.
for each frame l, r we know that if nums[l] + nums[r] <= target then that is true for all indices within that range.
this is where our formula comes in, because all within an approved range are valid, we can add 2^(l - r) to our result (l - r = frame size).
we check this condition for each frame, if nums[l] + nums[r] <= target, we check a larger l value, else we check a smaller r.
note every time we add to result to take the modulo to conform to question specifications.
"""