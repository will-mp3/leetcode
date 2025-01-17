"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1

        for p in range(m + n - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

"""
for this solution, we approach using two pointers, p1 and p2.
to solve this problem using minimal memory as well as time, we start by modifying nums1 from the end where there is empty data.
p1 represents nums1, so we initialize it to n - 1 and p2 represents nums2 so we initialize it to m - 1.
we iterate through the total length of nums1, m + n - 1, backwards.
each time we first check to see if p2 has any values, if not we break the loop.
after that we check two conditions, is the value at p1 greater than that at p2 or is the value at p2 greater than that at p1.
if the former is true, we add nums1[p1] to the current index in the greater nums1 array (nums1[p]).
if the latter is true, we add nums2[p2] to the current index.
each time one of these conditions is found to be true, we decrement the associated pointer.
this solution runs in O(n + m) linear time and has a space complexity of O(1).
""" 