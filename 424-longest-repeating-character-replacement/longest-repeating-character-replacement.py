class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        # l, r = 0,0
        # count = defaultdict(int)
        # ans = 0

        # while r < len(s):
        #     count[s[r]] += 1
        #     mf = max(count[s[r]], )
        #     wl = r - l + 1

        #     while wl - mf > k:
        #         count[s[l]] -= 1
        #         l += 1
        #         wl -= 1
            
        #     ans = max(ans, wl)
        #     r += 1

        # return ans 

        l,r = 0,0
        count = defaultdict(int)
        ans = 0
        mf = 0
        for r in range(len(s)):
            count[s[r]] += 1
            mf = max(mf, count[s[r]])
            wlen = r - l + 1
            while  wlen - mf > k:
                count[s[l]] -= 1
                wlen -= 1
                l+=1
            ans = max(ans, wlen)

        return ans
                
