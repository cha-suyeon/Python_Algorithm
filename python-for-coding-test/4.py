# L: 왼쪽, R: 오른쪽, U: 위, D: 아래
# 여행가가 밖으로 나가는 움직임은 무시, (0, n), (n, 0)이 되면 무시
# n = 5, p = [R, R, R, U, D, D] -> '3, 4' 가 나와야 함

n = int(input("공간의 크기==>"))
p = input('이동할 계획서==>').split()

# 현재 위치
x, y = 1, 1

# 방향 설정
d = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 이동 계획 하나씩 확인
for plan in p:
    # 이동 후 좌표값 구하기
    for i in range(len(d)):
        if plan == d[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
