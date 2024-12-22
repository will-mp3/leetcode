"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None


"""
to solve this problem we make use of recursive depth first search.
the problem insists we create a clone of a connected graph, meaning we need to remake all of its contents and their connections.
to do this we use a recursive function dfs() and a has table.
this function starts at a given node and first checks if we have already cloned it, if we have return it from the hash table.
if not, we make a new node called copy with the given nodes value.
next we go through the given nodes neighbors and append them to copy.
we do this recursively, so once called the neighbor node goes through the same process while also being added to the first nodes neighbors.
once all neighbors have been copied (the graph has all its nodes), the recursive function pops back to the original node we passed in.
along the way the connection to the neighbors is appended for every recursive instance.
in order: node is created, node creates a neighbor and connects to it, neighbor creates its neighbors and connects to them,
        first node is encountered (saved in the hash table), recursive function pops connecting the neighbors in the opposite direction.
this solution runs in O(n) linear time. 
"""