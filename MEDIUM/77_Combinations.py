"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(curr, first):
            # if our current combination is of length k, add it to our result array
            if len(curr) == k:
                ans.append(curr[:])
                return

            # for every value after (larger) then our current starting value, create a new combination
            for num in range(first, n + 1):
                curr.append(num)
                dfs(curr, num + 1) # once made, pass the combo into a new recursive call
                curr.pop() # remove the new number and repeat for the next number

        ans = []
        dfs([], 1)
        return ans

"""
this solution makes use of backtracking to gather all possible combinations based on our constraint k.
we create a depth first search function as though we are traversing a tree and apply a base case when our current combinations is length k.
the general idea is that for each value 1 through n we are creating every possible combination with the values larger than itself.
we are able to use only larger values because we dont want duplicates, for example 1 will always have more combos than 2 in its tree etc.
the recursion works using a current combination array and appends new values, calls dfs to check our base case, and pops after.
of course this creates that recursive stack we are used to but ultimately the stack will pop and we will move to the next value at index 0.
"""