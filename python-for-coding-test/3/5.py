# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = []
data = []
for i in range(n):
    data = list(map(int, input().split()))
    value = min(data)
    result.append(value)
    
print(max(result))
