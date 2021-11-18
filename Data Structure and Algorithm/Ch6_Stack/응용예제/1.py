# Chapter 06. Stack - 응용예제 1번

# 색상이 다른 돌을 6개 준비하고 순서를 임의로 섞는다.
# 과자 집에 가는 길에 떨어드린 돌의 색깔을 스택에 삽입한다.
# 그리고 돌의 색상을 출력한다.
# 최종적으로 돌을 떨어뜨린 순서로 출력한다.
# 집으로 돌아가는 길에 스택에서 추출하여 돌의 색상을 떨어뜨린 반대 순서로 출력한다.

# 출력 되어야 하는 코드
# 과자집에 가는길: 보라 --> 빨강 --> 초록 --> 파랑 --> 주황 --> 노랑 --> 과자집
# 우리집에 가는길: 노랑 --> 주황 --> 파랑 --> 초록 --> 빨강 --> 보라 --> 우리집

import random

# 스택이 꽉 찼는지 확인하는 함수
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False


# 스택이 비었는지 확인하는 함수
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False


# 스택에 데이터를 삽입하는 함수
def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('Stack is Full')
        return
    top += 1
    stack[top] = data


# 스택에 데이터를 추출하는 함수
def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is Empty')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


# 스택에서 top 위치의 데이터를 확인하는 함수
def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is Empty')
        return None
    return stack[top]


## 전역 변수 선언 부분 ##
SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1


## 메인 코드 부분 ##
if __name__ == "__main__":
    
    stoneArray = ['주황', '초록', '파랑', '보라', '빨강', '노랑']
    random.shuffle(stoneArray)

    print("과자집에 가는길:", end=' ')
    for stone in stoneArray:
        push(stone)
        print(stone, '-->', end=' ')
    print('과자집')

    print("우리집에 가는길:", end=' ')
    while True:
        stone = pop()
        if stone == None:
            break
        print(stone, '-->', end=' ')
    print('우리집')