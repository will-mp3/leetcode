"""
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.
"""

class Solution:
    def numTrees(self, n: int) -> int:
        """
        numTree[4] = numTree[0] * numTree[3] + 
                     numTree[1] * numTree[2] +
                     numTree[2] * numTree[1] +
                     numTree[3] * numTree[0]
        """
        numTree = [1] * (n + 1)

        # 0 nodes = 1 tree
        # 1 node = 1 tree
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]

"""
this problem makes use of dynamic programming to find its solution.
we break this problem down into smaller pieces by examining the amount of trees depending on our root node.
for example, if n was equal to 4 we could find this by adding up all of the combinations of trees that came before.
if our first value is the root we know our left subtree has zero nodes and right subtree has three nodes, and so on.
using this knowledge and our two given cases where 0 nodes is 1 tree (empty tree) and 1 node is 1 tree, 
we calculate the amount of trees for each node count, starting at 2 since 0 and 1 are accounted for.
because we use dynamic programming we can use the values stored in our numTree array to do all the calculations.
as we go through our array we continue to update each position until we get to position n.
position n holds the total number of possible trees so we can return numTree[n].
"""