"""
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack: # while cur is not null and stack in nonempty
            while cur: # go left until null
                stack.append(cur)
                cur = cur.left

            cur = stack.pop() # process value
            n += 1
            if n == k:
                return cur.val

            cur = cur.right

"""

"""