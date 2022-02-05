# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()    
    return answer

## 남의 코드 1
def solution1(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]

## 남의 코드 2
def solution2(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]

## 남의 코드 3
def solution3(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    if not answer:
        answer = [-1]
        
    answer.sort()
    return answer
