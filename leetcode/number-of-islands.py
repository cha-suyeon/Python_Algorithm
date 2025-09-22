from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False] * col_len for _ in row_len]
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        def dfs(r, c):
            visited[r][c] = True
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr < row_len and 0 <= nc < col_len:
                    if grid[nr][nc] == '1' and not visited[nr][nc]:
                        dfs(nr, nc)
                        
        island_count = 0
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == '1' and not visited[r][c]:
                    island_count += 1
                    dfs(r, c)
                    
        return island_count