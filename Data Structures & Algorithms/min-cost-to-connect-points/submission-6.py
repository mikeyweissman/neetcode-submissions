class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        heap = []
        seen = set()
        cost = 0

        heap.append([0,0])
        while heap:
            if len(seen) == len(points):
                break

            weight,node= heapq.heappop(heap)
            if node in seen:
                continue
                
            cost += weight  
            seen.add(node)

            for i,(x2,y2) in enumerate(points):
                if i in seen:
                    continue

                dis = abs(points[node][0]-x2) + abs(points[node][1]-y2)
                heapq.heappush(heap,[dis,i])

            

        
        return cost





