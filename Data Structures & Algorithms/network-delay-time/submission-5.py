class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        heap = []
        d = [float('inf')] * (n+1)
        d[k] = 0
        start = k
        seen = set()
        graph = {}

        for i in times:
            if i[0] not in graph:
                graph[i[0]] = []

            graph[i[0]].append([i[1],i[2]]) 

        heapq.heappush(heap,[0,k])

        while heap:

                dis,node = heapq.heappop(heap)

                if node in seen:
                    continue

                seen.add(node)    

                d[node] = min(d[node],dis)
                if node in graph:
                    for target,weight in graph[node]:
                        if target not in seen:
                            heapq.heappush(heap,[d[node]+weight,target])

                
            

        
        return max(d[1:]) if max(d[1:]) != float('inf') else -1
                


