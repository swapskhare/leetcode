class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posarr, negarr = [], []

        for num in nums:
            if num <0:
                negarr.append(num)
            else:
                posarr.append(num)

        ans = []
        for i in range(len(posarr)):
            ans.append(posarr[i])
            ans.append(negarr[i])

        return ans