import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for x,y in points:
            heapq.heappush(heap,(x**2+y**2,(x,y)))
            print(x**2+y**2)
            
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans