from collections import deque

def bfs(graph, start_v):
    # 시작점 예약
    q = deque()
    visited = {}
    q.append(start_v)
    visited[start_v] = True
    # queue가 비어있을 때까지 반복
    while q:
        # 현재 노드 방문
        cur_v = q.popleft()
        # 다음 노드 예약
        for next_v in graph[cur_v]:
            if next_v not in visited:
                q.append(next_v)
                visited[next_v] = True

graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}

bfs(graph, 0)

