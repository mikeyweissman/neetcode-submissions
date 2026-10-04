class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for x,y in points:
            dis = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(heap,[-dis,x,y])
            if len(heap) > k:
                heapq.heappop(heap)
            

        
        return [[x,y] for i,x,y in heap]