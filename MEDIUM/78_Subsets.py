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
this solution makes use of the backtracking technique and a depth first search algorithm.
the reason we use dfs is because we are approaching this problem in a binary decision tree manner.
we build our subsets based on two decisions, the left path adds nums[i] to the current subset and the right path adds nothing.
this is exemplified in our dfs function.
our function works by first checking our base case, if i (the index of the value in nums) is out of bounds,
we append the current subset to result and return.
we are given two decisions to make, the first being to add nums[i] to our subset.
for this decision we append nums[i] to subset and call our dfs function incrementing i.
for the decision not to include nums[i], we pop the just added nums[i] and call dfs incrementing i as well.
we start by calling dfs with i set to zero, once the recursion has completed we return our result.
"""