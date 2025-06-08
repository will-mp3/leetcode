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
this soltuion uses depth first search to go order oyur naumbers.
we loop through numbers in range 1 - 9 if n is 10 or larger and 1 - n if n is small.
each time we add the number to result and call dfs on the number.
our dfs function then raises it a power of ten and loops through numbers 1 - 9.
each time we check if our new number plus i is greater less than or equal to n.
if it is we append our new number plus i and call dfs on it.
this searches a tree that visits 1, 10, 100, 1000 etc first before checking 1001, 1002, etc.
"""