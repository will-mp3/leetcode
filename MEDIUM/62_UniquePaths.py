"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        
        return row[0]

"""
to solve this problem we will use a dynamic programming approach.
we know that the final space, the goal, is in the bottom right corner so like many dp approaches we will start there.
this algorithm works by working backward from that goal position, tallying up the number of possible moves in each square.
we know that you can only move right or down, so to calculate the total amount of moves, 
we add the value stored in fields to the right and below our current index.
the bottom row and rightmost column will be 1 by default since we cannot move down and right respectively.
as we go through the array the numbers add up and ultimately our starting point [0][0] will have the maximum number of combinations.
this solution runs in O(n * m).
"""