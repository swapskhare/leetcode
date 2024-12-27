class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        if len(s) < len(t):
            return ""

        left = 0
        right = 0
        
        count = {}
        wcount = {}

        
        res = [-1,-1]
        reslen = math.inf
        minlen = 0
        
        for char in t:
            count[char] = 1 + count.get(char,0)

        have = 0
        need = len(count)

        for right in range(len(s)):
            char = s[right]
            wcount[char] = 1 + wcount.get(char,0)

            if char in count and wcount[char] == count[char]:
                have += 1

                while have == need:
                    wlen = right - left + 1
                    if wlen <=  reslen:
                        res = [left,right]
                        reslen = min(reslen, wlen)

                    wcount[s[left]] -=1
                    if s[left] in count and wcount[s[left]] < count[s[left]]:
                        have -= 1
                    left +=1
        return s[res[0]:res[1]+1] if reslen != math.inf else ""

