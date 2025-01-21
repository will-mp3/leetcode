"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # solution for O(n) time, O(n) space
        n = len(nums)
        a = [0] * n # initialize empty array

        for i in range(n):
            a[(i + k) % n] = nums[i] # use modular indexing since we are rotating cyclically

        nums[:] = a

        # solution for O(1) space, O(n * k) time
        n = len(nums)
        k %= n # for when k is greater than len(nums), saves us from O(n^2)

        for i in range(k):
            tmp = nums[-1]
            for j in range(n):
                nums[j], tmp = tmp, nums[j]

"""

"""