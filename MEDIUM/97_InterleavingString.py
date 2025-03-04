"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # initialize 2 dimensional dynamic programming array 
        dp = [ [False] * (len(s2) + 1) for i in range((len(s1) + 1))]
        # initalize bottom right corner value as True
        dp[len(s1)][len(s2)] = True

        # work our way left then up row by row from bottom right corner
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]

"""
this problem makes use of a dynamic programming array for its solution.
to do this we set up a two dimensional array representing the dimensions of our two given strings.
we first initialize every cell to false, these cells will be used as our cache as our algorithm executes.
the basic idea is that, starting from the bottom right corner, 
we check every cell to see if the characters represented by its indices matches the sum of those indices.
an important formula to note is that the index of s1 + the index of s2 will always equal the current index of s3.
this is because the sum of the lengths of s1 and s2 is the same as s3, so as we cross off used characters we naturally move through s3.
with that out of the way lets continue.
we start at the bottom right corner and check two conditions:
if index i is in bounds, the character at s1[i] is equal the character at s3[i + j], and the cell to the right is True.
if all three of these pass, we fill in the current cell with True.
we then check if index j is in bounds, the character at s2[j] is equal the character at s3[i + j], and the cell below is True.
if all three of these pass, we fill in the current cell with True.
if neither of these execute we leave the cell as false and continue.
once complete the loop will have gotten all the way to the top left cell and we can return its value.
"""