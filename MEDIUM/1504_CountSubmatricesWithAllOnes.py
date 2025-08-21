"""
Given an m x n binary matrix mat, return the number of submatrices that have all ones.
"""

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        h = [0] * c
        ans = 0
        for i in range(r):
            for j in range(c):
                h[j] = h[j] + 1 if mat[i][j] else 0
            sumv, st = [0] * c, []
            for j in range(c):
                while st and h[st[-1]] >= h[j]:
                    st.pop()
                if st:
                    p = st[-1]
                    sumv[j] = sumv[p] + h[j] * (j - p)
                else:
                    sumv[j] = h[j] * (j + 1)
                st.append(j)
                ans += sumv[j]
        return ans

"""
This code defines a solution to count the number of submatrices filled with all ones in a given binary matrix mat.
The `numSubmat` method initializes the number of rows `r` and columns `c` of the matrix, and creates a height array `h` to keep track of the heights of consecutive ones in each column.
It then iterates through each row of the matrix. For each row, it updates the height array `h` based on whether the current cell contains a 1 or 0.
Next, it initializes a `sumv` array to store the cumulative sums of valid submatrices and a stack `st` to help calculate the number of submatrices efficiently.
It iterates through each column, using the stack to maintain the indices of columns with increasing heights.
When it finds a column with a height less than or equal to the current column, it pops indices from the stack until it finds a column with a smaller height.
It then calculates the number of submatrices that can be formed with the current column as the rightmost boundary and updates the `sumv` array accordingly.
Finally, it adds the values in `sumv` to the total count `ans` and returns it.
The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the matrix, as it processes each cell exactly once and uses a stack to maintain the indices of columns efficiently.
"""