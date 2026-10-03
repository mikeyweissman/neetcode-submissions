class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for i in stones:
            heapq.heappush(heap,-i)

        if not heap:
            return 0

        else:
            for j in range(len(heap)):
                if len(heap) < 1:
                    return 0
                elif len(heap) == 1:
                    return -heap[0]
                
                else:
                    val1 = -heapq.heappop(heap)
                    val2 = -heapq.heappop(heap)

                    if val1 > val2:
                        val1 = val1 - val2
                        heapq.heappush(heap,-val1)
                    
                    elif val1 < val2:
                        val2 = val2 - val1
                        heapq.heappush(heap,-val2)
                        
        return -heap[0]
     