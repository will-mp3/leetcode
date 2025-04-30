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
this problem involves us merging two lists to find the median, however a proper merge is not neecsary and actually wont work.
the problem gives us a time contraint of O(logn) time, which points us in the direction of binary search.
The idea is that we start by finding the middle of the smallest array, 
and using that value calculate how much of our larger array is needed to make equal partitions.
if the middle value of A is 3, and theres 12 values total, we know we need 3 values from B.
we set up our variables to accomplish this first "pass" by getting our A and B arrays, ensuring A is the smallest.
we also calculate our half value and save our total size.
once done, we set up a loop that will continue until returned.
the loop essentially binary searches until we find that our partitions are correct.
that means our left half is smaller than our right half.
we know this is true if the left value of A (largest of A left partition) is smaller than our right value of B (smallest of B right partition)
and our left value of B (largest of B left partition) is less than our right value of A (smallest of A right partition).
if this is true, we check whether there is an even number of elements and return the appropriate value.
if not true, we check which partition to increment in order to perform our binary search.
we then recalculate our A and B left & right values and repeat the process.
this repeats until our partitions are correct and a value is returned.
"""