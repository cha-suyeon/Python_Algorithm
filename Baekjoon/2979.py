A, B, C = map(int, input().split())
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

# 1 2 3 3 3 2 1 1 ... 
time_count = [0] * 101
total = 0

for i in range(a, b):
    time_count[i] += 1
for i in range(c, d):
    time_count[i] += 1
for i in range(e, f):
    time_count[i] += 1

for cnt in time_count:
    if cnt == 1:
        total += A * 1
    if cnt == 2:
        total += B * 2
    if cnt == 3:
        total += C * 3

print(total)