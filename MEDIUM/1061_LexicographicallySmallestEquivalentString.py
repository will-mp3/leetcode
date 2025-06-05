"""
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", 
and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
"""

from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # make a dictionary of list type
        adj = defaultdict(list)

        # create the adjacency list
        for a, b in zip(s1, s2):
            adj[a].append(b)
            adj[b].append(a)

        def dfs(char, visited):
            visited.add(char)
            curMin = char
            for neighbor in adj[char]:
                if neighbor not in visited:
                    # find the smallest character in each neighbors tree (including the neighbor) and compare that with the current character
                    candidate = dfs(neighbor, visited)
                    curMin = min(curMin, candidate)
            return curMin

        res = []
        for char in baseStr:
            visited = set() # resets with each char, avoids repeated work in the same search
            res.append(dfs(char, visited))
        
        return ''.join(res)

"""

"""