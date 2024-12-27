"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, 
and the rain water can flow to neighboring cells directly north, south, east, and west 
if the neighboring cell's height is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where 
result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

"""
for this problem we have a two dimensional array of values with the top row and left column bordered by the pacific ocean
and the bottom row and right column bordered by the atlantic ocean.
our approach will be using recursive depth first search function.
the idea is we want to find every cell that can reach the pacific ocean and cache it 
and then find every cell that can reach the atlantic and cache it.
once we have found all of those result our solution will be the overlapping cells, those which are in both the pac and atl cache.
our recursive function starts by finding all of the cells that can reach the pacific in the top row.
the recursive function then works to find all of those neighbors which can reach the pacific as well.
this logic is repeated for the bottom row and the atlantic, the leftmost column and the pacific, and the rightmost column and the atlantic.
once done we iterate through each cell and check if its been saved both in atl and pac, if so append to result and return.
this solution is costly but it is about as effecient as possible. it runs in O((r + c)^2)
"""