class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numslist = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numslist:
                length = 0

                while (num+length) in numslist:
                    length +=1
                longest = max(longest,length)

        return longest