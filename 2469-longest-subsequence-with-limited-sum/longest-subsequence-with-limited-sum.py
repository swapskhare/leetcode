class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()

        for query in queries:
            count = 0
            for num in nums:
                if query >= num:
                    query -= num
                    count +=1
                else:
                    break
            ans.append(count)

        return ans