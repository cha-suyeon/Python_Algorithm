from collections import deque

def topological_sort(node_num, prerequisites):
    """
    Kahn의 알고리즘을 사용한 위상 정렬 함수입니다.

    Args:
        node_num (int): 전체 노드(정점)의 개수.
        prerequisites (list): [v, u]는 u가 v의 선수과목임을 의미 (u -> v).
    """
    # 1. 그래프(인접 리스트) 및 진입 차수(indegree) 배열 초기화
    graph = [[] for _ in range(node_num)]
    indegree = [0] * node_num
    
    # 2. 그래프 구성 및 진입 차수 계산
    for v, u in prerequisites:
        graph[u].append(v)  # u -> v 간선 추가
        indegree[v] += 1
        
    # 3. 진입 차수가 0인 노드를 큐에 추가
    q = deque()
    for v in range(node_num):
        if indegree[v] == 0:
            q.append(v)
            
    result = [] # 위상 정렬 결과 리스트
    
    # 4. 큐가 빌 때까지 반복
    while q:
        cur_v = q.popleft()
        result.append(cur_v)
        
        # 현재 노드에서 나가는 간선 제거 (논리적으로)
        for next_v in graph[cur_v]:
            indegree[next_v] -= 1
            
            # 새롭게 진입 차수가 0이 된 노드를 큐에 추가
            if indegree[next_v] == 0:
                q.append(next_v)
                
    # 5. 순환(Cycle) 존재 여부 확인 후 결과 반환
    if len(result) == node_num:
        return result  # 순환이 없으면 정렬된 결과 반환
    else:
        return []      # 순환이 있으면 빈 리스트 반환
    
# 예시 1: 순환이 없는 경우
nodes1 = 4
# 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
prereqs1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(f"정렬 결과 1: {topological_sort(nodes1, prereqs1)}")
# 출력 결과 1: [0, 1, 2, 3] 또는 [0, 2, 1, 3] (정답은 여러 개일 수 있음)

# 예시 2: 순환이 있는 경우
nodes2 = 3
# 0 -> 1 -> 2 -> 0
prereqs2 = [[1, 0], [2, 1], [0, 2]]
print(f"정렬 결과 2: {topological_sort(nodes2, prereqs2)}")
# 출력 결과 2: []