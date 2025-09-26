from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        pq = [(0, k)]
        dist = {}

        while pq:
            time, node = heapq.heappop(pq)

            if node in dist:
                continue

            dist[node] = time

            if node in graph:
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(pq, (alt, v))

        if len(dist) == n:
            result = max(dist.values())
            return result
        else:
            return -1

# ===============================================
#           실행 코드 (Execution Code)
# ===============================================

solver = Solution()
print("### 실행 시작 ###\n")

# --- 예제 1 ---
times1 = [[2,1,1],[2,3,1],[3,4,1]]
n1, k1 = 4, 2
print(f"--- 예제 1: times={times1}, n={n1}, k={k1} ---")
result1 = solver.networkDelayTime(times1, n1, k1)
print(f"\n>>> 최종 결과: {result1} (예상 결과: 2)\n")

# --- 예제 2 ---
times2 = [[1,2,1]]
n2, k2 = 2, 1
print(f"--- 예제 2: times={times2}, n={n2}, k={k2} ---")
result2 = solver.networkDelayTime(times2, n2, k2)
print(f"\n>>> 최종 결과: {result2} (예상 결과: 1)\n")

# --- 예제 3 ---
times3 = [[1,2,1]]
n3, k3 = 2, 2
print(f"--- 예제 3: times={times3}, n={n3}, k={k3} ---")
result3 = solver.networkDelayTime(times3, n3, k3)
print(f"\n>>> 최종 결과: {result3} (예상 결과: -1)\n")