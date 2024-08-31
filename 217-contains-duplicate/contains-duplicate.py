class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = set()
        for n in nums:

            if n in num:
                return True
            else:
                num.add(n)
        return False