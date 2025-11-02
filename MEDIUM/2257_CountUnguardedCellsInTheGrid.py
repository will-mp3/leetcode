"""
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.
"""

class Solution:
    def countUnguarded(self, R: int, C: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # create 2d grid
        grid = [[0] * C for _ in range(R)]
        total = R * C
        # mark walls and guards
        for r,c in walls + guards:
            grid[r][c] = 2
            total -= 1
        # for each guard search 4 directions and mark what it sees, if a guard/wall is seen stop
        for x,y in guards:
            for dr,dc in (0,1),(1,0),(0,-1),(-1,0):
                r,c = x + dr,y + dc
                while C > c >= 0 <= r < R and grid[r][c] != 2:
                    total -= grid[r][c] == 0
                    grid[r][c] = 1
                    r += dr
                    c += dc
        return total

"""
This solution first initializes a grid and marks the positions of walls and guards. 
It then iterates through each guard and explores the four cardinal directions, marking cells as guarded until it encounters a wall or another guard. 
The total number of unguarded cells is updated accordingly and returned at the end.
The time complexity of this solution is O(G * (R + C)), where G is the number of guards, R is the number of rows, and C is the number of columns in the grid.
"""