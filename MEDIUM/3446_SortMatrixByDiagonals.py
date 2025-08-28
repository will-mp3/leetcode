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
This code defines a solution to sort the diagonals of a given n x n square matrix according to specific rules for the bottom-left and top-right triangles.
The `sortMatrix` method uses a dictionary `diags` to group the elements of the matrix based on the difference between their row and column indices (i - j). 
This difference uniquely identifies each diagonal in the matrix.
It iterates through each cell in the matrix, appending the element to the corresponding list in the `diags` dictionary. 
After populating the dictionary, it sorts each diagonal list in non-increasing order for the bottom-left triangle (i - j >= 0) and in non-decreasing order for the top-right triangle (i - j < 0).
After sorting the diagonals, it iterates through the matrix again and replaces each element with the corresponding sorted value from the `diags` dictionary. 
The index used to retrieve the sorted value is determined by the minimum of the row and column indices (min(i, j)), which ensures the correct position within the diagonal.
Finally, it returns the modified matrix with the diagonals sorted as specified.
The time complexity of this solution is O(n^2 log n), where n is the number of rows (or columns) in the matrix, due to the sorting of the diagonals. The space complexity is O(n^2) for storing the diagonals in the dictionary.
"""