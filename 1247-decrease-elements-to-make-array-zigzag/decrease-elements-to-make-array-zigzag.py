class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        n = len(nums)
        zig, zag = 0,0

        for i in range(n):
            if i>0:
                left = nums[i-1]
            else:
                left = float('inf')
            if i <n-1:
                right = nums[i+1]
            else:
                right = float('inf')
            
            target = min(left,right) -1

            if i%2 == 0:
                zig += max(0, nums[i]-target)
            else:
                zag += max(0, nums[i]-target)
            
        return min(zig, zag)