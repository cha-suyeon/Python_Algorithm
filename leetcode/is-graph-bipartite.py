from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # 1. 각 노드의 색상을 저장할 배열을 준비합니다.
        #    -1: 아직 색칠되지 않음
        #     0: 첫 번째 색상
        #     1: 두 번째 색상
        color = [-1] * len(graph)
        
        # 2. 그래프가 여러 덩어리로 나뉘어 있을 수 있으므로 모든 노드를 순회합니다.
        for i in range(len(graph)):
            
            # 3. 아직 색칠되지 않은 노드(새로운 덩어리의 시작점)를 발견하면
            if color[i] == -1:
                
                # BFS를 위한 큐를 만들고 시작 노드를 추가합니다.
                # 큐에는 (노드 번호, 색상) 튜플을 넣습니다.
                queue = deque([(i, 0)])
                color[i] = 0 # 시작 노드를 첫 번째 색상(0)으로 칠합니다.
                
                # 4. 큐가 비어있지 않는 동안 탐색을 계속합니다.
                while queue:
                    cur_node, cur_color = queue.popleft()
                    
                    # 5. 현재 노드에 연결된 모든 이웃 노드를 확인합니다.
                    for neighbor in graph[cur_node]:
                        
                        # 6. 이웃 노드가 아직 색칠되지 않았다면
                        if color[neighbor] == -1:
                            # 이웃 노드를 현재 노드와 다른 색상으로 칠합니다.
                            new_color = 1 - cur_color
                            color[neighbor] = new_color
                            # 그리고 큐에 추가합니다.
                            queue.append((neighbor,new_color))
                            # 여기에 코드를 작성하세요
                        
                        # 7. 이웃 노드가 이미 색칠되어 있다면
                        elif color[neighbor] == cur_color:
                            # 색깔이 현재 노드와 같은지 확인합니다.
                            # 만약 같다면, 이분 그래프가 아니므로 False를 반환합니다.
                            return False
                            
        # 8. 모든 노드를 성공적으로 색칠했다면
        return True
    
# --- 예시 실행 부분 ---
if __name__ == "__main__":
    solution = Solution()

    # 예시 1: false가 나와야 하는 경우
    graph_false = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(f"Graph 1: {graph_false}")
    print(f"Is bipartite? {solution.isBipartite(graph_false)}\n")

    # 예시 2: true가 나와야 하는 경우
    graph_true = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(f"Graph 2: {graph_true}")
    print(f"Is bipartite? {solution.isBipartite(graph_true)}\n")

    # 추가 예시: 여러 덩어리로 나뉜 그래프
    graph_disconnected = [[1], [0], [], [5], [6], [3, 6], [4, 5]]
    print(f"Graph 3: {graph_disconnected}")
    print(f"Is bipartite? {solution.isBipartite(graph_disconnected)}\n")

    # 추가 예시: 홀수 길이의 사이클 (false)
    graph_cycle = [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]]
    print(f"Graph 4: {graph_cycle}")
    print(f"Is bipartite? {solution.isBipartite(graph_cycle)}")