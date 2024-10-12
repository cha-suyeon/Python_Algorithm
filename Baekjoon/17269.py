N, M = map(int, input().split())
n1, n2 = map(str, input().split())

n1 = list(n1)
n2 = list(n2)

cnt = list('32124313113132122212111221')

for i, char in enumerate(n1):
    index = ord(char) - ord('A')
    n1[i] = cnt[index]

for j, char2 in enumerate(n2):
    idx = ord(char2) - ord('A')
    n2[j] = cnt[idx]

if N > M:           # 첫 번째 이름이 더 긴 경우
    min_len = M
    max_len = N
    max_name = n1
else:               # 두 번쩨 이름이 더 긴 경우
    min_len = N
    max_len = M
    max_name = n2

# 이름 숫자로 모두 변경하고, 더 긴 이름은 뒤에 추가
result = []
for pair in zip(n1, n2):
    result.extend(pair)

result.extend(max_name[min_len:max_len])

# 궁합이 나올 때까지 반복
while len(result) > 2:
    result2 = []
    for i in range(len(result) - 1):
        number = int(result[i]) + int(result[i+1])
        if number >= 10:
            number = number % 10
        result2.append(number)
    result = result2

# 01 일 경우, 1로 나오게 string으로 다시 변환
result = int(''.join(map(str, result)))

print(f"{result}%")

####
N, M = map(int, input().split())
n1, n2 = input().split()

cnt = '32124313113132122212111221'

n1 = [cnt[ord(char) - ord('A')] for char in n1]
n2 = [cnt[ord(char) - ord('A')] for char in n2]

result = []
for i in range(min(N, M)):
    result.append(n1[i])
    result.append(n2[i])

# 더 긴 이름의 나머지 부분 추가
if N > M:
    result.extend(n1[M:])
else:
    result.extend(n2[N:])

result.extend(max_name[min_len:])

while len(result) > 2:
    temp_result = []
    for i in range(len(result) - 1):
        number = int(result[i]) + int(result[i + 1])
        temp_result.append(str(number % 10))
    result = temp_result

print(f"{result[0]}{result[1]}%")