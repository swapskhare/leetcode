import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        ans = 0


        for i in range(k):
            x = heapq.heappop(heap)
            heapq.heappush(heap, x - int(x/2))
            # ans += x - int(x/2)

        while heap:
            ans += heapq.heappop(heap)


        return -ans