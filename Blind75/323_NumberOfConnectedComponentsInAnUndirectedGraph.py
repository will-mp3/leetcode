"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] 
indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        # function to find parent node
        def find(n1):
            res = n1 # initially itself
            while res != par[res]:
                par[res] = par[par[res]] # optimization to shorten linked list
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0 # no union

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res

"""
the algorithm this solution will use is called union find, we could approach this problem using a visit set and a depth first search,
but union find was made specifically for finding connected sets.

"""