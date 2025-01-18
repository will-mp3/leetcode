"""
Given an integer array nums sorted in non-decreasing order, 
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            
                if count > 2:
                    continue
            
            else:
                count = 1
            nums[j] = nums[i]
            j += 1

        return j

"""
for this problem, we need to modify nums in place so that the first k elements have no more than 2 duplicates.
to accomplish this, we use two pointers, i and j, where i iterates over the array and j tracks the position of our next insertion.
we also initiate a counter, count, to keep track of the current number of duplicates.
we iterate over the entire array, starting at index 1.
each iteration we check to see if the current element is a duplicate of the previous, if so we increment count by 1.
if this condition is evaluated to be true and count becomes greater than 2 we skip to the next iteration so as to leave j in place.
if the current element is unique, we set count to 1 to symbolize this.
every iteration where count is less than or equal to 2 we set position j to the element at position i and increment j.
this solution runs in O(n) linear time.
"""