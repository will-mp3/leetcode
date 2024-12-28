"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom: # loop until pointers meet
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every i in the left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

"""
to solve this problem we will use four boundary pointers: left, right, top, and bottom.
these pointers will help guide our iteration and also act as the condition for which our result is complete.
note the right and bottom are initiated outside of the matrix to help with the range function.
if at any point the pointers equal eachother, top and bottom or left and right, we know we are finished and can return.
with every row/col we update the pointers, moving them closer to eachother and shrinking our effective matrix.
we start by iterating through the top row, we go from left to right and append all of these values to result.
we then get every value in the right column, we go from top to bottom, adding these values (subtract 1 from right due to it starting outside).
next we get every value in the bottom row, going from right to left (we must use values right - 1 and left - 1 for range function).
finally we get the values in the left column, going from bottom to top (note the top was updated previously).
the entire outside grid of our matrix has been added now and we can repeat this loop on the next ring however many times necesary.
once either of the pointer sets equal eachother break the loop and return result.
this solution runs in O(m * n)
"""