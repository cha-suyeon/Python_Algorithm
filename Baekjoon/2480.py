# 1
a, b, c = map(int, input().split())

dice = [a, b, c]
count = [0] * 7
result = 0

for num in dice:
    count[num] += 1

if 3 in count:
    number = count.index(3)
    result = 10000 + number * 1000
elif 2 in count:
    number = count.index(2)
    result = 1000 + number * 100
else:
    max_number = max(dice)
    result = max_number * 100
    
print(result)

# 2
from collections import Counter

dice = list(map(int, input().split()))
count = Counter(dice)

if len(count) == 1:
    number = dice[0]
    result = 10000 + (number * 1000)
elif len(count) == 2:
    for num, cnt in count.items():
        if cnt == 2:
            result = 1000 + (num * 100)
            break
else:
    max_num = max(dice)
    result = max_num * 100

print(result)
