# 가로:m, 세로:n
N, M = map(int, input().split())

# 탐색하게 될 그래프
graph = []
for i in range(N):
	graph.append(list(map(int, input())))

# dfs 메서드 정의
def dfs(x, y):
	# 행렬 범위 벗어나면 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if graph[x][y]==0:
        graph[x][y] == 1
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True   
    return False

count = 0

for n in range(N):
    for m in range(M):
        if dfs(n,m):
            count += 1
            
print(count)