"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))

        pre = 1
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]
    
        return result

"""
the first thing to consider when solving this problem are the specific parameters given at the bottom:
we must solve this problem in O(n) time and cannot use the division operator.
to start we initialize our output array result.
there are two loops in this solution:
one going through and storing the prefix value in result[i] and then recalculating the prefix value with nums[i]
and another going through and multiplying the stored prefix from before with the current postfix value and then recaluating that like above.
what this does is multiplie all the before values (prefix) and after values (postfix) of i together and stores them in the result[i] slot.
this solution runs in O(n) linear time.
"""