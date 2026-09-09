class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = {}

        for i in s1:
            count[i] = count.get(i,0) + 1
        
        currCount = {}
        l = 0

        for r in range(len(s2)):

            if s2[r] not in s1:
                currCount = {}

            if s2[r] in s1:
                currCount[s2[r]] = currCount.get(s2[r],0) + 1

                while currCount.get(s2[r],0) > count[s2[r]]:
                    if s2[l] in s1:
                        currCount[s2[l]] -= 1
                    l += 1
            
            if currCount == count:
                return True
        
        return False
            

