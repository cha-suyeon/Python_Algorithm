from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # 1. visited를 빈 딕셔너리로 초기화합니다.
        visited = {}

        def dfs(current_room):
            # 2. 딕셔너리의 키로 방 번호를 넣고, 값으로 True를 주어 방문을 기록합니다.
            visited[current_room] = True
            
            for next_room in rooms[current_room]:
                # 딕셔너리에서도 'in'은 키가 있는지 확인하므로 이 부분은 동일합니다.
                if next_room not in visited:
                    dfs(next_room)
        
        # 0번 방에서부터 탐색 시작
        dfs(0)
        
        # 딕셔너리의 길이는 키의 개수이므로, 이 부분도 동일합니다.
        return len(visited) == len(rooms)

# --- 실행 예시 ---
solution = Solution()
rooms = [[1],[2],[3],[]]
answer = solution.canVisitAllRooms(rooms)
print(f"딕셔너리 사용 결과: {answer}")

rooms_false = [[1,3],[3,0,1],[2],[0]]
answer_false = solution.canVisitAllRooms(rooms_false)
print(f"딕셔너리 사용 결과 (False 케이스): {answer_false}")