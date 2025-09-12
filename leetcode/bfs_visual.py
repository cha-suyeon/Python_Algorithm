from collections import deque
import time # 시각적인 효과를 위해 time.sleep을 사용해봅니다.

def bfs_visual(graph, start_v):
    """
    BFS 탐색 과정을 단계별로 출력하는 함수
    """
    q = deque()
    visited = {}

    print(f"🚀 BFS 탐색 시작! (시작 노드: {start_v})")
    print("-" * 30)

    # 시작점 처리
    q.append(start_v)
    visited[start_v] = True
    print(f"1️⃣ 시작 노드 '{start_v}'를 Queue에 추가하고 방문 처리합니다.")
    print(f"   - 현재 Queue: {list(q)}")
    print(f"   - 방문한 노드: {list(visited.keys())}\n")
    time.sleep(1)


    # queue가 비어있을 때까지 반복
    step = 2
    while q:
        # 현재 노드 방문 (Queue에서 꺼냄)
        cur_v = q.popleft()
        print(f"{step}️⃣ Queue에서 '{cur_v}' 노드를 꺼내 방문합니다.")
        print(f"   - 현재 Queue: {list(q)}")
        time.sleep(1)


        # 인접한 노드들을 확인
        print(f"   - '{cur_v}'의 이웃 노드 {graph[cur_v]}를 확인합니다.")
        for next_v in graph[cur_v]:
            if next_v not in visited:
                # 방문하지 않았다면 Queue에 추가하고 방문 처리
                q.append(next_v)
                visited[next_v] = True
                print(f"     -> '{next_v}'는 첫 방문! Queue에 추가하고 방문 처리합니다.")
            else:
                # 이미 방문했다면 넘어감
                print(f"     -> '{next_v}'는 이미 방문한 노드입니다.")

        print(f"   - 최종 Queue: {list(q)}")
        print(f"   - 방문한 노드: {list(visited.keys())}\n")
        step += 1
        time.sleep(2) # 다음 단계로 넘어가기 전 잠시 대기

    print("✅ Queue가 비어있으므로 탐색을 종료합니다.")
    print(f"최종 방문 순서: {list(visited.keys())}")


# 기존 그래프 데이터
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

# 시각화 함수 실행
bfs_visual(graph, 0)