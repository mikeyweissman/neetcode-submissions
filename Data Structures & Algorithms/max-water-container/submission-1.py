class Solution:
    def maxArea(self, heights: List[int]) -> int: 
        l = 0
        r = len(heights) - 1
        resMax = 0
        
        while(l < r):
            length = r - l
            h = min(heights[l],heights[r])

            curArea = length * h
            if curArea > resMax:
                resMax = curArea

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return resMax
            
            