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
to solve this problem we will use a helper function sameTree.
we break this problem into to sub problems, one to check and traverse subtrees, and one to check if two trees are equal.
lets start with the latter, sameTree.
the way this function works is by first checking if both trees are empty, returning True if so.
after that edge case, we check if both roots are non-empty and if they are equal, our primary conditional.
if this is the case, we return the AND operation of this same function called on the root and subRoots children.
this goes through the trees in their entirety, until they reach null nodes (tree is exhausted) and returns True if they are the same 
or returns False at any point they are found to be different.
our last condition is if neither of the above are true, essentially stating that the roots are equal in some respect, and we return False.
our main function is Subtree uses this function in its logic.
the way this function works if by checking first if the subroot is null, this would gurantee its a subtree of any tree.
we next check if our main tree is null, this would gurantee there cant be a subtree since we know by now our subRoot is not null.
we next call our sameTree function to check if the trees are equal at this point, if they are (sameTree returns True) we return True.
otherwise, we call isSubtree again, this time using OR logic on the left and right children.
this recursively checks the rest of the tree, repeating the above logic for all the subtrees in root.
"""