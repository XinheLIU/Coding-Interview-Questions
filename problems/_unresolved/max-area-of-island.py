class Solution:    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area,self.Dfs(grid,i,j,1))
                    
        return max(0,max_area)
    
    def Dfs(self,grid,i,j,count):
        grid[i][j] = -1 # or 0
        for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if m>=0 and m< len(grid) and n>=0 and n<len(grid[0]) and grid[m][n] == 1:
                count = 1 + self.Dfs(grid,m,n,count)
        return count 