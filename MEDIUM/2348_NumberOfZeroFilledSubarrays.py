"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, zeros = 0, 0

        for num in nums:
            if num == 0:
                res += zeros + 1
                zeros += 1
            else:
                zeros = 0
        
        return res

"""
This code defines a solution to count the number of contiguous subarrays filled with zeros in a given integer array nums.
The `zeroFilledSubarray` method initializes two variables: `res` to store the total count of zero-filled subarrays and `zeros` to count consecutive zeros. 
It iterates through each number in the nums array. If the number is zero, it increments `res` by the current count of consecutive zeros plus one (to account for the new zero) and increments the `zeros` counter. 
If the number is not zero, it resets the `zeros` counter to zero. Finally, it returns the total count of zero-filled subarrays.
The time complexity of this solution is O(n), where n is the length of the nums array, as it processes each element exactly once.
"""