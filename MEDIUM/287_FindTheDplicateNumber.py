"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # phase one: find where slow and fast intersect
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # advance fast by 2

            if slow == fast:
                break

        slow2 = 0
        # phase two: find where slow and slow2 intersect and return
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                return slow

"""
to solve this problem we treat our input as a linked list and use floyds cycle algorithm to detect a loop.
to use our array as a linked list we treat the values in each position as pointers to respective indexes.
for example if index zero held a 3, then it would point to index 3.
say index three contains a 2, we would map a node with value 3 pointing to a node with value 2 and so on.
these indexes and nodes are important to understand for how we will increment our pointers in the algorithm.
our goal is to find a cycle, specifically the beginning of one, as that will be the value that has a duplicate.
for this we will use floyd's algorithm which is capable of not only finding cycles but finding the start of them.
floyd's algorithm is split into two phases, one where our fast and slow pointer intersect and one where two slow pointers intersect.
for phase one we increment our slow pointer by shifting its pointer one node, and we increment our fast pointer by shifting it two.
notice the syntax for this, its different than index shifting since we are hopping spots based on node values.
once they equal we break our loop and keep slow where it is.
for phase two we create a new slow pointer and loop once again until they intersect, this time with equal increments.
once they intersect we have found the start of our cycle and can return either pointer.
"""