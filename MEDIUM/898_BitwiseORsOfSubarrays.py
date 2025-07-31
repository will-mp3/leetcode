"""
Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.

The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = {0}
        for x in arr:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)

"""
This code defines a solution to find the number of distinct bitwise ORs of all non-empty subarrays of a given integer array.
The `subarrayBitwiseORs` method uses a set to keep track of distinct bitwise OR values. 
It iterates through each element in the array, updating the current set of OR values by combining the current element with all previously computed OR values. 
The union of these new values with the existing set ensures that only distinct values are retained.
Finally, the method returns the size of the set, which represents the number of distinct bitwise ORs found.
The time complexity of this solution is O(n * m), where n is the length of the input array and m is the average size of the current set, as it processes each element and combines it with all previous OR values.
This approach efficiently captures all unique OR results from subarrays, ensuring that duplicates are not counted multiple times.
The use of sets allows for quick membership checks and ensures that only distinct values are stored, leading to an accurate count of unique bitwise ORs.
"""