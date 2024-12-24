"""
You have a graph of n nodes labeled from 0 to n - 1. 
You are given an integer n and a list of edges where edges[i] = [ai, bi] 
indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True # empty graph is a valid graph
        
        # adjacency list
        adj = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)

"""
to solve this problem we must first understand what a valid tree looks like.
for our purposes a valid tree is where all of the given nodes are 1. connected and 2. void of any loops.
this solution works by using a hast table adjacency list to first map all the nodes and their connections.
using this alongside a set to track visited nodes we create a depth first search function to check the following conditions:
if the node has been visited return false, loop detected.
if not, add the node to visit and then check its neighbors.
if the neighbor is the previous node, prev, skip over it.
call the dfs function once more, this time on the current neighbor of node i using i now as the previous node.
if this returns false ever then the graph is not valid, if it returns true then we have one more condition to check.
in our return statement we must check if our dfs function returns true AND the visited nodes equal n.
if both of the cases are true (no loops and no unconnected nodes) then we can return true.
this solution runs in O(edges + vertices) ~linear time.
"""