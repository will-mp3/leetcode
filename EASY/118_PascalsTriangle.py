"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res

        for i in range(1, numRows):
            cur = [0 for _ in range(i + 1)]
            cur[0], cur[-1] = 1, 1
            
            for j in range(1, i):
                cur[j] = res[i - 1][j] + res[i - 1][j - 1]
                
            res.append(cur)

        return res

"""

"""