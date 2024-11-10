N, M = map(int, input().split()) # 스크린 크기 N, 바구니 크기 M
J = int(input())

left = 1
right = M
total = 0

for _ in range(J):
    pos = int(input())
    
    if left <= pos <= right:
        continue
    elif pos < left:
        move = left - pos
        left -= move
        right -= move
        total += move
    elif pos > right:
        move = pos - right
        left += move
        right += move
        total += move

print(total)
