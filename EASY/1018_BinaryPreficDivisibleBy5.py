"""
You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
"""

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        for i in range(len(nums)):
            val = ((val << 1) + nums[i]) % 5
            nums[i] = val == 0
        return nums

"""
This solution iterates through the binary array nums, maintaining a running value val that represents the decimal equivalent of the binary number formed by the subarray nums[0..i]. 
For each bit in the array, it shifts the current value left by one (equivalent to multiplying by 2) and adds the current bit. 
To prevent overflow and keep the computation efficient, it takes the modulo 5 of the value at each step. 
Finally, it checks if the current value is divisible by 5 and updates the nums array with boolean values accordingly, which is returned at the end.
"""