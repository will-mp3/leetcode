"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res

"""
solving this problem is rather straightforward.
given an array [0, 2, 3] we are given 3 distinct numbers in a range of 0 to 3.
the full size array for this would be [0, 1, 2, 3] and we must find that the 1 is missing.
to do this we simply take the sum of each array and find the difference.
this is done by setting our result value first equal to the length of nums, in this case 3.
we iterate through nums, each time adding the value of i (this will add 0, 1, 2) and subtracting the values in nums.
this allows for result to have all four values added, and all three values in nums subtracted, leaving the remainder behind.
this solution runs in O(n) linear time and has a space complexity of O(1).
"""