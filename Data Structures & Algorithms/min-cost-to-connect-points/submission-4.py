class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        cut = set()
        dis = [float('inf')] * n
        dis[0] = 0

        res = 0

        while len(cut) < n:

            nextElement = -1
            nextDist = float('inf')

            for j in range(n):
                if j not in cut and dis[j] < nextDist:
                    
                    nextDist = dis[j]
                    nextElement = j
            
            res += nextDist
            cut.add(nextElement)

            for i in range(n):
                if i not in cut:
                    distance = abs(points[i][0] - points[nextElement][0]) + abs(points[i][1] - points[nextElement][1])
                    dis[i] = min(dis[i],distance)

        
        return res
