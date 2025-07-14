"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binStr = ""

        while head:
            binStr = binStr + str(head.val)
            head = head.next
        
        return int(binStr, 2)

"""
this solution uses a simple while loop.
we initialize an empty string to hold our binary value, and continuously iterate through nodes in our list.
with each node we add the string value to our binary string and update head to be head.next.
once head is null we break and return the binary casted version of our string.
this solution runs in O(n) linear time.
"""