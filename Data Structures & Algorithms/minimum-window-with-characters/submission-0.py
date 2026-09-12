class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        s2Count = {}

        for i in t:

            s2Count[i]= s2Count.get(i,0) + 1
        
        
        s1Count = {}
        valid = 0
        l = 0
        res = ""
        resLen = float("inf")

        for rIndx,rvalue in enumerate(s):

            if rvalue in s2Count:
                s1Count[rvalue] = s1Count.get(rvalue,0) + 1
                if s1Count[rvalue] == s2Count[rvalue]:
                    valid += 1
                    
            
            while l < rIndx and (s[l] not in s2Count or s1Count[s[l]] > s2Count[s[l]]):
                    if s[l] in s2Count:
                        s1Count[s[l]] -= 1
                    l += 1
            
            if valid == len(s2Count):
                if rIndx - l + 1 < resLen:
                    resLen = len(s[l:rIndx+1])
                    res = s[l:rIndx+1]
                    

        return res



