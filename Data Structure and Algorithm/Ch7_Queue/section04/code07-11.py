# Section 04
# 01 원형 큐의 개념(Circular Queue)
# 큐의 처음과 끝이 연결된 구조이다.
# 순차 큐처럼 배열로 구현하되 큐의 끝에 다다르면 다시 처음으로 이어지도록 처리한다.

# 원형 큐 작동을 위한 통합 코드

## 함수 선언 부분 ##
from typing import Sized


def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1) % SIZE == front):      # 큐가 가득차 있는 상태
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front==rear):                   # 큐가 비어있는 상태
        return True
    else:
        return False
    
def enQueue(data):                      # 데이터 삽입을 위한 함수
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 가득찼습니다.")
        return
    rear = (rear+1) % SIZE
    queue[rear] = data
    
def deQueue():                          # 데이터 추출을 위한 함수
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():                             # 확인을 위한 함수
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[(front+1) % SIZE]

## 전역 변수 선언 부분 ##
SIZE = int(input("큐 크기를 입력하세요==>"))
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 -->')
    
    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input('입력할 데이터-->')
            enQueue(data)
            print('큐 상태:', queue)
            print('front:', front, ", rear:", rear)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print('추출된 데이터 -->', data)
            print('큐 상태:', queue)
            print('front:', front, ", rear:", rear)
        elif select == 'V' or select == 'v':
            data = peek()
            print('확인된 데이터 ==>', data)
            print('큐 상태:', queue)
            print('front:', front, ", rear:", rear)
        else:
            print('입력이 잘못됨')
        
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==>')
        
    print('프로그램 종료!')