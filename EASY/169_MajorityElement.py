"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}

        for i in range(len(nums)):
            if nums[i] in elements:
                elements[nums[i]] += 1
            else:
                elements[nums[i]] = 1
            
            if elements[nums[i]] >= len(nums) // 2 + 1:
                return nums[i]

"""

"""