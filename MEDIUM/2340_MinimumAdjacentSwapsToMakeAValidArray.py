"""
You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.
"""

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minNum, maxNum = min(nums), max(nums) # get min and max values
        minI = nums.index(minNum) # search left for min index
        
        nums = [nums[minI]] + nums[:minI] + nums[minI + 1:] # swap and update nums

        maxI = nums[::-1].index(maxNum) # search right for max index
        # nums[::-1] reverses the array, start and stop are omitted and step is backwards by 1

        return minI + maxI

"""
like most swap algorithms, we will take a greedy approach to find our solution.
when analyzing the problem, we see that the solution we're looking to return is really just the sum of two indexes.
we need the index of our minimum value, closest from the left, and the index of our maximum value, closest from the right.
for this right index, a more appropriate description would be distance from the right so we will use its reverse distance.
to start, we find our min and max values using the min and max function.
next we search our array starting from the left (default) and find the index of our minimum value.
we then take this value and shift it to the front, we update nums to be the minimum value, everything before it, and everything after it.
we then search our array from the right to find our maximum value.
to do this effectively, we reverse our array and search as we did for the left value.
this method of searching gets us that distance we were looking for while avoiding 
"""