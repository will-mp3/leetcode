"""
You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.
"""

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while True:
          if original in nums:
            original = original * 2
          else:
            return original

"""
This solution first converts the input list nums into a set for O(1) average-time complexity lookups. 
It then enters a loop where it checks if the current value of original is present in the set. 
If it is found, original is doubled. 
If not, the loop breaks and the final value of original is returned. 
"""