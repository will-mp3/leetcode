"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

"""
to solve this problem most efficiently we use a recursive depth first search function.
in fact, we dont even need to create a new function as we can use the one given to use.
all we do is first check the edge case for when there is no root (empty tree).
then we return 1 + the max of this same function on our (potential) two leaf nodes.
how it works is we continue to go down the tree as long as a leaf node exists somewhere and repeatedly add 1 when thats the case.
this solution runs in O(n) linear time.
"""