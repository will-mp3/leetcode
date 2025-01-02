"""
Given the root of a binary tree, invert the tree, and return its root.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

"""
to solve this problem we use a recursive depth first search method.
we break the problem into pieces, essentially dealing with only three nodes at a time, the root and its children.
we go through, starting at the top, and swap the left and right children of the root, 
then call the same method on the same left and right children, ending once the root is Null (end of tree)
once we're finished we return the root.
this solution runs in O(n) linear time.
"""