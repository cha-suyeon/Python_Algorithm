n = int(input())
score = list(map(int, input().split()))

max_score = max(score)
min_score = min(score)
diff = max_score - min_score

print(diff)