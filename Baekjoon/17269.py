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