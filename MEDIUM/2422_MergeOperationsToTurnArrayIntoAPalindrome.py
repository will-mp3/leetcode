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
this problem requires us to perform merges in order to convert an array of ints into a palindrome.
unlike traditional palindrome problems where we would go move out from the center, we will start on the edges.
using a left and right pointer, intialized at the start and end of our array, we check to see if l and r are equal.
if they are not equal, we evaluate the sign and merge the smaller value since merging can only increase.
if left is greater than right, we know we have to merge the right values and increment res.
we save the current r value in a tmp variable, then decrement r and add the new r value with our tmp variable.
if left is less than right, we merge left values and increment res.
we save the current l value in a tmp variable, then increment l and add the new l value with our tmp variable.
if left and right are equal then we perform both of the above operations without incrementing our result.
this solution runs in O(n) linear time.
"""