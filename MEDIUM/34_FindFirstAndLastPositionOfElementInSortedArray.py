"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)

        return [left, right]
    
    # leftBias = True/False; if False our res is rightBias (right index)
    def binarySearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1

        while l <= r:
            # calculate middle position
            m = (l + r) // 2

            # if target is bigger than our middle value, we know its right centered
            if target > nums[m]:
                l = m + 1
            # if target is smaller than our middle value, we know its left centered
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                # check which result index we are searching for
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1

        return i

"""

"""