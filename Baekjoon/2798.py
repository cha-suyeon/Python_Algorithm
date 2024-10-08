# card에서 N 장을 골라 M에 가장 가깝게 만드는 게임
from itertools import combinations

N, M = map(int, input().split())
card = list(map(int, input().split()))

# N장씩 골라서 더한 다음 M이랑 비교해서 차이가 제일 적은 걸 고르는 방법
# combination에 모든 조합 경우의 수가 담긴 객체 정보 저장
# 조합이 튜플로 나옴 - 튜플에 sum 가능 / 처음부터 list로 변형하거나 .. 

max_sum = 0

for combo in combinations(card, 3):
    com_sum = sum(combo)
    if com_sum <= M and com_sum > max_sum:
        max_sum = com_sum 

print(max_sum)