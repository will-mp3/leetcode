"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # ensure we always binary search A for simplicity
        if len(B) < len(A):
            A, B = B, A  

        # binary search on A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B (j starts at zero, i starts at 0. account for index)

            # set our edge variables and check that they are in bounds
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright) # this is where the infinity swap comes in to play
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # A is too big, too many elements from A
            elif Aleft > Bright:
                r = i - 1
            # A is too small, too little elements from A
            else:
                l = i + 1

"""

"""