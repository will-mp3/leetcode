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
this problem is similar to the original permutations question, except this time our input array may contain duplicates.
this prevents us from backtracking using a standard decision tree like in the first version of the problem.
we still use the backtracking technique and a recursive dfs function, but there is required preprocessing.
namely, we must turn our input array into a hashmap of unique numbers and their respective counts.
this allows us to both avoid duplicate decisions and ensure all values are included in our permutations.
once the reprocessing is done we call our depth first search function which is imbedded.
the way this works is by first checking the base case, if the current permutation (perm) is equal in length to our input array.
if this is true we append a copy and return.
if our base case does not execute we then iterate through all our values in count.
for each value n whose count is greater than zero we append n to our current permuation, decrement count, and call our dfs function again.
this process repeats until the recrusive stack is popped and then we cleanup by reincrementing count and popping the added n (for each call).
once the recrusion is finishing we return the result.
"""