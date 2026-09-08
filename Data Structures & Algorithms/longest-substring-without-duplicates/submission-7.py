class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        seen = set()
        l = 0
        r = l

        while(r < len(s)):
            if s[r] in seen:
                while(s[l] != s[r]):
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            r += 1

            res = max(res,len(seen))

        return res