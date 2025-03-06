"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, n in enumerate(row): # enumerate to access value and index at same time
                dp[i] = n + min(dp[i], dp[i + 1]) # overwrite position i with minimum of children below

        return dp[0]

"""
this problem is best visualized as a tree because the adjacent step mechanic is best compared to children in a tree.
for example the first rows first element, row1[0], will have children row2[0] & row2[1] which are accessible.
with that understood we want to approach this problem using dynamic programming.
starting from the bottom we can calculate the minimum path for each value.
we start by initializing an array of length triangle + 1 full of zeroes, this represents the row right below our last row.
we iterate through every row in triangle, starting from the bottom, and every value in the row.
for each value we check the minimum of its two children which are currently stored in our dp array.
this array more specifically holds the shortest path of the children and is continually updated until it reachs the top, dp[0].
the minimum of the current values child paths is used to overwrite the current value and the loop continues.
this is done for every value and by the time it reaches the top we can return our top value, dp[0].
this solutions runs in roughly O(n^2) time.
"""