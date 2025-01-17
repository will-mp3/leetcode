"""
You are given a 0-indexed integer array nums and a positive integer k.

We call an index i k-big if the following conditions are satisfied:

There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i].
There exist at least k different indices idx2 such that idx2 > i and nums[idx2] < nums[i].
Return the number of k-big indices.
"""

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        lo = SortedList()
        hi = SortedList(nums)
        ans = 0 
        for x in nums: 
            if lo.bisect_left(x) >= k and hi.bisect_left(x) >= k: ans += 1
            lo.add(x)
            hi.remove(x)
        return ans

"""
this problem asks us to find the number of indices in a list where there are k amount of smaller values to the left and right of that index.
A "k-big index" is an index is an index where there are k numbers <= nums[i] before i and k numbers <= nums[i] after i.
to solve this, we make use of sorted lists (a python3 specific import).
we create lists lo and hi, lo tracks the numbers before i and hi tracks the numbers after i.
we iterate through each number in nums, each time using the bisect left method.
what this does is inserts our passed in value x to the position in which it wont disrupt the order of the sorted list.
this checks how many numbers in lo (before i) are less than x and how many numbers in hi (after i) are less than x.
if there are k or more numbers less than nums[i] before and after i (in lo and high), increment ans.
each iteration we add the current value x to lo and remove it from hi to simulate shifting.
this solution runs in O(nlogn): add, remove, and bisect_left = logn ; length of nums = n.
"""