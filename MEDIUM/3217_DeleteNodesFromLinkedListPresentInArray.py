"""
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numSet = set(nums)
        dummy = ListNode(None)
        cur = dummy
        while head:
            if head.val not in numSet:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
        return dummy.next

"""
This solution first converts the array of integers into a set for O(1) look-up times. 
It then iterates through the linked list, adding nodes to a new linked list only if their values are not present in the set. 
Finally, it returns the head of the newly constructed linked list.
This soplution runs in O(N + M) time complexity, where N is the length of the linked list and M is the length of the array.
"""