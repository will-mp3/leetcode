"""
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. 
Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        return self._count_subsets(nums, 0, 0, max_or_value)

    def _count_subsets(
        self, nums: List[int], index: int, current_or: int, target_or: int
    ) -> int:
        # Base case: reached the end of the array
        if index == len(nums):
            return 1 if current_or == target_or else 0

        # Don't include the current number
        count_without = self._count_subsets(
            nums, index + 1, current_or, target_or
        )

        # Include the current number
        count_with = self._count_subsets(
            nums, index + 1, current_or | nums[index], target_or
        )

        # Return the sum of both cases
        return count_without + count_with

"""
This code defines a solution to count the number of subsets of an integer array that yield the maximum bitwise OR.
The `countMaxOrSubsets` method calculates the maximum bitwise OR value of the input array and then uses a recursive helper method `_count_subsets` to count the number of subsets that achieve this maximum OR value.
The helper method explores both including and excluding each element in the array, recursively calculating the OR value and checking against the target maximum OR.
The base case of the recursion checks if the end of the array is reached, returning 1 if the current OR matches the target OR, or 0 otherwise.
The time complexity of this solution is O(2^n), where n is the length of the input array, as it explores all possible subsets.
This approach ensures that all combinations are considered, and the final count of valid subsets is returned.
The solution effectively handles the problem of counting subsets with a specific bitwise OR by leveraging recursion and bitwise operations.
The use of bitwise OR operations allows for efficient calculation of the maximum OR value and the subsets that achieve it.
The recursive structure ensures that all possible combinations of elements are explored, leading to an accurate count of valid subsets.
The solution is designed to be clear and concise, making it easy to understand the logic behind counting subsets with the maximum bitwise OR.
The final result is returned as the total count of subsets that yield the maximum OR value, providing a complete solution to the problem.
"""