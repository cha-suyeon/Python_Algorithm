from itertools import combinations

key = []
for k in range(9):
    key.append(int(input()))

max_sum = 0
M = 100
resulut = []

for k in combinations(key, 7):
    key_sum = sum(k)
    if key_sum <= M and key_sum > max_sum:
        max_sum = key_sum
        result = list(k)

result.sort()

for num in result:
    print(num)