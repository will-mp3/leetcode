"""
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.
"""

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minRow, maxRow = m, -1
        minCol, maxCol = n, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    minRow = min(minRow, i)
                    maxRow = max(maxRow, i)
                    minCol = min(minCol, j)
                    maxCol = max(maxCol, j)

        return (maxRow - minRow + 1) * (maxCol - minCol + 1)

"""
This code defines a solution to find the minimum possible area of a rectangle that can cover all the 1's in a given 2D binary array grid.
The `minimumArea` method initializes the number of rows `m` and columns `n` of the grid, and sets initial values for the minimum and maximum row and column indices that will be updated as it finds 1's in the grid.
It then iterates through each cell in the grid. If it encounters a cell with a value of 1, it updates the minimum and maximum row and column indices accordingly.
After processing the entire grid, it calculates the area of the rectangle that covers all the 1's using the formula `(maxRow - minRow + 1) * (maxCol - minCol + 1)` and returns this value.
The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the grid, as it processes each cell exactly once.
"""