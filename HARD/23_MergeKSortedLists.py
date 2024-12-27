"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2): # merging pairs so we increment 2
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists

        return lists[0]


    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

"""
this solution uses the solution from 21 as a helper variable to solve.
since we already know how to merge two linked lists, our task really is to expand that principle for a larger group.
the way we do this effeciently is by merging two lists at a time and then updating our list of lists.
this cuts the amount of lists in half for each round of iterations and continues doing so until we get to a length of 1.
the code is extremely simple since we already have our merge list solution from problem 21. 
all we do is go through pairs of lists and use our merge function.
this creates a sort of tree shape where the list goes from say 8 lists to 4, then 4 to 2, then 2 to 1 and returns.
this solution runs in O(nlogn).
"""