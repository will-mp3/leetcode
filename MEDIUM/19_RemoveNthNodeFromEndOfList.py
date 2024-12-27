"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right: # shift right into position
            right = right.next
            n -= 1

        while right: # shift right to null
            left = left.next
            right = right.next

        # delete target node
        left.next = left.next.next

        return dummy.next

"""
to solve this problem we make use of a two pointer solution like we've seen many times before.
given a value n, if we set our left pointer at the head and our right pointer n nodes in front of the left pointer and iterate through the list,
by the time that the right pointer reaches the end of the list (equals null) our left pointer will be on our desired value.
this is good, however since we want to remove this node its better if our left pointer is on the node before so we can reassign its next value.
to accomplish this we create a dummy node before the head and use that as the left pointer instead.
this makes the gap n + 1 and will land us on the node before the one we are targetting (left.next), allowing us to remove its pointer.
we then simply return dummy.next (the head).
this solution runs in O(n) linear time.
"""