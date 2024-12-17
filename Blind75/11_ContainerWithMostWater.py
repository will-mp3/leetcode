"""
You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else: # both the > and == clause since it dosent matter which pointer we adjust when ==
                r -= 1

        return res

"""
so solve this problem we want to first start by making two pointers, l and r.
these pointers point to the left-most and right-most values in the array.
we start here because we have the maximum possible width in this case.
the algorithm works by incrementing l or decrementing r based on which of the two is smaller.
for example if we have l = 1 and r = 8 then we would shift l + 1 in search of a larger area.
this solution runs in O(n) linear time.
"""