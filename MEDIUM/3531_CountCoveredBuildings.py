"""
You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

A building is covered if there is at least one building in all four directions: left, right, above, and below.

Return the number of covered buildings.
"""

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rmax = [0] * (n + 1)
        rmin = [n + 1] * (n + 1)
        cmax = [0] * (n + 1)
        cmin = [n + 1] * (n + 1)

        # Track extreme buildings for each row and column
        for x, y in buildings:
            rmax[y] = max(rmax[y], x)
            rmin[y] = min(rmin[y], x)
            cmax[x] = max(cmax[x], y)
            cmin[x] = min(cmin[x], y)

        ans = 0

        # A building is covered only if it's strictly inside both extremes
        for x, y in buildings:
            if rmin[y] < x < rmax[y] and cmin[x] < y < cmax[x]:
                ans += 1

        return ans

"""

"""