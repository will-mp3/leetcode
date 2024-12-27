"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
     res = []

     def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

     dfs(0, [], 0)
     return res

"""
this problem makes use of recursion in its solution.
the issue we run into when solving is not the base problem but rather the no dupplicate combinations.
to account for this, instead of a brute force DFS going through every option, we instead use recursion and two options.
for each value in candidates, we are given a choice to either use that value or use the next value.
if we started at 2, the entire leftmost branch system would be [2, 2, 2, ...].
this allows for us to never have more than one combination of any amount of the values in our list.
this could look like:
candidates = [2, 3, 4]
2 -> [2],[] ; [2] -> [2, 2] [3] ; [2, 2] -> [2, 2, 2] [2, 2, 3] and so on. (this represents the leftmost branch.)
these decisions are exemplified by the two dfs calls at the bottom of the recursive function.
this solution runs in O(2^t) where t is our target value.
"""