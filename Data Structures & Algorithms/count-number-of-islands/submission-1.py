class Solution:
    def dfs(self,c,r,grid):
        if (
            c < 0
            or
            c > len(grid) - 1
            or
            r > len(grid[0]) - 1
            or 
            r < 0
            or
            grid[c][r] != '1'
        ):
            return
        
        else:
            grid[c][r] = '0'
            self.dfs(c,r+1,grid)
            self.dfs(c+1,r,grid)
            self.dfs(c-1,r,grid)
            self.dfs(c,r-1,grid)
            grid[c][r] = '0'

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1':
                    self.dfs(i,j,grid)
                    res += 1
    

        return res

    

