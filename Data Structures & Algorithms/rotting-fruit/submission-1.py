class Solution:
    def add(self,grid,r,c):
        
        if(
            r<0 
            or
            r>len(grid)-1
            or
            c<0
            or
            c>len(grid[0])-1
            or
            grid[r][c] != 1
        ):
            return
        
        self.count -= 1
        grid[r][c] = 2
        self.queue.append([r,c])

        return
    
    def bfs(self,grid):
        while self.queue:
            for i in range(len(self.queue)):
                r,c = self.queue.popleft()
                self.add(grid,r+1,c)
                self.add(grid,r-1,c)
                self.add(grid,r,c+1)
                self.add(grid,r,c-1)

            self.res += 1
        
        return


    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.queue = deque()
        self.res = -1
        self.count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    
                    self.queue.append([i,j])
                
                if grid[i][j] == 1:
                    self.count += 1
        
        if self.count == 0:
            return 0

        self.bfs(grid)
        
        if self.count > 0:
            return -1

        return self.res
        
        
        
        
               
