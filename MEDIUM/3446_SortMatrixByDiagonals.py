"""
You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
"""

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        diags = defaultdict(list)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diags[i - j].append(grid[i][j])
                diags[i - j].sort(reverse = False if i - j < 0 else True)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = diags[i - j][min(i, j)]
        
        return grid

"""

"""