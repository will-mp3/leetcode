"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        # roating in counter clockwise order
        while l < r:
            for i in range(r - l): # evaluates to n - 1 rotations per row/col
                top, bottom = l, r

                # save the top left value
                topLeft = matrix[top][l + i] # shift top left to the right

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l] # shift bottom left up

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i] # shift bottom right to the left

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r] # shift top right down

                # move top left into top right
                matrix[top + i][r] = topLeft

            # decrement pointers
            r -= 1
            l += 1

"""
to solve this problem we use a similar pointer method as problem 54 spiral matrix.
using left, right, top, and bottom pointers we are able to divide the main problem into smaller subproblems.
we use these pointers in conjunction with a while loop to swap our values around as needed.
the first thing we do is set aside the top left value into its own temp variable topLeft.
then, in counterclockwise order we update the bottom left, bottom right, top right, and top left value.
once finished we update out left and right pointers and run through that logic again.
i is incremented, and we do the same logic using i as a shift value.
we then swap the appropriate values again and continue the process until the left pointer is no longer less than the right pointer.
there is no need for a return value as we are updating the original matrix.
this solution has O(n^2) time complexity and O(1) memory complexity. 
"""