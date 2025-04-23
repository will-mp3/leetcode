"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(curr, first):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for num in range(first, n + 1):
                curr.append(num)
                dfs(curr, num + 1)
                curr.pop()

        ans = []
        dfs([], 1)
        return ans

"""

"""