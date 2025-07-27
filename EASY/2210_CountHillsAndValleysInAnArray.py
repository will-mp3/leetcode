"""
You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. 
Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. 
Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.
"""

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        l = 0

        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                if (nums[i] > nums[l] and nums[i] > nums[i + 1]) or \
                   (nums[i] < nums[l] and nums[i] < nums[i + 1]):
                    res += 1
                l = i

        return res

"""
This code defines a solution to count the number of hills and valleys in a given integer array.
The `countHillValley` method iterates through the array, checking for hills and valleys by comparing the current element with its neighbors.
A hill is identified when the current element is greater than both its neighbors, while a valley is identified when it is less than both neighbors.
The method maintains a pointer `l` to track the last non-equal neighbor, ensuring that adjacent equal elements do not falsely contribute to hills or valleys.
The time complexity is O(n), where n is the length of the input array, making it efficient for larger inputs.
The solution effectively counts the hills and valleys by leveraging simple comparisons and a single pass through the array.
The final result is returned as the count of hills and valleys found in the input array.
"""