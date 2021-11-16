# Section 03
## 큐 작동을 위한 통합 코드 수정 ##

def isQueueFull():                      # 큐가 꽉 찼는지 확인하는 함수 개선 버전
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE-1) and (front == -1):
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False
    
def isQueueEmpty():                     # 큐가 비었는지 체크하는 함수
    global SIZE, queue, rear, front
    if (front == rear):
        return True
    else:
        return False
    
def enQueue(data):                      # 큐에 데이터를 삽입하는 함수
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data
    
def deQueue():                          # 큐에서 데이터를 추출하는 함수
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None         
    return data

def peek():                             # 큐에서 front+1 위치의 데이터를 확인하는 함수
    global SIZE, queue, rear, front
    if (isQueueEmpty()):
        print('큐가 비었습니다.')
        return None
    return queue[front+1]

## 전역 변수 선언 부분 ##
SIZE = int(input('큐 크기를 입력하세요 -->'))
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인 코드 부분 ##
if __name__ == "__main__":
    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 -->')
    
    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input('입력할 데이터-->')
            enQueue(data)
            print('큐 상태:', queue)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print('추출된 데이터 -->', data)
            print('큐 상태:', queue)
        elif select == 'V' or select == 'v':
            data = peek()
            print('확인된 데이터 ==>', data)
            print('큐 상태:', queue)
        else:
            print('입력이 잘못됨')
        
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==>')
        
    print('프로그램 종료!')