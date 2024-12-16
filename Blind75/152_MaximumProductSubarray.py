"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n) # bugfix to avoid a change in curMax affecting the min
            res = max(res, curMax)
        return res

"""
when considering this problem the first thing to consider are all the possible patterns.
the array can consist of all positive numbers, all negative numbers, or a mix of both.
The most complicated is the array of all negative numbers.
because of this, we not only need to keep track of the max subbaray but the current max subarray and the current minimum subarray.
to start we begin looping through the list, our first bit of logic is handling the zero case.
we then calculate the current max and current min by comparing: 
n * curMax (for when n is poitive), n * curMin (for when n is negative), and n (for when n is larger than the current max).
note the temp variable to account for the potential change in curMax
compare the saved max subarray (res) with the current max.
this solution runs in O(n) linear time.
"""