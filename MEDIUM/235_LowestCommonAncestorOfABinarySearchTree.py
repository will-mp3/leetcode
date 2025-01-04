"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else: # split occurs or cur equals p or q
                return cur

"""
this problem tasks us with finding the lowest common ancestor for two nodes p and q.
the lowest common ancestor is the node farthest down the tree from which both p and q can still be reached.
conditions for a node to be the LCA are if p and q split at this node OR this node is equal to p or q.
to solve this problem we simply go down the tree until p and q split or equal the current node.
once we reach one of those conditions we return the node.
this solution runs in O(logn).
"""