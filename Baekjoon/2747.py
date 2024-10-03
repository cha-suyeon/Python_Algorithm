# 1 
n = int(input())

def fibo(n):
    a = 1
    b = 1
    if n == 1 or n == 2:
    	return 1
    for i in range(3, n+1):
        a, b = b, a + b
    return b
    
print(fibo(n))

# 2
n = int(input())

def fibo(n, memo={}):
	if n in memo:
		return memo[n]
	if n == 1 or n == 2:
		return 1
	memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
	return memo[n]

print(fibo(n))

# fibo(5)일 때, memo에는 아직 값이 없으므로 fibo(4), fibo(3) 호출 => 3 + 2 = 5
# fibo(4) 호출도 마찬가지로 fibo(3) + fibo(2) = 2 + 1 = 3
# fibo(3) -> fibo(2) + fibo(1) = 1 + 1 = 2
# fibo(2) -> 1 반환
# fibo(1) -> 1 반환
