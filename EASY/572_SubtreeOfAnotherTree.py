"""
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: # subroot is null, always a subtree
            return True
        if not root: # root is null and subRoot is not, pay attention to order of conditions.
            return False
        
        if self.sameTree(root, subRoot): # current tree is equal to subtree.
            return True
        
        # if current tree is not equal to subtree, check the subtrees of our current tree
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))

        
    def sameTree(self, root, subRoot):
        # s = root, t = subroot
        if not root and not subRoot: # both trees empty, return true
            return True
        if root and subRoot and root.val == subRoot.val: # current nodes values are equal, check the rest of their leaves
            return(self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        return False

"""

"""