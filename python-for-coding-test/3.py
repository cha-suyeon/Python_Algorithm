# L: 왼쪽, R: 오른쪽, U: 위, D: 아래
# 여행가가 밖으로 나가는 움직임은 무시, (0, n), (n, 0)이 되면 무시

N = int(input("공간의 크기==>"))
P = list(input('이동할 계획서==>').split())
A = [1,1]

for p in P: # R R R U D D
    if p == 'L':
        A[1] -= 1
    elif p == 'R':
        A[1] += 1
    elif p == 'U':
        A[0] -= 1
    elif p == 'D':
        A[0] += 1
    for i in range(2):
        if A[i] < 1 :
            A[i] += 1
            continue
        if A[i] > N:
            A[i] -= 1
            continue

print(A)

