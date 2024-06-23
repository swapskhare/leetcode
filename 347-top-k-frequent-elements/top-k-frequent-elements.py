import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for key,val in counts.items():
            heapq.heappush(heap, (val,key))
            if len(heap)>k:
                heapq.heappop(heap)
    
        return [x[1] for x in heap]