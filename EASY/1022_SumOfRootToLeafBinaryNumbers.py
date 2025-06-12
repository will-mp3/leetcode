"""
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        
        def dfs(node, num):
            
            if not node:
                return
            
            num = num + str(node.val)
            
            if not node.left and not node.right:
                res.append(num)
            
            dfs(node.left, num)
            dfs(node.right, num)
            
            return
        
        dfs(root, '')
        print(res)
        
        val = 0
        for num in res:
            val += int(num, 2)
        return val

"""
for this problem we use depth first search to traverse the tree.
each new node we check if it exists, if not we return (base case).
if the node exists we append the string value of the node to our num string.
we then check if there are any children, if not the binary string is complete and we can add it to our result list.
we then call dfs on its children.
at the end for go through each string num in our result array and add its integer value to val.
we use int(num, 2) to transform binary values to base 2.
"""