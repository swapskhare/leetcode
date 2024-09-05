class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0

        while left <= right:
            ans = max (ans, abs((right-left)*min(height[left],height[right]))) 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans