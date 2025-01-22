"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        nextl = deque(
            [
                root,
            ]
        )
        rightside = []

        while nextl:
            cur = nextl
            nextl = deque()

            while cur:
                node = cur.popleft()

                # add child nodes of the current level in the queue for next
                if node.left:
                    nextl.append(node.left)
                if node.right:
                    nextl.append(node.right)
                
            # current level is finished, its last element is the rightmost node
            rightside.append(node.val)
        
        return rightside

"""
to solve this problem we make use of an iterative breadth first search algorithm, specifically using two queues.
the way the algorithm works is we maintain two queues to represent the current and next level of our tree.
as we go through our current queue, we add its children to the next queue.
once we get to the last value of the current queue we know thats the rightmost node and we can append its value to our rightside array.
each iteration we set our current queue to next, and create a new empty queue for next.
we go through cur and add all the children until its empty then append that last node and repeat.
this process contoinues until next is null signalling the end of the tree.
this solution runs in O(n) linear time.
"""