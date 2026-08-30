class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        numSorted = sorted(nums)
        res = set()

        for i in range(len(numSorted)):     
            l = i+1
            r = len(numSorted) - 1

            while(l < r):
                if(-numSorted[i] == numSorted[l] + numSorted[r]):
                    res.add((numSorted[i],numSorted[r],numSorted[l]))
                    l += 1
                    r -= 1
                elif (-numSorted[i] > numSorted[l] + numSorted[r]):
                    l += 1
                else:
                    r -= 1
        
        return [list(x) for x in res]
