from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh_count = 0
        rotten = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    rotten.append((r, c))

        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]
        minutes = 0
        while rotten:
            level_size = len(rotten)
            minutes += 1

            for _ in range(level_size):
                # process
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr >= 0 and nr < ROWS and
                        nc >= 0 and nc < COLS and
                        grid[nr][nc] == 1
                    ):
                        rotten.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh_count -= 1
        if minutes:
            minutes -= 1       

        return -1 if fresh_count > 0 else minutes