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
the way this code works is first we declare two arrays, one of the parent nodes (which start initially as themselves)
and one with the rank of the nodes.
the rank arrays purpose is to track essentially how many nodes a parent has connected to it and allow for future connections.
this is purely for optimization and makes our nodes into more of a tree shape than a list.
once these arrays are created we create two methods, find and union.
the purpose of find is to search for a parent node, once found its returned.
using passed in edges, this will search for the parent nodes of all nodes and return them, useful in the next function.
the purpose of union is to perform the actual union of nodes and return 1 once finished.
find is run on the edge passed in and checks if the parent is different.
if the parent is the same, no union is needed and zero is returned.
if the parent are different, union is carried out based on rank and 1 is returned.
the values serve to decrement our result, starting at n, by 1 with each union.
"""