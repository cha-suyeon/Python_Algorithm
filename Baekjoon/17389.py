N = int(input())
S = input()

bonus = 0
score = 0

for i, ox in enumerate(S, start=1):
    if ox == 'O':
        bonus += 1
        score += i + bonus - 1
    else:
        bonus = 0

print(score)

# 2
N = int(input())
S = input()

bonus = 0
score = 0

for i, ox in enumerate(S, start=1):
    if ox == 'O':
        score += i + bonus
        bonus += 1

    else:
        bonus = 0

print(score)