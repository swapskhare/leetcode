from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rotten = []
        oranges = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c,0))
                if grid[r][c] == 1:
                    oranges += 1

        queue = deque(rotten)
        minutes = 0
        
        while queue:
            r, c, level = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr >= 0 and nr < ROWS and 
                    nc >= 0 and nc < COLS and 
                    grid[nr][nc] == 1):

                    queue.append((nr, nc, level + 1))
                    minutes = max(minutes, level + 1)
                    grid[nr][nc] = 2
                    oranges -= 1
        
        if oranges > 0:
            return -1
        else: return minutes

