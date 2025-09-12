import time

def dfs_visual(cur_v, graph, visited, depth=0):
    """
    DFS 탐색 과정을 재귀 깊이에 맞춰 들여쓰기로 출력하는 함수
    """
    indent = "    " * depth # 깊이에 따라 들여쓰기 생성
    
    # 현재 노드 방문 처리
    visited[cur_v] = True
    print(f"{indent}📞 '{cur_v}' 노드 방문 및 탐색 시작 (깊이: {depth})")
    time.sleep(1)

    # 인접한 노드들을 확인
    print(f"{indent}   - '{cur_v}'의 이웃 노드 {graph[cur_v]}를 확인합니다.")
    for v in graph[cur_v]:
        print(f"{indent}     -> 이웃 '{v}' 확인 중...")
        if v not in visited:
            print(f"{indent}        '{v}'는 첫 방문! 더 깊이 탐색을 시작합니다.")
            time.sleep(1)
            # 재귀 호출 (더 깊이 들어감)
            dfs_visual(v, graph, visited, depth + 1)
            print(f"{indent}📞 '{v}' 노드에서 탐색을 마치고 '{cur_v}'로 복귀.")
            time.sleep(1)
        else:
            print(f"{indent}        '{v}'는 이미 방문한 노드입니다.")
            
    print(f"{indent}🏁 '{cur_v}' 노드의 모든 이웃 탐색 완료. 이전 노드로 돌아갑니다.")


# 그래프 데이터
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

# 방문 기록을 저장할 딕셔너리와 시작점
visited_nodes = {}
start_node = 0

print(f"🚀 DFS 탐색 시작! (시작 노드: {start_node})")
print("-" * 40)
dfs_visual(start_node, graph, visited_nodes)
print("-" * 40)
print(f"✅ 탐색 종료. 최종 방문 순서: {list(visited_nodes.keys())}")