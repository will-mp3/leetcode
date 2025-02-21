"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # phase one: find where slow and fast intersect
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # advance fast by 2

            if slow == fast:
                break

        slow2 = 0
        # phase two: find where slow and slow2 intersect and return
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                return slow

"""

"""