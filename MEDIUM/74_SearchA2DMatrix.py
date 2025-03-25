"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        # binary search for rows
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]: # check rightmost value (largest in that row)
                top = row + 1 # look at rows that are larger, shift top down
            elif target < matrix[row][0]: # check leftmost value (smallest in that row)
                bot = row - 1 # look at rows smaller, shift bot up
            else:
                break # target falls within current row, break

        # the following condition checks if the loop properly broke
        # if not, the target value is not within our matrix, return False
        if not (top <= bot):
            return False

        # binary search for the found row
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]: # check if target is greater than middle
                l = mid + 1 # shift left pointer to search right partition
            elif target < matrix[row][mid]: # check if target is less than middle
                r = mid - 1 # shift right pointer to search right partition
            else:
                return True
        
        return False

"""

"""