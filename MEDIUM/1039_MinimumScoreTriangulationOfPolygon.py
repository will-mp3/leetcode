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
This code defines a solution to find the minimum possible score of triangulating a convex polygon with given vertex values. The function `minScoreTriangulation` takes a list of integers `values` representing the vertex values of the polygon and returns an integer representing the minimum score achievable through triangulation. The approach used in this solution can be broken down into the following steps:
1. Initialize a 2D list `dp` to store the minimum scores for subproblems, where `dp[i][j]` represents the minimum score for triangulating the polygon formed by vertices from index `i` to index `j`.
2. Define the recursive function `minScoreTriangulation` with parameters `i` and `j` representing the current segment of the polygon being considered. If `j` is not provided, it is set to the last index of the `values` list.
3. If the value for `dp[i][j]` has already been computed (i.e., it is not zero), return that value to avoid redundant calculations.
4. Iterate through all possible vertices `k` between `i` and `j` to form triangles. For each vertex `k`, calculate the score of the triangle formed by vertices `i`, `k`, and `j`, and recursively compute the minimum scores for the two resulting sub-polygons: one from `i` to `k` and the other from `k` to `j`.
5. Update the result `res` with the minimum score found during the iterations.
6. Store the computed minimum score in `dp[i][j]` and return it.
The time complexity of this solution is O(n^3), where n is the number of vertices in the polygon, due to the three nested loops (one for the range of `i` to `j` and two for the recursive calls). The space complexity is O(n^2) for storing the `dp` table.
"""