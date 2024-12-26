"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

"""
to solve this problem we can easily use a hast set to iterate through the list and check if a node has already been visited.
however, if we want to optimize this and acheive linear time AND constant space complexity we can use floyd's tortoise and hare algorithm.
the way this works is we have a slow pointer and a fast pointer.
the slow pointer increments by 1 every cycle and the fast pointer increments by 2 every cycle.
if at any point the fast pointer reaches the end of the list we know there is no loop.
to check if there is a loop, we continue to iterate and if slow and fast ever equal eachother then we know there is a loop.
this is because while the fast pointer will start in front of the slow pointer after iteration 1,
if they are moving cyclically the fast pointer will continue to close the gap by one space each iteration, eventually reaching the slow pointer.
this solution runs in O(n) linear time and has a space complexity of O(1).
"""