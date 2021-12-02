# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, 0)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result) # 최종 답안 출력