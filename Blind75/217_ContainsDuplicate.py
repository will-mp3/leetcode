"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hSet = set()

        for n in nums:
            if n in hSet:
                return True
            hSet.add(n)
        return False

"""
to solve this problem we begin by initializing a hashset.
using our hashset, we iterate through the list and check if n is in our hashset.
if true, return True.
if false, add n to our hashset.
continue looping until a duplicate is found or the loop completes and returns False.
this solution uses extra memory, the hashset, in return for a better runtime.
this solution runs is O(n) linear time and has a space complexity of O(n) due to the hashset.
"""