"""
You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones: return n - ones
        
        res = inf
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    res = min(res, j - i)

        if res == inf: return -1
        return res + n - 1

"""
This solution first checks if there are any 1's in the array. 
If there are, it calculates the minimum number of operations needed to make all elements equal to 1 by subtracting the count of 1's from the total length of the array. 
If there are no 1's, it iterates through all possible subarrays to find the shortest
"""