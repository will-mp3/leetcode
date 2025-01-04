"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            
            # check if node isnt between left and right boundaries
            if not (node.val < right and node.val > left):
                return False

            # going left, left boundary stays the same, right boundary updates to parent value
            # going right, right boundary stays the same and left boundary updates to parent value
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))

"""

"""