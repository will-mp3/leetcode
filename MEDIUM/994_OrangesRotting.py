"""

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        
        queue = collections.deque()
        fresh_oranges = 0
        minutes = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue and fresh_oranges > 0:
            level_size = len(queue)
            progress = False
            
            for i in range(level_size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        progress = True
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))
                        
            if progress:
                minutes += 1
                
        if fresh_oranges == 0:
            return minutes
        else:
            return -1

"""

"""