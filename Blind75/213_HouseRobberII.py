"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

"""
this problem is quite simple to solve if you understand house robber 1 (198).
the nly difference is that the first and last house are adjacent.
to account for this we add the original code from house robber 1 as a helper variable.
we use this helper variable on the array skipping the first house (nums[1:]) and skipping the last house (nums[:-1]).
we then take the max of these two values as well as the value of an single-variable array.
this solution runs in O(n) linear time.
"""