"""
A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list 
such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None : None } # null pointer edge case

        cur = head
        # first pass: create copies of all nodes and map them to our hashmap
        while cur:
            # create copy of node and map the copy to the old node
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        # second pass: set pointers
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]

"""
this solution is actually very simple.
the tricky part is the random pointer which needs to be accounted for when making the copy.
to solve for this we use a two pass strategy and a hashmap of all the "old" nodes.
we start by initializing our hashmap with one pair, null mapping to null, to account for the null pointer edge case.
once this is done we set our variable cur equal to the head and begin our first pass.
this first pass we aim to copy each node and map the old node (cur) to this new copy in our map.
once this loop completes we set cur equal to the head once more and begin our second pass.
the goal of our second pass is to set the pointers for each of our copy nodes.
since we've saved them to our map we can access them using the current node as the key and set the pointers.
to set said pointers we use cur.next and cur.random as our key for the hashmap which will get us the correct node to point to.
once this is finished we can return the copy mapped to head.
this solution runs in O(n) linear time.
"""