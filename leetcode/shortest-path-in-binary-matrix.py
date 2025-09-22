from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortest_dist = -1
        row_len = len(grid)
        col_len = len(grid[0])
        
        if grid[0][0] == 1 or grid[row_len -1][col_len - 1] == 1:
            return shortest_dist
        
        visited = [[False] * col_len for _ in range(row_len)]
        dr = [0, 1, 1, 1, 0, -1, -1, -1]
        dc = [1, 1, 0, -1, -1, -1, 0, 1]
        
        queue = deque()
        queue.append((0, 0, 1))
        visited[0][0] = True
        
        while queue:
            cur_r, cur_c, cur_dist = queue.popleft()
            if cur_r == row_len -1 and cur_c == col_len - 1:
                shortest_dist = cur_dist
                break
            for i in range(8):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if (0 <= next_r < row_len) and (0 <= next_c < col_len):
                    if grid[next_r][next_c] == 0:
                        if not visited[next_r][next_c]:
                            queue.append((next_r, next_c, cur_dist + 1))
                            visited[next_r][next_c] = True
                            
        return shortest_dist