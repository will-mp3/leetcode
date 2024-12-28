"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # create second half of list
        prev = slow.next = None # point end of first half to null

        while second: # reverse the second portion of the list
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two halves
        first, second = head, prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            
            # insert second node inbetween first and first.next
            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2

"""
this solution is broken up into two parts, separating the list into halves and merging those halves together.
the first thing we need to do is separate the list into halves, to find the middle of the list we use slow and fast pointers.
the slow pointer increments by 1 and the fast pointer increments by 2, this will land slow in the middle once fast reaches the end.
next thing we need to do is reverse the second half of the list.
we do this by flipping the pointers of the nodes to allow us to traverse in the same direction as the first half once we merge.
once reversed, we begin to merge the two halves.
the algorithm for this makes use of temp variables to insert a value from the second half inbetween a value from the first half and its next.
we continue doing this and update our pointers each iteration.
for this problem no return is necesary.
this solution runs in O(n) linear time.
"""