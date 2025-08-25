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
This code defines a solution to traverse a given m x n matrix in a diagonal order and return the elements in that order as a list.
The `findDiagonalOrder` method uses a dictionary `groups` to group the elements of the matrix based on the sum of their row and column indices (i + j). This sum represents the diagonal level of the element.
It iterates through each cell in the matrix, appending the element to the corresponding list in the `groups` dictionary.
After grouping the elements, it initializes an empty list `res` to store the final result. It then iterates through the possible diagonal levels (from 0 to m + n - 2) and appends the elements from each group to `res`. If the diagonal level is odd, it appends the elements in their original order; if even, it appends them in reverse order to achieve the required zigzag pattern.
Finally, it returns the list `res` containing the elements in diagonal order.
The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the matrix, as it processes each cell exactly once.
"""