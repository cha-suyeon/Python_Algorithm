from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        start_v = 0
        q = deque()
        visited = {}
        
        q.append(start_v)
        print(f"1st Queue: {q}")
        
        visited[start_v] = True
        print(f"1st visited: {visited}")
        
        while q:
            cur_v = q.popleft()
            for next_v in rooms[cur_v]:
                if next_v not in visited:
                    q.append(next_v)
                    visited[next_v] = True
        
        print(f"visited: {visited}")
        print(f"visited: {len(visited)}")
            
        return len(rooms) == len(visited)
        
# --- 실행 예시 ---
solution = Solution()
rooms = [[1],[2],[3],[]]
answer = solution.canVisitAllRooms(rooms)
print(answer)        