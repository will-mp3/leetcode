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
for this problem we are tasked with recreating a tree using its inorder and preorder traversals.
we tackle this problem recursively using just one pointer and some array manipulation.
we will use preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] as our example inputs.
to solve this problem we start by creating the root of the tree, that will always be the first value in a preorder array.
next we get our mid pointer, we use this to divide the arrays into left and right subarrays, symbolizing left and right sides of the tree.
the node creation happens when we make our root node, so once we have that and mid we call the buildTree function again.
the mid pointer is used here to divide our arrays into smaller subarrays.
here our mid value is 1. 
using that we call buildTree on the left, passing just [9] as our preorder (index 1 to mid + 1) and [9] again for our inorder (index 0 to mid).
we do the same thing on the right, this time passing [20, 15, 7] as preorder (mid + 1 onward) and [15, 20, 7] as our inorder (mid + 1 onward).
you notice that our values for inorder and preorder are the same, just in a different order.
that is because they contain all of the values in that side of the remaining tree.
our buildTree function uses these values until the tree is empty to construct the tree and then returns root back to the top. 
"""