class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = float('inf')

        while l <= r:

            mid = (l + r) // 2
            sum = 0
            for i in piles:
                sum += (i + mid -1 ) // mid
            
            if sum <= h:
                res = min(res,mid)
                r = mid -1 
            else:
                l = mid + 1
        

        return int(res)

