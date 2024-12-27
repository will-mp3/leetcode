"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

"""
so solve this problem we use a simple iterative solution.
the algorithm is as follows:
we first want to create a dummy node to ensure we dont have problems inserting into a null list.
next we iterate through the two lists while they are both not null.
during this process we check two conditions:
if the value at the current list1 pointer is less than the value of the current list2 pointer we insert the list1 value into our list.
we then update our list1 pointer to prepare to check the next value.
if the opposite is true we insert the list 2 value and update the list 2 pointer.
we update tail at the end of each iteration.
if the solution is not found by the end of the loop we add whatever remains from whichever list is not null onto the end of our result list.
we then return the head value.
this solution runs in O(n) linear time.
"""