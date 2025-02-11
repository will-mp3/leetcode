"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # solve using recursion
        # base case
        if (len(nums) == 1):
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0) # pop the value at the 0 index and save it to n
            perms = self.permute(nums)

            # once the call stack starts returning, begin appending the popped value n
            for perm in perms:
                perm.append(n)
            
            # add all of the elements to result
            result.extend(perms)
            
            # add the removed element back
            nums.append(n)
        
        return result

"""

"""