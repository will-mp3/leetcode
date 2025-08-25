"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                groups[i + j].append(mat[i][j])

        res = []
        for i in range(len(mat) + len(mat[0])):
            res += groups[i] if i % 2 == 1 else groups[i][::-1]
        
        return res

"""

"""