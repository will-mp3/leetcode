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
to solve this problem, we utilize breadth first search.
to implement this algorithm, we utilize a queue.
we start by adding the root to our queue, this initializes it and allows us to start our looping algorithm.
while the queue is not empty, taken the current length and create an array level to hold the nodes at this current level.
with our queue length, iterate through that many times, each time popping the left value and adding it to our level array.
we all add our left and right children to our queue, maintaining the loop.
lastly we add the level array to our result array and continue the loop.
each iteration we update the length and reset the level array.
what this is doing is taking each node for each level and storing them as a list in an array.
once our queue is empty we know we have searched every node and are done.
by the end our result array will hold all of our node lists.
this solution runs in O(n) linear time.
""" 