import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # counts = {}
        # for num in nums:
        #     counts[num] = 1 + counts.get(num, 0)
        
        # heap = []
        # for num in counts.keys():
        #     heapq.heappush(heap,(counts[num],num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])

        # return res

        count = {}
        freq  = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
               
