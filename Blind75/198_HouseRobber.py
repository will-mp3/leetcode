"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

"""
this problem can by solved using dynamic programming.
this ghist is that we cannot rob adjacent houses, and must find the maximum amount we can rob in one night (values stored).
to solve this, we make use of two pointers, rob1 and rob2, which are two previous max possible values.
rob1 is the previous-previous max, and rob2 is the adjacent previous max of the current house (n).
ex: [rob1, rob2, n, n+1, ...]
rob1 is the max you would compute with n (n + rob1) and rob2 is the max should you opt not to rob the current house (n).
as the loop executes rob1 becomes rob2 and rob2 is updated with the temp value which evaluates any growth.
this solution runs in O(n) linear time.
"""