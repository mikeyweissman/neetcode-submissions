class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = l + 1
        maxProfit = 0

        while (l < r and r< len(prices)):
            currProf = prices[r] - prices[l]
            if currProf > maxProfit:
                maxProfit = currProf
            
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        
        return maxProfit