"""
You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return True if goal == 0 else False

"""
this problem is actually rather simple to solve and does not require any dfs or dynamic programming.
the approach above starts at the last index, the starting goal.
from here we check each index moving backward until we get to index zero.
the way this works is the goal marker moves from spot to spot depending on if that index can reach the current goal.
if the goal marker is able to make it to index zero (goal == 0) then we know that there is a path from start to finish.
this solution runs in O(n) linear time.
"""