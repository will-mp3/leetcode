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
this problem requires an adjacency list for its solution, we pair this with a depth first search algorithm.
if transitivity was not an included rule, we could simply take the min of the neighbors for each character in baseStr.
however due to the inclyusion of transitivyt we have to find the min of our neighbors neighbors to ensure our solution is correct.
now if we change the word neighbor to children its obvious we cna use dfs to traverse our entire adj list.
we start by making our adj list, which is a dictionary of listy type.
we fill it in mapping characters in s1 to s2 and vice versa.
for each character in baseStr we add the result of our dfs function.
our dfs function takes in the current char as well as a fresh visited set with each char in baseStr.
our dfs first adds the passed char to visited and sets it to the current min since we will be looking down from here on.
we call dfs on every unvisited neighbor of our current char.
once that recurisve stack pops up to the current level, we compare the found minimum with our current minimum.
our base case is when every neighbor of the current node has been visited, in which we just return the current char.
this well effectively min compare every connected character to our passed in character.
"""