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
this problem would normally be as simple as an O(n) single pass algorithm, however the problem wants us to solve it in O(log n) time.
to accomplish this we use a mdofied version of binary search, utilizing left and right "biasing" depending on if we which target we want.
all of the logic is handled in our binary search function and makes use of left and right pointers.
ultimately we are hoping to return the index of the first appearance (left bias) and last appearance(right bias).
the idea is that when left biased, we focus on shifting our right pointer left and when right biased shifting our left pointer right.
while our pointers arent overlapping we calculate a middle value, 
if our target is greater than the middle value we move our left pointer to m + 1 position (right partition).
if our target is less than the middle value we move our right pointer to the m - 1 position (left partition).
if our target equals our middle position we save that index to i.
our biasing now comes in handy, if we want the leftmost appearance, we will continue to search by moving our right pointer to m - 1.
this partitions our array further allowing us to keep search left incase there is an instance of our target further left.
if our we want the rightmost appearance, we shift our left pointer to m + 1 and search right based on the same premise.
our bias variable essentially tells us which way we will continue to partition and search.
once our pointers cross we can return our index variable.
we run this for the left and right index of our result, only changing the passed in bias variable and return that result.
this solution runs in O(log n) logarithmic time.
"""