"""
You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

Count the number of pairs of points (A, B), where

A is on the upper left side of B, and
there are no other points in the rectangle (or line) they make (including the border).
Return the count.
"""

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sort by x descending, then y ascending
        points.sort(key=lambda p: (-p[0], p[1]))
        n = len(points)
        res = 0

        for i in range(n - 1):
            minY = 1 << 31  # like +infinity
            for j in range(i + 1, n):
                # condition: points[i] is upper-left of points[j]
                if minY > points[j][1] >= points[i][1]:
                    res += 1
                    minY = points[j][1]  # update "lowest seen" y
        return res

"""

"""