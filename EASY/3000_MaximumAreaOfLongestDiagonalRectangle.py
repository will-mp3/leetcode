"""
You are given a 2D 0-indexed integer array dimensions.

For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.

Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.
"""

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        maxDiag = 0
        
        for rec in dimensions:
            diag = math.sqrt((rec[0] * rec[0]) + (rec[1] * rec[1]))
            if diag > maxDiag:
                maxDiag = diag
                res = rec[0] * rec[1]
            elif diag == maxDiag:
                res = max(res, rec[0] * rec[1])
        
        return res

"""

"""