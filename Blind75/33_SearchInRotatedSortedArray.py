"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

"""
the first thing to note when solving is that the solution must be in O(log n), meaning we will likely need binary search.
we notice that there are two portions of this array and both of them are sorted.
use the array [5, 6, 7, 8, 9, 0, 1, 2, 4] as an example with the following logic.
we start by initializing left and right pointers, using a while loop to make sure we can check for arrays of length 1.
we initialize our middle value and check if its the target.
if that is not the case we start by checking if we are in the left portion (left value <= middle value).
if we are in the left portion:
if the target is greater than the middle value OR if the target is less than the left-most value we search right, else we search left.
if we are in the right portion:
if the target is less than the middle value OR the target is greater than the right-most value we search left, else we search right.
if the value is not found we return -1.
this solution runs in O(log n) logarithmic time.
"""