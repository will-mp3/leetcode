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
this questions asks us to find the kth smallest integer of a binary search tree.
luckily, there is a traversal method that puts all our values in order, namely in-order traversal (obviously).
this is an easy thing to implement using recursion, but for the sake of practice we will do the iterative solution instead.
to start, we initiliaze our count variable n (which we will compare to k), our stack, and set our current node to the root node.
while our tree still has nodes or our stack still have values we loop.
each iteration we hit another loop that runs until cur is null, within we add cur to our stack and update cur to its left child.
once this loop breaks we know we've hit the bottom of our leftmost traversal.
we pop the stack to update cur, add 1 to n, and check if n is equal to k.
if n and k are equal, we can return the value of cur, otherwise we set cur to its right value and repeat this logic.
this loop will completely search the tree using in order traversal.
this solution runs in O(n) linear time.
"""