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
This code defines a solution to count the number of pairs of points (A, B) in a 2D plane such that A is on the upper left side of B and there are no other points in the rectangle formed by A and B.
The `numberOfPairs` method first sorts the list of points in descending order by their x-coordinates and in ascending order by their y-coordinates. This sorting ensures that when iterating through the points, we can efficiently check the conditions for the pairs.
It initializes a variable `res` to keep track of the count of valid pairs. The outer loop iterates through each point as point A, and the inner loop iterates through the subsequent points as point B.
For each pair of points, it checks if point B is on the lower right side of point A (i.e., B's y-coordinate is greater than or equal to A's y-coordinate and less than the minimum y-coordinate seen so far). If this condition is met, it increments the count `res` and updates the minimum y-coordinate seen.
Finally, it returns the total count of valid pairs.
The time complexity of this solution is O(n^2), where n is the number of points, due to the nested loops. The space complexity is O(1) as it uses a constant amount of additional space.
"""