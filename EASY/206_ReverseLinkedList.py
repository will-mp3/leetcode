"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

"""
this is a common practive needed for linked list problems.
to reverse a linked list in the most efficient way, we want to first start at the head of the list.
we will make our current node the head, and the previous node null for starters (our two tracked variables).
we iterate through the list doing three things:
first, we reverse our pointer from current and have it point to the current previous node instead of the one in front of it.
we then move up our pointers, setting previous to current and current to the next node.
note: we use nxt as a temporary variable for curr.next since we are detaching the pointer to it in the second line of the loop.
once finished we can return the head which should be stored in prev.
this solution runs in O(n) linear time.
"""