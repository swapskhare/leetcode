class Solution:
    def mostFreq(self, count):
        mf = 0
        for key,value in count.items():
            mf = max(mf,value)

        return mf

    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        count = defaultdict(int)
        ans = 0

        while r < len(s):
            count[s[r]] += 1
            mf = self.mostFreq(count)
            wl = r - l + 1

            while wl - mf > k:
                count[s[l]] -= 1
                l += 1
                wl -= 1
                mf = self.mostFreq(count)
            
            ans = max(ans, wl)
            r += 1

        return ans 
