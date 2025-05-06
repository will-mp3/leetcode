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
this problem follows a simple breadth first search with a minor twist at the end.
like any bfs we approach this with a queue.
while our queue is not empty we build our level, iterating based on the current length of the queue (nodes to be added to this level).
we popleft to get the leftmost node, add it to level, then check our nodes children and add them to the queue.
this goes through the entire level, fills up the nodes for the next level, then adds the current level to our result.
the twist is when we are on an odd level we reverse our list.
to do this we just mod the length of our result, if length is odd we know to reverse the list.
"""