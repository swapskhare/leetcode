import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            h1 = abs(heapq.heappop(stones))
            h2 = abs(heapq.heappop(stones))
            if h1 != h2:
                heapq.heappush(stones, -abs(h1-h2))
        
        if stones:
            return (-stones[0])
        else:
            return 0
