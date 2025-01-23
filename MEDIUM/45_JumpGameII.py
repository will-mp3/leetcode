"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        far, end = 0, 0
        res, n = 0, len(nums)

        for i in range(n - 1):
            far = max(far, i + nums[i])

            if i == end:
                res += 1
                end = far
        
        return res

"""
to solve this problem we take a greedy approach, we ultimately just need to calculate the smallest amount of steps, not the optimal steps.
we have two variables we track, far and end, 
which track the farthest point we can reach from our current position and the end point we have reached.
we iterate through the entire list, each time calculating a new farthest index.
after this, if our current index i equals our current endpoint we increment result by 1 and set our new endpoint equal to the farthest index.
what this is doing is finding the farthest point we can reach at our current index.
for example is index 2 has the value 3 and index 3 has the value 1 we keep that farthest distance from index 2.
using this farthest distance we update our result and end point every time we reach it.
the first iteration end automatically updates to the farthest point, and until we reach that now saved end point the farthest point keeps updating.
once we reach the endpoint, our farthest point has updated to the max of any position thus far and gets updated as our new endpoint.
once it gets large enough to cross the end threshhold then i will never reach it, and result will stop incrementing.
the loop finishes and result is returned.
this soltution runs in O(n) linear time.
"""