"""
You are given an array nums consisting of positive integers.

You can perform the following operation on the array any number of times:

Choose any two adjacent elements and replace them with their sum.
For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].
Return the minimum number of operations needed to turn the array into a palindrome.
"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 0

        while l < r:
            if nums[l] > nums[r]:
                tmp = nums[r]
                r -= 1
                nums[r] += tmp
                res += 1
            elif nums[l] < nums[r]:
                tmp = nums[l]
                l += 1
                nums[l] += tmp
                res += 1
            else:
                tmp = nums[l]
                l += 1
                nums[l] += tmp
                tmp = nums[r]
                r -= 1
                nums[r] += tmp

        return res

"""

"""