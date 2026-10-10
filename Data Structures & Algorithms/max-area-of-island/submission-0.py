class Solution:

    
    def dfs(self,r,c,grid) -> int:
        if (
            r < 0
            or
            r > len(grid) - 1
            or 
            c < 0
            or
            c > len(grid[0]) - 1
            or
            grid[r][c] != 1
        ):
            return 0

        grid[r][c] = 0

        return 1 + self.dfs(r-1,c,grid) + self.dfs(r+1,c,grid) + self.dfs(r,c-1,grid) + self.dfs(r,c+1,grid) 


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                   res = max(res,self.dfs(i,j,grid))
        

        return res