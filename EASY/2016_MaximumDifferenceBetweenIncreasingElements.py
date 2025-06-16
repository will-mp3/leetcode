"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] 
(i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
"""

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l, r = 0, 1
        maxDif = float("-inf")

        while r < len(nums):
            if nums[r - 1] < nums[l]:
                l = r - 1
            maxDif = max(maxDif, nums[r] - nums[l])
            r += 1

        if maxDif <= 0:
            return -1
        
        return maxDif

"""
for this solution we use two pointers to find the largest difference.
the basic algorithm is we traverse our list iwth left and right pointers, checking the difference each time.
with each iteration we first check to see if the last seen number is smaller than our current left pointer, our small value.
if it is smaller, we update the left pointer to r - 1 (the last seen value).
we then check if the difference between nums[r] and nums[l] is larger than our current largest difference, if so update.
finally we increment our right pointer by 1 and repeat the process until out of bounds.
once the loop completes we check if we found a difference greater than zero, if not return -1.
otherwise return maxDif.
this solutions runs in O(n) linear time.
"""