"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []

        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if start != nums[i]:
                res.append(str(start) + "->" + str(nums[i]))
            else:
                res.append(str(nums[i]))
            i += 1
        
        return res

"""
this solution dosent make use of too many fancy concepts, the algorithm is rather starightforward.
we start by initializing our variable i and result array.
we then create an outer while loop, this loop represents one range each iteration.
inside of this loop we create a variable start and set it to the value at the current index i.
the next while loop serves to move i along the list of numbers so long as they are concurrent.
once this loop breaks we know that our range is organized, we then check two conditions.
if our start element is different than our current element (end) we append both of them in the proper format.
if start and our current element are the same we only append one to avoid duplicates.
this solution runs in O(n) linear time.
"""