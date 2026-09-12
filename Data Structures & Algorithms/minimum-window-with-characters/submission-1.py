class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        s1count = {}

        for i in t:
            s1count[i] = s1count.get(i,0) + 1
        

        s2count = {}
        l = 0
        res = ''
        resLen = float("inf")
        valid = 0


        for r, rvalue in enumerate(s):

            if rvalue in s1count:
                s2count[rvalue] = s2count.get(rvalue,0) + 1
                if s2count[rvalue] == s1count[rvalue]:
                    valid += 1
            
            while valid == len(s1count):

                if r-l+1 < resLen:
                        res = s[l:r+1]
                        resLen = r-l+1

                if s[l] in s1count:
                    s2count[s[l]] -= 1
                    if s2count[s[l]] < s1count[s[l]]:
                        valid -= 1
                        
                l += 1
        
        return res
            



            
