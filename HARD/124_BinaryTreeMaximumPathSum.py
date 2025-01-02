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
this solution makes use of a recursive depth first search algorithm.
its important to note we are looking for paths, meaning there can be no branches.
this could either contain just one side of the tree or a single split, but no more than one split may be included.
the way it works if our recursive function, which receives a node (starting at the root), searches all the nodes in the tree for their values.
the function is called all the way down the tree, where we begin computing the maximum value.
our max is stored in our global variable res[], 
and each time our function is called we calculate the max value of our node with or without a split.
we update result so see if our max path includes this node as our pivot (the path splits on this node), 
and if not we return our roots value plus the max path (left or right).
this continues until we've checked every position.
ultimately, we will have checked every node as a pivot point (split) and as a path, finding the maximum path overall by combining these pieces.
note we handle negative numbers by zeroing them, this equates to excluding them all together.
this solution runs in O(n) linear time.
"""