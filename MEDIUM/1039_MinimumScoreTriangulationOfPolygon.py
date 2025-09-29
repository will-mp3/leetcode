"""
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.

You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.

Return the minimum possible score that you can achieve with some triangulation of the polygon.
"""

class Solution:
    def __init__(self):
        self.dp = [[0] * 50 for _ in range(50)]
        
    def minScoreTriangulation(self, values, i=0, j=0, res=0):
        if j == 0:
            j = len(values) - 1
        if self.dp[i][j] != 0:
            return self.dp[i][j]
        for k in range(i + 1, j):
            res = min(res if res != 0 else float('inf'),
                self.minScoreTriangulation(values, i, k) +
                values[i] * values[k] * values[j] +
                self.minScoreTriangulation(values, k, j))
        self.dp[i][j] = res
        return self.dp[i][j]

"""

"""