class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        count=0
        def dfs(r,c):
            #check boundaries
            if(r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0"):
                return
            #mark as visited
            grid[r][c]="0"
            #explore all directions
            dfs(r-1,c)#up
            dfs(r+1,c)#down
            dfs(r,c-1)#left
            dfs(r,c+1)#right
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    count+=1
                    dfs(r,c)
        return count