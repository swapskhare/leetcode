class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        res = 0
        visited = set()

        def dfs(r, c):
            if (r<0 or c<0 or r==ROWS or c==COLS or grid2[r][c] == 0 or (r,c) in visited):
                return True
            
            visited.add((r,c))
            isSub = True
            if grid1[r][c] == 0:
                isSub = False

            isSub = dfs(r + 1, c) and isSub
            isSub = dfs(r -1, c) and isSub
            isSub = dfs(r, c + 1) and isSub
            isSub = dfs(r, c - 1) and isSub

            return isSub

            

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r,c) not in visited and dfs(r,c):
                    res += 1
        return res
