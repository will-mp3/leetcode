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
this problem gives us a time complexity restraint of O(log(m * n)).
seeing this our first thought is that we will need to use some form of binary search given we are hunting for lgoarithmic time.
the problem gives us two extra clues to help with this.
we know that each row in our matrix is already sorted, and we also know our columns are sorted as well.
knowing this, not only can we use binary search on each specific row to acheive O(mlogn) time (brute force would be O(m * n)).
we can also binary search the columns using their first and last values to acheive O(log(m + n)).
essentially we are taking what would be a linear product time complexity and turning it into a logarithmic sum.
to start, we run binary search on our rows, we set top and bottom pointers and loop while they havent crossed.
for each iteration we collect our middle value, row, and check to see if our target is greater than its rightmost (largest) value,
or if our target is less than its leftmost (smallest) value.
if the first is true we move our top value down and search the bottom partition. 
if the second is true we move bottom up and search the top partition.
if neither is true then our value should fall within our current row and we can break our of the loop.
once the loop finishes we need to check if the break was due to finding the row or if the loop simply ran out.
now we can do binary search on our specific row.
following the same logic we set left and right pointers and loop while they havent crossed each other.
we get our middle value, compare it to target, and search the appropriate partition.
if at any point our middle value isnt greater than or less than our target, we found it and can return True.
if the loop completes without returning True, return False.
this solution runs in O(log(m + n)).
"""