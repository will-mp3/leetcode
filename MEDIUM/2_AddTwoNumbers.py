"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        cur = dummyHead
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            lsum = x + y + carry
            carry = lsum // 10
            node = ListNode(lsum % 10)
            cur.next = node
            cur = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummyHead.next

"""
to solve this problem we use basic arithmetic in combination with a carry variable.
we know that due to resizing of lists we cant edit our current lists in place, we must make a new one.
we start by creating a head node, dummyHead, and setting cur equal to it along with our carry value equal to 0
while l1, l2, or carry are not Null or zero we loop through our lists.
first, we check if l1 is not null; if l1 exists we set x equal to its value otherwise we set x equal to 0.
we do the same for y and l2 and then add them together with our carry variable in our variable lsum.
we then calculate our carry by dividing lsum by 10 (this type of division eliminates remainders).
now that everything is calculated, we create a node node with our sum % 10 so account for the carry value.
we set cur.next to the node to link it with our list then set cur equal to our node.
finally we move l1 and l2 if their next value is not null.
once finished we return dummyHead.next (the start of our list).
"""