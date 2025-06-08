"""
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
"""

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(num):
            newNum = num * 10

            for i in range(10):
                if newNum + i <= n: 
                    res.append(newNum + i)   
                    dfs(newNum + i)
                    
        for i in range(1, 10 if n >= 10 else n + 1):
            res.append(i)
            dfs(i)
        
        return res

"""

"""