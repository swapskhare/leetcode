class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            m = (left + right) // 2
            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m

        pivot = left
        
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        return result if result != -1  else  binary_search(pivot, len(nums) - 1)