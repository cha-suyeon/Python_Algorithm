from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        q = deque([0])
        print(f"1st Queue: {q}")
        
        visited = {0}
        print(f"1st Visited: {visited}")
        
        while q:
            cur_v = q.popleft()
            print(f"Current visit: {cur_v}")
            
            for key in rooms[cur_v]:
                print(f"Key: {key}")
                
                if key not in visited:
                    visited.add(key)
                    print(f"Visited: {visited}")
                    q.append(key)
                    print(f"Queue: {q}")
                    
        return len(rooms) == len(visited)
                    
# --- 실행 예시 ---
solution = Solution()
rooms = [[1],[2],[3],[]]
answer = solution.canVisitAllRooms(rooms)
print(answer)        