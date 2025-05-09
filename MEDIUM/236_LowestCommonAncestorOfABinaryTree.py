"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

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
        # edge case, not applicable but good practice
        if not root:
            return None

        # if our root is one of our targets, return root
        if root == p or root == q:
            return root

        # dfs on the left and right subtrees, looking to find targets on the right and left
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # targets are on different subtrees, neither target is the LCA
        if l and r:
            return root
        # both targets are on left subtree, return the first one found as LCA
        elif l:
            return l
        # both targets are on right subtree, return the first one found as LCA
        else:
            return r

"""

"""