"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [] # store list of permutations
        perm = [] # list ot store each permutation
        count = { n:0 for n in nums } # count hashmap mapping every n in nums with its count
        for n in nums:
            count[n] += 1
        
        def dfs():
            # base case
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    # recurse
                    dfs()
                    # cleanup
                    count[n] += 1
                    perm.pop()
    
        dfs()
        return res

"""

"""