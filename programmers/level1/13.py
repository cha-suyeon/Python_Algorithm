# 두 정수의 합

## 나의 이전 풀이
def solution(a, b):
    answer = 0

    if a==b:
        return a
    elif a>b:
        for i in range(b, a+1): answer+=i
    else :
        for i in range(a, b+1): answer+=i

    return answer

## 나의 풀이 2
def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a < b:
        answer = sum(range(a,b+1))
    else:
        answer = sum(range(b,a+1))
    return answer

## 남의 풀이 1
def solution(a,b):
    if a > b : a, b = b, a
    return sum(range(a,b+1))

## 남의 풀이 2
def solution(a,b):
    return (abs(a-b)+1*(a+b))//2

## 남의 풀이 3
def solution(a,b):
    return sum(range(min(a,b),max(a.b)+1))