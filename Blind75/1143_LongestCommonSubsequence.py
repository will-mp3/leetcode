"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted 
without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1] # bottom right diagonal
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

"""
to solve this problem we make us of bottom up dynamic programming and a two dimensional grid of both strings.
we solve this bottoms up by working our way from the bottom right corner of the grid and checking if the two values that make up
that squares coordinates are equal.
if they are equal, add 1 to the lower right diagonal's value and save it in the current position.
if they are not equal we check the value below and to the right and take the max value of the two and insert it into the cell
we add a rightmost and bottommost column and row of zeros to account for the end of the string 
and ensure that the first match is calculated as 1
this may look something like this:
  a b c
a 2 1 1 0
c 1 1 1 0
d 0 0 0 0 <----- start here (c, d)
  0 0 0
this solution runs in O(n^2) quadratic time
"""