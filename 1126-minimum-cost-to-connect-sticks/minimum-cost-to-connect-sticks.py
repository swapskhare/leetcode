import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks
        heapq.heapify(heap)
        ans = 0
        
        while len(heap)>1:
            x1 = heapq.heappop(heap)
            x2 = heapq.heappop(heap)
            ans += (x1 + x2)
            heapq.heappush(heap, x1+x2)
                
        return ans