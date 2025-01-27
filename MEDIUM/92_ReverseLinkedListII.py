"""
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        lnode, rnode = head, head
        stop = False

        def recurse(rnode, left, right):
            nonlocal lnode, stop

            # base case
            if right == 1:
                return

            # move right pointer until right == 1
            rnode = rnode.next

            # move left pointer to the right until we reach the proper position
            if left > 1:
                lnode = lnode.next

            # recurse
            recurse(rnode, left - 1, right - 1)

            # if pointers cross or become equal we stop
            if lnode == rnode or rnode.next == lnode:
                stop = True
            
            if not stop:
                lnode.val, rnode.val = rnode.val, lnode.val
            
                # move left one step right
                lnode = lnode.next
        
        recurse(rnode, left, right)
        return head

"""
for this solution we make us of a recursion function and a few global variable tricks.
the way our function works is by having four variables tracking through the execution.
two for our actual nodes and two for counting.
we use lnode and rnode for our left and right nodes and left and right as our location pointers.
we define our recursive function to take in our right node and our two location pointers.
the base case for our recursive function is when right == 1, 
these pointers are decremented each call and the nodes are moved alongside them.
left will always be less than right, so once left is less than 1 we stop moving our left node since we have found its position.
we continue decrementing right until it hits one, meaning our right node is now also in position.
once this condition is met we begin backtracking, and while our global variable stop is false we also swap the values.
we use stop because we must recurse through the whole list and we cant break this, so we want to specify which nodes to swap.
as we backtrack and swap, we check if the left and right nodes are equal or have crossed.
if either of these happen we make stop True, stop swapping, and let the recursion complete.
this solution runs in O(n) linear time.
"""