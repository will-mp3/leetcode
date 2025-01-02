"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return max path sum without splitting
        def dfs(root):
            if not root: # no node, root is null
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # we want to leave out negative values
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # comput max path WITHOUT split
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

"""

"""