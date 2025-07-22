"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
"""

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l, cur, res = 0, 0, 0

        for r in range(len(nums)):
            while nums[r] in seen:
                cur -= nums[l]
                seen.remove(nums[l])
                l += 1
            cur += nums[r]
            seen.add(nums[r])
            res = max(res, cur)

        return res

"""
this code defines a solution to the problem of finding the maximum score obtainable by erasing a subarray of unique elements from an array of positive integers.
The `maximumUniqueSubarray` method uses a sliding window approach with two pointers (`l` and `r`) to maintain a window of unique elements. 
It keeps track of the current sum of the elements in the window (`cur`) and updates the maximum score (`res`) whenever a new element is added to the window. 
If a duplicate element is encountered, it shrinks the window from the left until the duplicate is removed, ensuring that all elements in the window remain unique.
The time complexity of this solution is O(n), where n is the length of the input array `nums`, as each element is processed at most twice (once when added and once when removed).
"""