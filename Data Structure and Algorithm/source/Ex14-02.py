## 함수 선언 부분 ##
def recu_fibo(n) :
	global  count_recu
	count_recu += 1
	if n < 2 :
		return 1
	else :
		return recu_fibo(n-1) + recu_fibo(n-2)

def dp_fibo(n):
	global count_dp
	memo = [1, 1]
	if n < 2 :
		return memo[n]
	else :
		for i in range(2, n+1) :
			memo.append(memo[i-1] + memo[i-2])
			count_dp += 1
		return memo[n]


## 전역 변수 선언 부분 ##
count_dp, count_recu = 0, 0

## 메인 코드 부분 ##
print(' ## 30번째 피보나치 수열 ##')

res = recu_fibo(30)
print('재귀 방식 --> 답:', res, ', 반복수 : ', count_recu)

res = dp_fibo(30)
print('DP 방식 --> 답:', res, ', 반복수 : ', count_dp)

