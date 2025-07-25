"""
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.
"""

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = []
        for num in nums:
            if num not in seen:
                seen.append(num)
        seen.sort()
        if len(seen) == 1:
            return seen[0]
        else:
            res = sum(seen)
            for i in range(len(seen) - 1):
                if res - seen[i] > res:
                    res -= seen[i]
        return res

"""
this solution defines a method to find the maximum sum of a subarray with unique elements from a given integer array.
The `maxSum` method first creates a list of unique elements from the input array, sorts it, and then calculates the sum of these unique elements.
If there is only one unique element, it returns that element.
Otherwise, it iterates through the unique elements and checks if removing any element would yield a higher sum, updating the result accordingly.
The final result is the maximum sum of the unique subarray.
The solution efficiently handles the uniqueness constraint and maximizes the sum by leveraging sorting and iteration.
The time complexity is O(n log n) due to sorting, where n is the number of unique elements in the input array.
This ensures that the solution is efficient even for larger input sizes.
"""