class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robber(nums[1:]), self.robber(nums[:-1]))

    def robber(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2