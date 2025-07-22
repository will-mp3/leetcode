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

"""