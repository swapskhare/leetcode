class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def bin_search(arr,target):
            left = 0
            right = len(arr)-1
            while left<= right:
                mid = (right+left)//2
                if arr[mid]<target:
                    left= mid +1
                else:
                    right = mid-1
            return left
        
        potions.sort()
        ans = []
        m = len(potions)

        for spell in spells:
            i = bin_search(potions,success/spell)
            ans.append(m-i)

        return ans