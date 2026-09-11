class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1count = {}

        for i in s1:
            s1count[i] = s1count.get(i,0) + 1
        

        s2count = {}
        l = 0

        for r,rvalue in enumerate(s2):

            if rvalue not in s1count:
                l = r+1
                s2count = {}
                continue
            
            s2count[rvalue] = s2count.get(rvalue,0) +1
            
            while s2count[rvalue] > s1count[rvalue]:
                s2count[s2[l]] -= 1
                l += 1
            

            if s1count == s2count:
                return True
        
        return False
            
            
            
