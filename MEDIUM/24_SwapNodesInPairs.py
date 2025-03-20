"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            # save pointers
            nextPair = cur.next.next
            second = cur.next

            # reverse this pair
            second.next = cur
            cur.next = nextPair
            prev.next = second

            # update pointers
            prev = cur
            cur = nextPair

        return dummy.next

"""
this solution dosent involve a super complicated algorithm, its just a little hard to visualize.
to solve this problem we need to use a dummy node since we are manipulating a lot of pointers.
the first thing we need to do is create this dummy node and set it pointing to head.
once this is set up we can begin to visualize the problem.
for every pair of nodes, we need to change the next pointers so that the first node in the pair (cur) is pointing to the third (cur.next.next)
and the second (cur.next) is pointing to the first (cur).
we do this swap for every value until we reach the end of our list.
how we accomplish this is first by saving a few pointers for reassignment, specifically our "third" and "second" nodes in the pair.
once we save these pointers we can reverse the pair.
to do this we set our second node to our current node, our current node to the third, and our previous node to the second.
the new order is now previous -> second -> first -> third.
as you can see first and second have swapped but maintained the chain of nodes.
finally we update our static pointers to move previous and cur up one node, in this case prev = first and cur = third (jumping two nodes).
this continues until the list runs out and we return dummy.next which will always point to the head.
this solution runs in O(n) linear time.
"""