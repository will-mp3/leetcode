"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i if i >= 1 else 0
        return len(nums)

"""
This code defines a solution to find the index at which a target value should be inserted into a sorted array of distinct integers. If the target value is already present in the array, it returns the index of that value. The function `searchInsert` takes a list of integers `nums` and an integer `target` as input and returns an integer representing the index.
The method iterates through the list `nums` using a for loop. For each element, it checks if the current element is greater than or equal to the target value. If it finds such an element, it returns the current index `i`. If `i` is 0, it returns 0, indicating that the target should be inserted at the beginning of the array.
If the loop completes without finding an element greater than or equal to the target, it returns the length of the list `nums`, indicating that the target should be inserted at the end of the array.
The time complexity of this solution is O(n) in the worst case, as it may need to iterate through the entire list. The space complexity is O(1) since it uses a constant amount of additional space.
"""