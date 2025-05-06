"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root] if root else []) # add root if not null

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft() # get our node
                level.append(node.val) # add node value to level array

                # get children and add to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level = list(reversed(level)) if len(res) % 2 else level # reverse on odd levels
            res.append(level)

        return res

"""

"""