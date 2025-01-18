"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}

        for i in range(len(nums)):
            elements[nums[i]] = 1 + elements.get(nums[i], 0)
            
            if elements[nums[i]] >= len(nums) // 2 + 1:
                return nums[i]

"""
to solve this problem we make use of a hash map (dictionary) to track the occurances of each value.
for each element in nums, we update its key in our hashmap.
to do this we use the get operator, we add 1 to either the current value at that key or 0 (if the key dosent exist yet).
while the loop runs we continuously check to see if our current number has passed the majority threshold.
if it has, return that number.
this solution runs in O(n) linear time.
"""