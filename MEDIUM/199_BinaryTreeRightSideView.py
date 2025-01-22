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

"""