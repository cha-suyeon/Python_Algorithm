from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(cur_v):
            visited.add(cur_v)
            
            for next_v in rooms[cur_v]:
                if next_v not in visited:
                    dfs(next_v)
                    
        dfs(0)
        
        return len(visited) == len(rooms)
   
# --- 실행 예시 ---
solution = Solution()
rooms = [[1],[2],[3],[]]
answer = solution.canVisitAllRooms(rooms)
print(answer) # True가 올바르게 출력됩니다.

rooms_false = [[1,3],[3,0,1],[2],[0]]
answer_false = solution.canVisitAllRooms(rooms_false)
print(f"(False 케이스): {answer_false}")
