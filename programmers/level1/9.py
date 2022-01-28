# 약수의 합
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer

## 다른 사람 풀이
def solution(n):
	return n + sum([i for i in range(1, (n//2) +1) if n % i == 0])
"""
약수에 언제나 입력값 n은 포함되므로 n을 기본으로 더하면서
n //2 를 해주어 range((n//2)+1) 로 범위 지정을 한 다음에
n % i == 0 의 조건 넣어주기
이렇게 했을 때 좋은 이유는 범위가 반으로 줄어서 성능이 향상된다
"""

## 다른 사람 풀이 2
def solution(n):
    return sum([i for i in range(1,n+1) if n%i==0])
# 나와 같은 코드인데 sum을 이용하여 list comprehension 이용

