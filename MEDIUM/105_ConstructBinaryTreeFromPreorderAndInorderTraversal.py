"""
Given two integer arrays preorder and inorder 
where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) # first value in preorder is always the root
        mid = inorder.index(preorder[0]) # sets out middle position, dividing nodes on the left and right of the root
        # create sublists
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) # every value from index 1 to mid for preoder, every value from the beginning to mid for inorder (draw picture if lost)
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) # every value from mid + 1 onward for preorder, every value from mid + 1 onward for inorder

        return root

"""

"""