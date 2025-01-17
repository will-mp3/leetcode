"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

"""
for this problem we make use of two pointers, specifically taking advantage of the fact that variables can be moved in our input array.
because we are only counting the first k elements (the number of elements minus those to be removed), we can simply overwrite them.
what this would look like is if we had an array [1, 5, 6, 8, 3, 4, 9, 5] and we wanted to remove 5,
our array would become [1, 6, 8, 3, 4, 9, 5, Null].
what is happening here is every iteration our value at pointer j does not equal i, we copy the value over and increment pointer i with j.
if we come across our value, we skip this step, and pointer i stays where it is (at this value).
the next iteration that dosent match this value then gets overridden.
simply put, pointer i only increments when pointer j is on a value that is not equal to our solution.
the purpose of pointer i is to overwrite our target value.
this solution runs in O(n) linear time.
"""