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
to solve this problem we use a depth first search algorithm to search the entire tree.
we use the logic of, for each root node checked, if the target values are in the left and right subtrees, return the root as LCA.
if the target values are in either the left or the right subtree, meaning one tree returned a value and one returned null, 
return the target found as the LCA.
we see this in our code as having our base case when the root/current node equals a target, return it.
if thats not the case we search the left and right subtrees.
based on the return value we know what to pass up the stack as the LCA.
if targets are found in left and right, l and r are not null, return the root/current node.
if l is not null and r is, return the l value as our LCA and vice versa for r.
"""