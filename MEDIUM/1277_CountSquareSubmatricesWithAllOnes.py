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
                        toAdd = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])
                        matrix[i][j] += toAdd
                        res += toAdd
        
        return res

"""

"""