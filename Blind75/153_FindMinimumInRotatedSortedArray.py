"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

"""
to begin thinking about this problem we start by observing the required time complexity.
because O(log n) time is required, we are going to use a form of binary search.
to set up: start by tracking our result and two pointers (left and right) that point to the left-most and right-most item.
the first bit of logic after the while loop checks if the array is in sorted order and if so we break the while loop
the brunt of our logic will involve using the m pointer (middle position)
this divides the list into two sorted portions, left and right.
we check to see if m is larger than the leftmost value.
if true, we know that m is in the left-most portion and we need to search right 
since we know the pivot (largest value to smallest value due to rotation) cant be to the left.
ex: [3(l), 4, 5(m), 1, 2(r)]
if false, we know that m is in the rightmost portion and we need to search left for the same reason above.
ex: [5(l), 1, 2(m), 3, 4(r)]
this logic continues until we find the solution.
this solution runs in O(log n) logarithmic time.
"""