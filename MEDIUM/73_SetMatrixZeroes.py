"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        # dedicated value to account for overlapping [0][0] edge case
        rowZero = False

        # determine which rows and columns need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # update arrays
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        # zero most rows
        for r in range(1, ROWS): # skip first row and column, handle after
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # zero first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # zero first row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

"""
this problem presents a space complexity constraint rather than a time complexity constraint.
the most effecient time complexity we can get is O(m * n) due to the need for checking and replacing values.
two options we have are making and updating a copy (space comp. O(m * n)) or row/col arrays to denote needed updates (space comp. O(m + n)).
both of these are alright but we can do this problem in O(1) space complexity.
this solution makes use of the concept behind the row/col arrays, but instead of making new objects we utilize the first row and column of the matrix.
this reason this works is because if a zero is found and we update the array, it wont change the matrix in a manner that matters,
this is because the value getting changed has already been visited.
previously the need for a copy was needed because if we changed a row to all zeros and then landed on a zero that was placed artifically
our matrix may be changed incorrectly.
the way our solution works in by first going through the entire matrix and marking each row/col that needs to be changed.
reminder these values are stored as zeroes in the first row and column.
once everything is marked, we go through the matrix once more and make the changes.
to account for the overlapping cell at [0][0] we go through most of the matrix first and update the zeroes, avoiding the first row and column.
next we handle the first column, 
and finally based on the rowZero variable we used to account for the previously mentioned endge case we update the first row.
this solution runs in O(m * n) time complexity and O(1) space complexity.
"""