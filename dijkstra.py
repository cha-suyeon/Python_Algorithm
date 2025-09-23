import heapq

def dijkstra(graph, start, end, V):
    """
    다익스트라 알고리즘을 사용하여 최단 경로를 찾습니다.

    Args:
        graph (list): 인접 리스트 형태의 그래프. graph[i]는 (연결된 정점, 가중치) 튜플의 리스트입니다.
        start (int): 출발 정점.
        end (int): 도착 정점.
        V (int): 총 정점의 개수.
    """
    # 각 정점까지의 최단 거리를 저장하는 리스트, 초깃값은 무한대(inf)
    distance = [float("inf")] * (V + 1)
    
    # 시작 정점의 거리는 0으로 초기화
    distance[start] = 0
    
    # 우선순위 큐(최소 힙)를 생성하고, 시작 정점 정보를 넣음
    q = []
    # (거리, 정점) 순서로 저장해야 거리가 짧은 순으로 정렬됨
    heapq.heappush(q, (0, start))
    
    while q:
        # 현재 가장 거리가 짧은 정점 정보를 큐에서 꺼냄
        dist, now_node = heapq.heappop(q)
        
        # 이미 처리된 정점이라면(더 짧은 경로를 이미 찾았다면) 무시
        if distance[now_node] < dist:
            continue
            
        # 현재 정점과 연결된 다른 인접 정점들을 확인
        for neighbor_node, weight in graph[now_node]:
            # 현재 정점을 거쳐서 다른 정점으로 이동하는 비용 계산
            cost = dist + weight
            
            # 현재 정점을 거쳐 가는 것이 기존 경로보다 더 짧은 경우
            if cost < distance[neighbor_node]:
                # 최단 거리 갱신
                distance[neighbor_node] = cost
                # 갱신된 정보를 큐에 삽입
                heapq.heappush(q, (cost, neighbor_node))
                
    # 도착 정점까지의 최단 거리를 반환
    return distance[end]

# --- 예시 사용법 ---
if __name__ == '__main__':
    V = 6  # 정점 6개
    graph = [[] for _ in range(V + 1)] # 1번부터 6번 정점 사용
    
    # 그래프 정보 (출발, 도착, 비용)
    edges = [
        (1, 2, 2), (1, 3, 5), (1, 4, 1),
        (2, 3, 3), (2, 4, 2),
        (3, 2, 3), (3, 6, 5),
        (4, 3, 3), (4, 5, 1),
        (5, 3, 1), (5, 6, 2)
    ]
    
    for u, v, w in edges:
        graph[u].append((v, w))
        
    start_node = 1
    end_node = 6
    
    # 다익스트라 알고리즘 실행
    shortest_path = dijkstra(graph, start_node, end_node, V)
    
    if shortest_path == float('inf'):
        print(f"경로 없음: {start_node} -> {end_node}")
    else:
        # 예상 결과: 1 -> 4 -> 5 -> 6 (비용: 1 + 1 + 2 = 4)
        print(f"최단 거리 ({start_node} -> {end_node}): {shortest_path}")

# 출력 결과:
# 최단 거리 (1 -> 6): 4