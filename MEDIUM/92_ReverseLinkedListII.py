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

            # move right pointer until n == 1
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

"""