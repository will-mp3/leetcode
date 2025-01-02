"""
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later 
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = [] # will join with comma delimiter later

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            # pre-order traversal
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()

"""
this solution is broken up into two functions, one that serializes a tree and one that deserializes.
all this basically means is one encodes a tree into a string and one turns that string back into the original tree.
our serialize function is the most simple, the basis is we are serializing our tree by using null leaves as our condition.
we set these equal to "N" and return our dfs function when a null leaf is ecountered.
our dfs function appends the value at non null nodes to our result array and then calls the dfs recursively on its two children.
we go about this using depth first search and preorder traversal, so we start with the left side and then go to the right.
our result array could look something like [1, 2, N, N, 3, 4, N, N, 5, N, N] where nodes 2, 4, and 5 have no children.
our deserialize function uses the same depth first search and preorder approach to tranform this string.
the first thing we do is strip the commas from our string, turning it into an ununterrupted string of characters.
once thats done we call our recursive depth first search function, this uses the saved N characters as a condition to return.
if an N isnt encountered we make a new node using the current character valuse and call dfs on its children.
similarly to above we call left first since it needs to be decoded in a preorder manner.
once all said and done we return dfs() which calls itself and builds our tree to be returned.
"""