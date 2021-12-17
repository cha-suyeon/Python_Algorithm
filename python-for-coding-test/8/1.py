# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fib(x):
    if x == 1 or x == 2:
        return 1
    return fib(x-1) + fib(x-2)

print(fib(4))