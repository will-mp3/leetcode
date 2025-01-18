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
this problems solution is extremely similar to LeetCode 27, we must rewrite our array nums so as to remove all duplicates.
the way we accomplish this is by using two pointers, one pointer as our insertion point and one for iteration.
our insertion pointer will increment every time our iteration pointer finds no duplicates.
our iteration pointer (i) checks to see if itself and the previous elemtn are equal to identify duplicates.
if no duplicate is found, the element at i is copied to our current insertion index j.
if a duplicate is found, our insertion index remains since we know the current value must be overwritten at some point.
for example, if there are three "4"s in a row, our insertion index will stop on that second four, waiting until i finds a value that is not 4.
once i finds a value that is not 4, it copies it to the insertion position (the second 4).
note that we are returning k, the number of non duplicate values.
this solution runs in O(n) linear time.
"""