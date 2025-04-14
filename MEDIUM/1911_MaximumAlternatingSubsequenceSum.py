"""
The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) 
without changing the remaining elements' relative order. 
For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.
"""

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # sumAdd -> first value in subsequence was added
        # sumSubtract -> first value in subsequence was subtracted
        sumAdd, sumSubtract = 0, 0 # current maxes

        for i in range(len(nums) - 1, -1, -1):
            # compute maximum if we are adding
            tmpAdd = max(sumSubtract + nums[i], sumAdd)

            # compute maximum if we are subtracting
            tmpSubtract = max(sumAdd - nums[i], sumSubtract)

            sumAdd, sumSubtract = tmpAdd, tmpSubtract # new maxes

        return max(sumAdd, sumSubtract)

"""
this solution makes use of a dynamic programming technique to avoid the use of extra memory in a dp array/hashmap.
we start from the end of our array nums and work our way to the front, just like any bottom up dynamic programming algorithm.
we keep track of two variables, sumAdd and sumSubtract, which represent the current maximum alternating subsequence.
the difference between them is essentially if we choose to add or subtract the first value of our sequence.
having both of these allows us to "checkerboard" the whole array ensuring every combination is tested.
we start at the end of our array and update two temporary variables.
our tmpAdd variable is updated with the max of our current sumAdd and the value we would get should we add the current value at index i.
our tmpSubtract variable is updated with the max of our current sumSubtract variable and the value if we subtracted the current value.
our two global variable are then updated with the temporary ones (which hold the new maxes) and our loop continues.
once the loop completes we return the max of our global variables.
this solution runs in O(n) linear time and has O(1) memory usage.
"""