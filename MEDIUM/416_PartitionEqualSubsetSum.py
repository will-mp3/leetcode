"""
Given an integer array nums, 
return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0) # base case, guranteed sum of zero
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            # cant update set while we iterate through it, create dummy set nextDP
            nextDP = set()
            for t in dp:
                # check if target is found
                if (t + nums[i]) == target:
                    return True
                # add every value in dp and every value + nums[i] to nextDP
                nextDP.add(t)
                nextDP.add(t + nums[i])
            # update dp
            dp = nextDP
        
        return True if target in dp else False

"""

"""