n = int(input())
B = list(map(int, input().split()))
A = []

A.append(B[0])

for i in range(1, n):
    a_i = B[i] * (i+1) - sum(A)
    A.append(a_i)

for i in A:
    print(i, end=' ')