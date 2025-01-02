"""
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        # loop to go through every node of a given level
        while q:
            qLen = len(q)
            level = [] # array for current level values
            for i in range(qLen):
                node = q.popleft() 
                if node:
                    level.append(node.val) # add node to our level array
                    # add nodes children to our queue
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res

"""

"""