"""
You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 109 + 7.
"""

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9+7
        freq = Counter(p[1] for p in points)
        Sum, c2 = 0, 0

        for f in freq.values():
            if f <= 1:
                continue
            c = f * (f - 1) // 2
            Sum += c
            c2 += c * c
        return (Sum * Sum - c2) // 2 % MOD

"""

"""