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
this problem expands upon simple tree traversal, we use the same method of recursive depth first search to solve.
we start by checking our base cases, if the nodes are both empty we return true by default and if the nodes are not equal we return false.
if neither of these execute we go to our recursive step which is calling this same function on the left and right children of the current nodes.
ultimately we want our function to return True if they match and if they every dont match the function will evealuate to False.
"""