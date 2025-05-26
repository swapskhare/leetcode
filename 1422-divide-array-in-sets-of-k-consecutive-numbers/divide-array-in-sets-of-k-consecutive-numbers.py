import heapq

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        l = len(nums)

        if l%k != 0:
            return False

        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1

            if count[num] > l/k:
                return False

        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first, first + k):
                if count[i] == 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i == heap[0]:
                        heapq.heappop(heap)
                    else:
                        heap.remove(i)
                        heapq.heapify(heap)


        
        

        return True