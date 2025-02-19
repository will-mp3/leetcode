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
to solve this problem we will use the backtracking technique with a recursive depth first search function.
we have an added helper function used to determine if a set of values is a palindrome as well.
it works by shifting and checking left and right pointers, very simple.
our main function works as follows:
we start by creating a result array and a partition array, the partition array will hold the current partition to potentialy be added to res.
our dfs function works by first checking the base case, if we get to a value i (the current index) that is equal to the length of s,
we know we have reached the end of the input string s and used all its characters.
from here we can append the partition and continue.
if the base case does not execute then we go through the remaining characters in our input string s ranging from current index i to j.
we check to see if the string from i to j is a palindrome using our helper variable, if true we continue otherwise move on to the next cycle.
if true, append the string from i to j + 1 to our current partition array and call our dfs function starting at j + 1.
to cleanup we simply pop the most recent value from our partition.
"""