"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        # if the above case does not activate then we know that both nodes are non-empty and have equal values
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

"""

"""