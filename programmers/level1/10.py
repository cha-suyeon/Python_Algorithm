# 서울에서 김서방 찾기

## 나의 풀이 1
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = '김서방은 {}에 있다'.format(i)
    return answer

## 나의 풀이 2
def solution(seoul):
    count = -1 
    for i in seoul:
        count += 1
        if i == 'Kim':
            answer = '김서방은 {}에 있다'.format(count)
    return answer

## 다른 사람 풀이
# 값의 인덱스 번호를 찾아주는 index()를 사용한 간단한 풀이이다.
def solution(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))


"""
이 문제를 풀 때 알아야 할 것은
(1) format을 활용할 줄 아는가?
(2) 내장 함수 index()를 아는가?
였다.
"""