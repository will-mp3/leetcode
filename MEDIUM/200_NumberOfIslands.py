"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # check that row/col is in bounds, is land, and hasnt been visited
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands

"""
to solve this problem we make use of a breadth first search algorithm.
unlike dfs, bfs is iterative and rather simple.
the way this solution works if after setting up our variables, namely the grid size, visit set, and island counter, we iterate over the grid.
once a cell is found that is both a 1 (land) and is not in our visited set we call our bfs function and add a discovered island.
we then perform our bfs on this cell, purpose being to find all of the 1s connected and add them to our visited set.
once the bfs function has finished in all directions and our queue is empty (no more 1s found), we continue traversing the grid.
this traversal continues until we find another 1 which meets the original criteria of not being visited or the grid ends.
"""