"""
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = [] # current partition

        def dfs(i):
            # base case
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                # check if palindrome using helper function
                if self.isPali(s, i, j): # if palindrome, add to res. otherwise skip to next iteration
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    #cleanup
                    part.pop()
        
        dfs(0)
        return res
        
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

"""

"""