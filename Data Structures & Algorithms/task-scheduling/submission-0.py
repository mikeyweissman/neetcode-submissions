class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cooldown = deque()

        count = [0] * 26

        for i in tasks:
            count[ord(i)-ord('A')] += 1
        
        heap = [-i for i in count if i>0]
        heapq.heapify(heap)
        
        t = 0

        while heap or cooldown:
            if heap:
                task = heapq.heappop(heap)
                if task+1 < 0:
                    cooldown.append([task + 1,t + n])

            if cooldown and cooldown[0][1] == t:
                heapq.heappush(heap,cooldown[0][0])
                cooldown.popleft()
            
            t += 1

        

        return t