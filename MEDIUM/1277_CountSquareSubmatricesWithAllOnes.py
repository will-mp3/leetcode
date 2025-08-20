"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # check to see if cell is valid
                if matrix[i][j] == 1:
                    res += 1
                    # check edges
                    if i == 0 or j == 0:
                        continue
                    
                    # if upper edges are greater than or equal to 1, increment cell & result by the minimum of their values
                    if matrix[i - 1][j - 1] >= 1 and matrix[i][j - 1] >= 1 and matrix[i - 1][j] >= 1:
                        matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])
                        res += matrix[i][j] - 1
        
        return res

"""
This code defines a solution to count the number of square submatrices filled with all ones in a given binary matrix.
The `countSquares` method initializes a result variable `res` to zero. It then iterates through each cell in the matrix. 
If the current cell contains a 1, it increments `res` by 1, indicating that at least one square submatrix (of size 1x1) exists at that cell.
If the cell is not on the first row or first column, it checks the values of the cells directly above, to the left, and diagonally above-left. 
If these cells also contain ones, it calculates the minimum of these three values and adds it to the current cell's value, effectively counting larger square submatrices that can be formed with this cell as the bottom-right corner.
Finally, it returns the total count of square submatrices filled with ones.
The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the matrix, as it processes each cell exactly once
"""