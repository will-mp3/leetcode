"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dynamic programming: bottom up
        # recursion: top down
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {} # map each r,c position to max length of square

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)


            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2

"""
this problem can be solved effeciently either using recursion or dyanmic programming.
the idea is we must go through unvisited cells in a 2d array and mark them based on the amount of neighboring ones.
dynamic programming takes a bottom up approach whereas recursion takes a top down approach.
for this solution we will opt for the recursive implementation.
the idea is that we go through each unvisited cell, starting top left, and check its right, diagonal, and lower neighbors.
with each check, we increment the value held in the cache based on its maximum length (we will square this at the end).
to implement this we will define a helper function which I'll explain later.
to start we must define our cache which will be represented by a hash table, we are mapping our (r,c) positions to their max square length.
our helper variable takes in a starting position and calls itself recursively, we start at 0,0.
the first thing we check is the base case, which happens when either of our coordinates are out of bound.
if the base case dosent execute and the current cell is unvisited, we call our helper function on our right, diagonal, and lower neighbor.
this will traverse the entire matrix and get us to the bottom right position where the recursive call stack will begin returning.
now we map the current cell in the cache to zero, and check if it contains a 1 in our original matrix.
if the cell contains a 1, we map 1 + the minimum of its three neighbors to our cache.
what this is doing is checking to see that all its square neighbors also contain ones, and if their neighbors contains ones and so on.
once the recursion finishes we return our finished cache and return the max value from it squared.
this solution runs in O(m * n) time where m is the number of rows and n is the number of columns.
"""