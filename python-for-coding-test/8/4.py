# 메모이제이션 동작 분석
d = [0] * 100

def fib(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fib(x-1) + fib(x-2)
    return d[x]

fib(6)