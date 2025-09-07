"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return res

"""
This code defines a solution to perform an inorder traversal of a binary tree and return the values of its nodes in a list. The function `inorderTraversal` takes the root of the binary tree as input and returns a list of integers representing the inorder traversal.
The method initializes an empty list `res` to store the values of the nodes during the traversal. It defines a nested helper function `dfs` (depth-first search) that performs the actual traversal.
The `dfs` function takes a node `root` as input. If the node is `None`, it returns immediately, effectively handling the base case of the recursion. If the node is not `None`, it recursively calls itself on the left child of the node, appends the value of the current node to the `res` list, and then recursively calls itself on the right child of the node. This order of operations ensures that the left subtree is processed first, followed by the current node, and finally the right subtree, which is characteristic of inorder traversal.
After defining the `dfs` function, the method calls it with the initial `root` node to start the traversal. Finally, it returns the `res` list containing the values of the nodes in inorder sequence.
The time complexity of this solution is O(n), where n is the number of nodes in the binary tree, as each node is visited exactly once. The space complexity is O(h), where h is the height of the tree, due to the recursion stack used during the depth-first search. In the worst case, the height of the tree can be equal to the number of nodes (O(n)) for a skewed tree, but for a balanced tree, the height would be O(log n).
"""