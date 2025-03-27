"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        
        return dfs(root, root.val)

"""
for this problem, like many binary tree problems, we will make use of a recursive depth first search algorithm.
the problem asks us to count the number of good nodes in the tree, requiring us to scan through all of the nodes in the tree by default.
we obviously can use dfs to accomplish this, but we need some extra variables in order to evaluate each node.
in order to check if a node is "good" we will keep track of a maxVal variable.
maxVal represents the largest value seen in the current branch we are traversing.
this will allow us to check each node to see if it qualifies as being good (no nodes in its path greater than itself).
we create our dfs function and pass in the current node as well as the current max value for the branch.
our base case is when our node is Null, in which we return zero.
the first thing we do is check if the node is good or not, if it is we set our result variable to 1, otherwise set it to 0.
this result variable is ultimately what we return, either 1 or 0 as a recursive incrementer.
once we set result we can update our max value based on the current node and call dfs on the left and right children.
once the recursive stack begins to pop, we return result and increment the result variables still in the stack (see dfs call).
this solution runs in O(n) linear time.
"""