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

"""