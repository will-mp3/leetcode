"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1 # insertion index j

        # j in essentially rewriting nums using values stored at i
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: # if current index is not a duplicate of previous index
                nums[j] = nums[i] 
                j += 1
        return j

"""

"""