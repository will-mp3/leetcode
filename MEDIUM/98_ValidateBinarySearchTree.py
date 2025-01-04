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
this problem tasks us with checking to see if a tree is valid or not, i.e. is it correctly balanced.
to do this we use a recurisve depth first search approach.
our logic is based on a recursive helper function which utilizes left and right boundaries to check validity.
each time the function is called it checks if the node is between the left and right boundaries passed in.
if it is, the function continues calling itself.
our boundaries start at negative and positive infinity, and update as we call the function.
when we traverse left, we keep our left boundary the same and update our right boundary to be the parents value.
this is because we must be less than the parent value but our minimum will remain the same.
when we traverse right we do the opposite, since we must be greater than the parent value and our maximum does not change.
this logic continues with every child until the tree is proven invalid or runs to completion.
this solution runs in O(n) linear time.
"""