"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i): # i is the index of the value we are making a decision on
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # two decisions
            # decision to include nums[i], left branch of decision tree
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

"""

"""