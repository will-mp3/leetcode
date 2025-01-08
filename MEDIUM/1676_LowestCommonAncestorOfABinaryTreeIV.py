"""
Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. 
All the nodes will exist in the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: 
"The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant 
(where we allow a node to be a descendant of itself) for every valid i". 
A descendant of a node x is a node y that is on the path from node x to some leaf node.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # set to check if current node is a target node
        # once a target node is encountered, we know we dont need to go any lower
        target = set(nodes)

        # dfs function to traverse the tree and search for target nodes
        def dfs(root):
            # if root is a target node, return root node to be saved
            if root in target:
                return root

            # if root is null, return null. for end of tree and edge case handling
            if not root:
                return None
            
            # if node is not a target and is not null, we call dfs on our left and right children
            # the goal of this if to find the earliest left and right target nodes
            # once the dfs function for both left and right finish, we will know our LCA
            left = dfs(root.left)
            right = dfs(root.right)

            # if both left and right contain a node, we know the current root is the LCA, it has two target children
            if left and right:
                return root
            # if only left contains a node, we know that either left is the only target node or all target nodes are beneath it
            if left and not right:
                return left
            # if only right contains a node, we know that either right is the only target node or all target nodes are beneath it 
            if right and not left:
                return right
            
            return None

"""

"""