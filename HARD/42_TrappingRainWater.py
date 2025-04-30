"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax: # shift left pointer
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] # this will never be negative

            else: # leftMax > rightMax - shift right pointer
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res

"""
this solution is found by understanding how the bottle necks work in our problem.
we know that for each given index, we can only hold as much water as the minimum of its left and right sides.
using this understanding, our algorithm goes through the elevation array using left and right pointers to track elevations.
we also track the max left and right elevations.
the trick is that with each iteration, we shift the minimum of the two maxes and then calculate our water based on the newly shifted max.
this is because we know, for example, if we had to shift the left max, then the left max is the bottleneck (the minimum of the two).
this allows us to calulate the water caught by subtracting the bottleneck max by the current height.
this idea is repeated until our pointers meet, each time updating result with the water calculation.
this solution runs in O(n) time with O(1) space complexity.
"""