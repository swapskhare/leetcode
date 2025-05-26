import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        direction = [(0,1), (1,0), (-1,0), (0,-1)]

        visit.add((0,0))

        while minHeap:
            t, r, c  = heapq.heappop(minHeap)
            visit.add((r,c))

            if r == N-1 and c == N -1:
                return t
            for dr,dc in direction:
                nr, nc = r + dr, c + dc

                if nr<0 or nc<0 or nr == N or nc == N or (nr, nc) in visit:
                    continue
                visit.add((nr,nc))
                heapq.heappush(minHeap, [max(t,grid[nr][nc]), nr, nc])

            

